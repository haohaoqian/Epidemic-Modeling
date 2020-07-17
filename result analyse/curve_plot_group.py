import json
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(20,15))
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region670-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='red',linestyle='-',label='region NO.670')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region607-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='blue',linestyle='-',label='region NO.607')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region236-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='green',linestyle='-',label='region NO.236')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region587-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='red',linestyle='--',label='region NO.587')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region411-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='blue',linestyle='--',label='region NO.411')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region28-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='green',linestyle='--',label='region NO.28')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region124-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='red',linestyle='-.',label='region NO.124')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region505-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='blue',linestyle='-.',label='region NO.505')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region498-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='green',linestyle='-.',label='region NO.498')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region501-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='red',linestyle=':',label='region NO.501')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region387-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='blue',linestyle=':',label='region NO.387')
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region666-average.json','r') as f:
    result=json.load(f)
result=np.array(result)
time=[]
analyseI=[]
for i in range(np.shape(result)[0]):
    I=0
    for j in range(np.shape(result)[1]):
        I+=result[i][j][2]
        I+=result[i][j][4]
    analyseI.append(I)
    time.append(i/48)
plt.plot(time,analyseI,color='green',linestyle=':',label='region NO.666')
plt.xlim(0,365)
plt.xlabel('Time(day)',fontsize=15)
plt.ylabel('Infected Number',fontsize=15)
plt.title('Effect of different start region',fontsize=15)
plt.legend(fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid()
plt.show()
print('-')