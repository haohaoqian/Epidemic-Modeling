import json

LIST=[(24,2),(48,2),(96,2)]
for I in LIST:
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment4\\result\\first20days\\result-20d-50infected-nonhospital-1traffic-nonincome-time1.json','r') as f:
        data1=json.load(f)
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\result-480d-nonhospital-1.0traffic-{}freq-{}threshold.json'.format(I[0],I[1]),'r') as f:
        data2=json.load(f)
    data=[]
    for i in range(len(data1)):
        data.append(data1[i])
    for i in range(len(data2)):
        data.append(data2[i])
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment5\\result-500d-nonhospital-1.0traffic-{}freq-{}threshold.json'.format(I[0],I[1]),'w') as f:
        json.dump(data,f)
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment4\\result\\first20days\\control_influency-time1.json','r') as f:
        data1=json.load(f)
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\control_influency-480d-nonhospital-1.0traffic-{}freq-{}threshold.json'.format(I[0],I[1]),'r') as f:
        data2=json.load(f)
    data=[]
    for i in range(len(data1)):
        data.append(data1[i])
    for i in range(len(data2)):
        data.append(data2[i])
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment5\\control_influency-500d-nonhospital-1.0traffic-{}freq-{}threshold.json'.format(I[0],I[1]),'w') as f:
        json.dump(data,f)
    print('-')
