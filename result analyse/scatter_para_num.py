import json
import matplotlib.pyplot as plt
import numpy as np

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','r') as f:
    dense=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','r') as f:
    flow=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region_marker.json','r') as f:
    marker=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-1.json','r') as f:
    para1=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-2.json','r') as f:
    para2=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-3.json','r') as f:
    para3=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-4.json','r') as f:
    para4=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-5.json','r') as f:
    para5=json.load(f)

marker=np.array(marker)
dense=np.array(dense)*marker
dense=dense[dense!=0]
flow=np.array(flow)*marker
flow=flow[flow!=0]

para1=np.array(para1)
para2=np.array(para2)
para3=np.array(para3)
para4=np.array(para4)
para5=np.array(para5)

sigma1=para1[:,1]
sigma2=para2[:,1]
sigma3=para3[:,1]
sigma4=para4[:,1]
sigma5=para5[:,1]
sigma1=sigma1*marker
sigma1=sigma1[sigma1!=0]
sigma2=sigma2*marker
sigma2=sigma2[sigma2!=0]
sigma3=sigma3*marker
sigma3=sigma3[sigma3!=0]
sigma4=sigma4*marker
sigma4=sigma4[sigma4!=0]
sigma5=sigma5*marker
sigma5=sigma5[sigma5!=0]
sigma=(sigma1+sigma2+sigma3+sigma4+sigma5)/5

mu1=para1[:,2]
mu2=para2[:,2]
mu3=para3[:,2]
mu4=para4[:,2]
mu5=para5[:,2]
mu1=mu1*marker
mu1=mu1[mu1!=0]
mu2=mu2*marker
mu2=mu2[mu2!=0]
mu3=mu3*marker
mu3=mu3[mu3!=0]
mu4=mu4*marker
mu4=mu4[mu4!=0]
mu5=mu5*marker
mu5=mu5[mu5!=0]
mu=(mu1+mu2+mu3+mu4+mu5)/5

m1=para1[:,3]
m2=para2[:,3]
m3=para3[:,3]
m4=para4[:,3]
m5=para5[:,3]
m1=m1*marker
m1=m1[m1!=0]
m2=m2*marker
m2=m2[m2!=0]
m3=m3*marker
m3=m3[m3!=0]
m4=m4*marker
m4=m4[m4!=0]
m5=m5*marker
m5=m5[m5!=0]
m=(m1+m2+m3+m4+m5)/5

fig=plt.figure(figsize=(20,15))
plt.scatter(dense,m,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0,np.max(dense)*1.05)
plt.xlabel('Population density(people/km^2)')
plt.ylabel('Para-m',fontsize=15)
plt.title('Population density & Para-m',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(flow,m,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.2,1.05)
plt.xlabel('Relatively flow')
plt.ylabel('Para-m',fontsize=15)
plt.title('Relatively flow & Para-m',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(dense,mu,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0,np.max(dense)*1.05)
plt.xlabel('Population density(people/km^2)')
plt.ylabel('Para-$\\mu$',fontsize=15)
plt.title('Population density & Para-$\\mu$',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(flow,mu,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.2,1.05)
plt.xlabel('Relatively flow')
plt.ylabel('Para-$\\mu$',fontsize=15)
plt.title('Relatively flow & Para-$\\mu$',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(dense,sigma,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0,np.max(dense)*1.05)
plt.xlabel('Population density(people/km^2)')
plt.ylabel('Para-$\\sigma$',fontsize=15)
plt.title('Population density & Para-$\\sigma$',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(flow,sigma,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.2,1.05)
plt.xlabel('Relatively flow')
plt.ylabel('Para-$\\sigma$',fontsize=15)
plt.title('Relatively flow & Para-$\\sigma$',fontsize=15)
plt.show()

p=np.corrcoef([dense,flow,sigma,mu,m])
print(p)

t1=para1[:,4]
t2=para2[:,4]
t3=para3[:,4]
t4=para4[:,4]
t5=para5[:,4]
t1=t1*marker
t1=t1[t1!=0]
t2=t2*marker
t2=t2[t2!=0]
t3=t3*marker
t3=t3[t3!=0]
t4=t4*marker
t4=t4[t4!=0]
t5=t5*marker
t5=t5[t5!=0]
t=(t1+t2+t3+t4+t5)/5
print(np.mean(t))