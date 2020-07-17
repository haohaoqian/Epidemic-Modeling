#  High Spatial-Temporal Resolution Epidemic Simulator——Version 2.1

##  Log

###  Publish 1.0 2020-4-1

—修改部分参数名称并添加注释，避免混淆30min单位/day单位

—分离数据提取、处理代码与主程序代码，避免每次运行重复处理数据

—将人口流动模式、交通场站信息以参数传入，提供方便的接口研究不同人口流动下的情形

—设置可变参数收治率，提供方便的接口探究不同医疗条件下的人口流动情形

—修正人口流动模拟机制，避免人口数为负的情况

—速度达到模拟现实中1day用时小于30s

—分离结果分析代码与主程序代码，提供方便的途径进行不同维度的数据分析

###  Update to Version 1.1 2020-4-1

—整理删减冗余代码

—修正北京市总人口数至城区人口，约1500万

—增加结果文件合并与曲线绘制代码

###  Update to Version 1.2 2020-4-2

—增加记录各时间节点输入病例数

—补充曲线绘制代码

—更改部分临时变量temp名称

###  Update to Version 2.0 2020-4-2

—增加交通限制因子，可以等比例限制交通

—增加读入数据功能，支持从某一时刻改变条件继续模拟

—整理重构部分代码

—性能优化

###  Update to Version 2.1 2020-4-4

—增加医院容量上限参数

—修改绘图坐标轴刻度为day

—可选是否考虑输入病人

—自动合并结果文件

—支持输入参数表，自动连续模拟多组条件

—加入自动定位感染者峰值时间及高度功能

—性能优化，模拟现实中1day用时小于7s

###  Update to Version 3.0 2020-4-12

—增加智能动态管控措施及相关参数设置

—可分析交通管制带来的流量影响



##  Files List

—epidemic_simulator

​	—data_process

​		—note.txt

​		—od_prob.py

​		—pop_record.py

​		—pop_region.py

​		—pop.sum.py

​		—traffic.py

​	—simulator

​		—node.py

​		—cal.py

​		—main.py

​	—result_analyse

​		—note.txt

​		—curve_plot.py

​		—merge_two_files.py

​		—spilit_last.py



##  Contributors

Qianyue

Minghao
