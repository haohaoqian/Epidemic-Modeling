import numpy as np
import json
from node import node
from node import I_h
from cal import cal

if __name__=='__main__':
    #载入人口流动模式
    print('Loading dynamic pattern...')
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\od_prob.json','r') as f:
        od_prob1=json.load(f)
        od_prob1=np.array(od_prob1)
    print('Down!')
    LIST=[0]
    #LIST=[670,607,236,587,411,28,124,505,498,501,387,666,101]
    #LIST=[670,607,236,587,411,28,124,505,498,501,387,666]
    times=1
    for I in LIST:
        income_control=False
        clever_strategy=False
        control_threshold=0#区域封闭阈值
        strategy_freq=0#措施更新频率(30min)
        traffic_restrict=1
        #print('Setting traffic restriction...')
        #od_prob1=od_prob*traffic_restrict
        #print('Down!')
        NI0=1#起始病人数
        NL0=20#起始潜伏数
        for ti in range(times):
            LAST=500#模拟天数
            #m=input('是否载入已有数据 y/n\n')
            m='n'
            if(m=='n'):
                start=3#开始于星期
                I0=[168,169,170,205,208]#发病于I0区域
                #初始化人口
                print('Initializing population...')
                with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region.json','r') as f:
                    pop_region=json.load(f)
                nodes=[]
                region_num=len(pop_region)
                pop_region=np.array(pop_region)
                pop_total=0
                for i in range(region_num):
                    nodes.append(node(i))
                    nodes[i].set_susceptible(pop_region[i])
                    pop_total+=pop_region[i]
                del pop_region
                print('Down!')

                #初始化感染情况
                print('Initializing infection...')
                for k in I0:
                    nodes[k].set_latent(NL0)
                    nodes[k].set_susceptible(nodes[k].susceptible-NL0)
                nodes[170].set_infected(NI0)
                nodes[170].set_susceptible(nodes[170].susceptible-NL0-NI0)
                print('Down!')

                #初始化日期
                print('Initializing start date...')
                START=start
                print('Down!')
            else:
                #START=int(input('重新开始于星期\n'))
                START=7
                print('Loading data...')
                with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\resultlast-20d-50infected-nonhospital-1traffic-nonincome-time1.json','r') as f:
                    data=json.load(f)
                nodes=[]
                region_num=len(data)
                pop_total=0
                for i in range(region_num):
                    nodes.append(node(i))
                    nodes[i].set_susceptible(data[i][0])
                    nodes[i].set_latent(data[i][1])
                    nodes[i].set_infected(data[i][2])
                    nodes[i].set_infected_asymptomatic(data[i][3])
                    nodes[i].set_in_hospital(data[i][4])
                    nodes[i].set_recovered(data[i][5])
                    nodes[i].set_death(data[i][6])
                    pop_total+=sum(data[i])
                print('Down!')

            if (income_control):
                #载入交通场站信息
                print('Loading traffic info...')
                with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\traffic.json','r') as f:
                    traffic=json.load(f)
                station_num=len(traffic)
                print('Down!')

            #开始模拟
            print('Start simulation...')
            statistics=cal(nodes)
            income=[]
            control_mark=np.zeros(region_num)
            control_influency=[]
            S_temp=np.zeros((region_num,region_num+1))
            L_temp=np.zeros((region_num,region_num+1))
            I_temp=np.zeros((region_num,region_num+1))
            Ia_temp=np.zeros((region_num,region_num+1))
            R_temp=np.zeros((region_num,region_num+1))
            for time in range(int(LAST*48)):
                print('time'+str(ti+1)+' step'+str(time+1))
                #区域内部状态转移
                for i in range(region_num):
                    nodes[i].step()
                #区域之间移动
                for k in range(region_num):
                    S_temp[k]=np.random.multinomial(nodes[k].susceptible,od_prob1[((START-1)*48+time)%(7*48)][k])
                    L_temp[k]=np.random.multinomial(nodes[k].latent,od_prob1[((START-1)*48+time)%(7*48)][k])
                    I_temp[k]=np.random.multinomial(nodes[k].infected,od_prob1[((START-1)*48+time)%(7*48)][k])
                    Ia_temp[k]=np.random.multinomial(nodes[k].infected_asymptomatic,od_prob1[((START-1)*48+time)%(7*48)][k])
                    R_temp[k]=np.random.multinomial(nodes[k].recovered,od_prob1[((START-1)*48+time)%(7*48)][k])
                total=0
                if(clever_strategy):
                    if(time%strategy_freq==0):
                        print('Adujsting strategy...')
                        for i in range(region_num):
                            if(nodes[i].infected+nodes[i].in_hospital>=control_threshold):
                                control_mark[i]=1
                            else:
                                control_mark[i]=0
                        print('Down!')
                    for k in range(region_num):
                        S_temp[k][k]=0
                        L_temp[k][k]=0
                        I_temp[k][k]=0
                        Ia_temp[k][k]=0
                        R_temp[k][k]=0
                    total+=np.sum(np.sum(S_temp,axis=0),axis=0)
                    total+=np.sum(np.sum(L_temp,axis=0),axis=0)
                    total+=np.sum(np.sum(I_temp,axis=0),axis=0)
                    total+=np.sum(np.sum(Ia_temp,axis=0),axis=0)
                    total+=np.sum(np.sum(R_temp,axis=0),axis=0)
                    for k in range(region_num):
                        if(control_mark[k]):
                            S_temp[k,:]=0
                            S_temp[:,k]=0
                            L_temp[k,:]=0
                            L_temp[:,k]=0
                            I_temp[k,:]=0
                            I_temp[:,k]=0
                            Ia_temp[k,:]=0
                            Ia_temp[:,k]=0
                            R_temp[k,:]=0
                            R_temp[:,k]=0
                S_temp_sum0=np.sum(S_temp,axis=0)
                L_temp_sum0=np.sum(L_temp,axis=0)
                I_temp_sum0=np.sum(I_temp,axis=0)
                Ia_temp_sum0=np.sum(Ia_temp,axis=0)
                R_temp_sum0=np.sum(R_temp,axis=0)
                S_temp_sum1=np.sum(S_temp,axis=1)
                L_temp_sum1=np.sum(L_temp,axis=1)
                I_temp_sum1=np.sum(I_temp,axis=1)
                Ia_temp_sum1=np.sum(Ia_temp,axis=1)
                R_temp_sum1=np.sum(R_temp,axis=1)
                if(clever_strategy):
                    total1=0
                    total1+=np.sum(S_temp_sum0,axis=0)
                    total1+=np.sum(L_temp_sum0,axis=0)
                    total1+=np.sum(I_temp_sum0,axis=0)
                    total1+=np.sum(Ia_temp_sum0,axis=0)
                    total1+=np.sum(R_temp_sum0,axis=0)
                    control_influency.append((1-(total1/total))*traffic_restrict)
                else:
                    control_influency.append(1-traffic_restrict)
                for k in range(region_num):
                    nodes[k].set_susceptible(nodes[k].susceptible+S_temp_sum0[k]-S_temp_sum1[k]+S_temp[k][region_num])
                    nodes[k].set_latent(nodes[k].latent+L_temp_sum0[k]-L_temp_sum1[k]+L_temp[k][region_num])
                    nodes[k].set_infected(nodes[k].infected+I_temp_sum0[k]-I_temp_sum1[k]+I_temp[k][region_num])
                    nodes[k].set_infected_asymptomatic(nodes[k].infected_asymptomatic+Ia_temp_sum0[k]-Ia_temp_sum1[k]+Ia_temp[k][region_num])
                    nodes[k].set_recovered(nodes[k].recovered+R_temp_sum0[k]-R_temp_sum1[k]+R_temp[k][region_num])
                if(income_control):
                    #交通场站输入
                    if(time%48<12 or time%48>42):
                        percentage=1/143
                    elif(time%48<16 or time%48>36):
                        percentage=5/286
                    else:
                        percentage=5/143
                    statistics.total_nums(nodes)
                    PI=statistics.nums['infected']/pop_total
                    PL=statistics.nums['latent']/pop_total
                    PIa=statistics.nums['asymptomatic']/pop_total
                    income_L_total=0
                    income_I_total=0
                    income_Ia_total=0
                    print(statistics.nums['infected'])
                    for k in range(station_num):
                        income_L,income_I,income_Ia,__=np.random.multinomial(percentage*traffic[k][1],[PL,PI,PIa,1])
                        nodes[traffic[k][0]].infected+=income_I
                        nodes[traffic[k][0]].latent+=income_L
                        nodes[traffic[k][0]].infected_asymptomatic+=income_Ia
                        pop_total+=(income_Ia+income_L+income_I)
                        income_L_total+=income_L
                        income_I_total+=income_I
                        income_Ia_total+=income_Ia
                    income.append([income_I_total,income_L_total,income_Ia_total])
                #保存数据
                save=[]
                for i in range(region_num):
                    temp1=[nodes[i].susceptible,nodes[i].latent,nodes[i].infected,nodes[i].infected_asymptomatic,nodes[i].in_hospital,nodes[i].recovered,nodes[i].death]
                    save.append(temp1)
                save=np.array(save)
                save=save.astype(np.float)
                with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\result_'+str(time)+'.json','w') as f:
                    json.dump(save.tolist(),f)
            if(income_control):
                #保存income数据
                income=np.array(income)
                income=income.astype(np.float)
                with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\result_income.json','w') as f:
                    json.dump(income.tolist(),f)
            if(I_h!=0):
                ss=str(int(1/(48*I_h)))+'day'
            else:
                ss='non'
            if(income_control):
                sss='with'
            else:
                sss='non'
            #保存管制影响数据
            #with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\control_influency-'+str(LAST)+'d-'+str(N0)+'infected-'+ss+'hospital-'+str(traffic_restrict)+'traffic-'+sss+'income-time'+str(ti+1)+'.json','w') as f:
                #json.dump(control_influency,f)
            #with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\control_influency-480d-nonhospital-1.0traffic-{}freq-{}threshold.json'.format(I[0],I[1]),'w') as f:
                #json.dump(control_influency,f)
            #合并文件
            print('Merging data...')
            T=LAST*48 #文件数(=模拟步数)
            result=[]
            for i in range(T):
                with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\result_'+str(i)+'.json','r') as f:
                    temp=json.load(f)
                result.append(temp)
                print('{}/{}'.format(i+1,T))
            print('saving...')
            with open('c:\\users\\郝千越\\desktop\\result.json','w') as f:
                json.dump(result,f)
            #with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\result-'+str(LAST)+'d-'+str(N0)+'infected-'+ss+'hospital-'+str(traffic_restrict)+'traffic-'+sss+'income.json','w') as f:
                #json.dump(result,f)
            #with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\result-'+str(LAST)+'d-'+ss+'hospital-'+str(traffic_restrict)+'traffic-'+sss+'income.json','w') as f:
                #json.dump(result,f)
            #with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\result-300days-3dayhospital-{}traffic.json'.format(I),'w') as f:
                #json.dump(result,f)
            print('Down!')