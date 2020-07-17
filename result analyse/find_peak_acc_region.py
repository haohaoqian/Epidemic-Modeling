import json

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\result-365d-average-300start.json','r') as f:
    data=json.load(f)
peak_date=[]
peak_height=[]
acc=[]
for i in range(len(data[0])):
    temp=0
    date=0
    for j in range(len(data)):
        if(sum(data[j][i])!=0):
            if((data[j][i][2]+data[j][i][3])/sum(data[j][i])>temp):
                temp=(data[j][i][2]+data[j][i][3])/sum(data[j][i])
                date=j
    peak_date.append(date)
    peak_height.append(temp*100)
    if(sum(data[-1][i])!=0):
        acc.append(((sum(data[-1][i])-data[-1][i][0])/sum(data[-1][i]))*100)
    else:
        acc.append(0)
    print(i)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_date_region-300start.json','w') as f:
    json.dump(peak_date,f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_height_region-300start.json','w') as f:
    json.dump(peak_height,f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\acc_region-300start.json','w') as f:
    json.dump(acc,f)