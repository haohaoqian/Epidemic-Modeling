import json

LIST1=[1.0,0.8,0.5]
LIST2=[1.0,0.5,0.1]
A=[]
for i1 in LIST1:
    temp=[]
    for i2 in LIST2:
        with open ('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment2\\{}β\\result-500d-50infected-nonhospital-{}traffic-nonincome.json'.format(i1,i2),'r') as f:
            data=json.load(f)
        acc=0
        for i in range(675):
            acc+=sum(data[-1][i])
            acc-=data[-1][i][0]
        temp.append(acc)
        print('-')
    A.append(temp)
with open ('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment2\\accumulate.json','w') as f:
    json.dump(A,f)