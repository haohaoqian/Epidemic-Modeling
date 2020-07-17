import json
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6.4,4.76))
LIST=[24,48,96]
for II in range(len(LIST)):
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment5\\control_influency-500d-nonhospital-1.0traffic-{}freq-2threshold.json'.format(LIST[II]),'r') as f:
        result=json.load(f)
        result=np.array(result)
    time=[]
    for i in range(np.shape(result)[0]):
        time.append(i/48)
    plt.plot(time,result*100,label='$C_f$'+'={}'.format(LIST[II]))
    print('{}/{}'.format(II+1,len(LIST)))
plt.legend(fontsize=15)
plt.xlabel('t(day)',fontsize=15)
plt.ylabel('restrict-ratio(%)',fontsize=15)
plt.tick_params(labelsize=12)
plt.hlines(99.99, -10, 510,linestyle='-.',color="red",linewidth=2)
plt.subplots_adjust(left=0.2,bottom=0.2)
plt.savefig('c:\\users\\郝千越\\desktop\\traffic.png',dpi=100)