import json

with open ('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\area_region.json','r') as f:
    area=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region.json','r') as f:
    pop=json.load(f)
dense=[]
for i in range(675):
    dense.append((pop[i]/area[i])*1000000)
with open ('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','w') as f:
    json.dump(dense,f)