import json

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region.json','r') as f:
    data=json.load(f)

region_mark=[1]*len(data)
for i in range(len(data)):
    if(data[i]<300):
        region_mark[i]=0
print(sum(region_mark))

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region_marker.json','w') as f:
    json.dump(region_mark,f)