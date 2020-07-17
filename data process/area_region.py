import shapely
import pyproj
import json
import numpy as np
from pyproj import Proj
from shapely.geometry import Polygon

with open ('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\raw\\region_beijing_tencent.json','r') as f:
    data=json.load(f)
area=[]
for i in range(675):
    bound=np.array(data['boundary'][i])
    p = Proj('+proj=aea +lon_0=105 +lat_1=25 +lat_2=47 +ellps=krass')
    x,y = p(bound[:,0], bound[:,1])
    polygon = Polygon(np.stack((x,y), axis=1))
    area.append(polygon.area)
with open ('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\area_region.json','w') as f:
    json.dump(area,f)