import json
import matplotlib.pyplot as plt
import numpy as np

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment2\\accumulate.json','r') as f:
    data=json.load(f)

data1=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        data1[i][j]=((data[i][0]-data[i][j])/data[i][0])*100
print(data1)
xaxis=['0','50','90']
plt.figure()
plt.plot(xaxis,data1[0],label='1.0β')
plt.plot(xaxis,data1[1],label='0.8β')
plt.plot(xaxis,data1[2],label='0.5β')
plt.legend()
plt.grid()
plt.xlabel('Traffic-restriction(%)')
plt.ylabel('Decrease on accumulated infected number at 500days(%)')
plt.title('Effect of Traffic-restriction(different β)')
plt.show()