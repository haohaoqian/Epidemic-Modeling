import json

record=[]
LIST=[670,607,236,587,411,28,124,505,498,501,387,666]
for j in LIST:
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\result-365d-region{}-average.json'.format(j),'r') as f:
        data=json.load(f)
    temp=0
    date=0
    for t in range(len(data)):
        I=0
        for k in range(len(data[0])):
            I+=data[t][k][2]
        if(I>temp):
            temp=I
            date=t
    record.append([temp/11000000,date])
    print(temp/11000000,date)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\peak_record.json','w') as f:
    json.dump(record,f)