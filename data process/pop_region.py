import json
import numpy as np

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_record.json','r') as f:
    pop_record=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_sum.json','r') as f:
    pop_sum=json.load(f)
pop_region=np.zeros(675,dtype=np.int)
for j in range(336,672):
    for i in range(675):
        pop_region[i]+=int((11000000/pop_sum[j])*pop_record[j][i])
for i in range(675):
    pop_region[i]=int(pop_region[i]/336)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region.json','w') as f:
    json.dump(pop_region.tolist(),f)