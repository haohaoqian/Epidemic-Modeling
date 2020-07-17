import json

times=10
for I in range(times):
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\result-20d-50infected-nonhospital-1traffic-nonincome-time{}.json'.format(I+1),'r') as f:
        data=json.load(f)
        data1=data[-1]
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\resultlast-20d-50infected-nonhospital-1traffic-nonincome-time{}.json'.format(I+1),'w') as f:
        json.dump(data1,f)