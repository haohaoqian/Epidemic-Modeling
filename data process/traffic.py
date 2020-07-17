import json

a=[[466, 140000], [458, 80000], [324, 100000], [163, 100000], [255, 50000]]
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\traffic.json','w') as f:
        json.dump(a,f)