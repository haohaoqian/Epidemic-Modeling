import json

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\result-365d-average-5.json','r') as f:
    data=json.load(f)

start=[0]*len(data[0])
for i in range(len(data)):
    for j in range(len(start)):
        if(data[i][j][2]+data[i][j][3]+data[i][j][4]!=0):
            if(start[j]==0):
                start[j]=i/48

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\start-result-365d-average-5.json','w') as f:
    json.dump(start,f)