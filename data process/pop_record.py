import numpy as np
import json

record=np.zeros((1488,675),dtype=np.int)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\raw\\pop_region_30','r') as f:
    for line in f:
        tim_loc,pop=line.strip("\r\n").split("\t")
        time,loc=tim_loc.split('=')
        loc=loc.replace('0-','',1)
        time=int(time)
        pop=int(pop)
        loc=int(loc)
        record[time][loc]=pop
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_record.json','w') as f:
    json.dump(record.tolist(),f)