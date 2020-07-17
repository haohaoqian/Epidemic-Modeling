import json
import matplotlib.pyplot as plt

L=['0','50%','90%','95%','99%','99.5%','99.9%','99.95%','99.99%']
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment2\\1.0β\\peak_record.json','r') as f:
    data1=json.load(f)
date1=[]
peak1=[]
for i in range(9):
    date1.append(data1[i][0]/48)
    peak1.append(data1[i][1])
plt.figure()
plt.plot(L,peak1)
plt.xlabel('Restriction percentage')
plt.ylabel('Infected-num')
plt.title('Infected of traffic-restriction')
plt.grid()
plt.show()