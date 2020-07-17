import json
import numpy as np
LIST=[670,607,236,587,411,28,124,505,498,501,387,666,101]
temp=np.zeros((17520,675,7))
temp1=np.zeros(17520)
for i in LIST:
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\result-365d-region{}-300start.json'.format(i),'r') as f:
        data=json.load(f)
    temp+=np.array(data)
    '''
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result\\effect of traffic-restriction\\control_influency-300d-50infected-3dayhospital-0.001traffic-nonincome-time{}.json'.format(i+1),'r') as f:
        data=json.load(f)
    temp1+=np.array(data)2
    '''
    print('-')
    temp=temp/len(LIST)
'''
temp1=temp1/times
'''
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\result-365d-average-300start.json','w') as f:
    json.dump(temp.tolist(),f)
'''
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment4\\average\\effect of traffic-restriction\\control_influency-300d-50infected-nonhospital-0.001traffic-nonincome.json','w') as f:
    json.dump(temp1.tolist(),f)
'''