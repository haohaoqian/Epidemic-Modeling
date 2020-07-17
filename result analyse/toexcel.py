import xlwt
import json

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','r') as f:
    dense=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','r') as f:
    flow=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\marker_region.json','r') as f:
    marker=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-1.json','r') as f:
    acc1=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-2.json','r') as f:
    acc2=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-3.json','r') as f:
    acc3=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-4.json','r') as f:
    acc4=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-5.json','r') as f:
    acc5=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-1.json','r') as f:
    num1=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-2.json','r') as f:
    num2=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-3.json','r') as f:
    num3=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-4.json','r') as f:
    num4=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-5.json','r') as f:
    num5=json.load(f)


workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('sheet1')
for i in range(len(dense)):
    worksheet.write(i+2,0,i+1)
    worksheet.write(i+2,1,marker[i])
    worksheet.write(i+2,2,dense[i])
    worksheet.write(i+2,3,flow[i])

    worksheet.write(i+2,5,acc1[i][2])
    worksheet.write(i+2,6,acc1[i][4])
    worksheet.write(i+2,7,num1[i][1])
    worksheet.write(i+2,8,num1[i][2])
    worksheet.write(i+2,9,num1[i][3])
    worksheet.write(i+2,10,num1[i][4])

    worksheet.write(i+2,11,acc2[i][2])
    worksheet.write(i+2,12,acc2[i][4])
    worksheet.write(i+2,13,num2[i][1])
    worksheet.write(i+2,14,num2[i][2])
    worksheet.write(i+2,15,num2[i][3])
    worksheet.write(i+2,16,num2[i][4])

    worksheet.write(i+2,18,acc3[i][2])
    worksheet.write(i+2,19,acc3[i][4])
    worksheet.write(i+2,20,num3[i][1])
    worksheet.write(i+2,21,num3[i][2])
    worksheet.write(i+2,22,num3[i][3])
    worksheet.write(i+2,23,num3[i][4])

    worksheet.write(i+2,25,acc4[i][2])
    worksheet.write(i+2,26,acc4[i][4])
    worksheet.write(i+2,27,num4[i][1])
    worksheet.write(i+2,28,num4[i][2])
    worksheet.write(i+2,29,num4[i][3])
    worksheet.write(i+2,30,num4[i][4])

    worksheet.write(i+2,32,acc5[i][2])
    worksheet.write(i+2,33,acc5[i][4])
    worksheet.write(i+2,34,num5[i][1])
    worksheet.write(i+2,35,num5[i][2])
    worksheet.write(i+2,36,num5[i][3])
    worksheet.write(i+2,37,num5[i][4])

workbook.save('c:\\users\\郝千越\\desktop\\data.xls')