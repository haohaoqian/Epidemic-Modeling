import json
import numpy as np

result=np.zeros((2880,675,7))
for i in range(10):
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment10\\分散\\result-{}.json'.format(i+1),'r') as f:
        result+=np.array(json.load(f))
    print('-')
result/=10

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment10\\分散\\result.json','w') as f:
    json.dump(result.tolist(),f)