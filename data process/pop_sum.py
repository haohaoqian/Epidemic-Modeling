import json
import numpy as np
import matplotlib.pyplot as plt

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_record.json','r') as f:
    pop_record=json.load(f)
pop_sum=np.sum(pop_record,axis=1)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_sum.json','w') as f:
    json.dump(pop_sum.tolist(),f)
plt.plot(pop_sum)
plt.show()