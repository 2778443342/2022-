x=int(input("请输入x坐标"))
y=int(input("请输入y坐标"))
if(x==0 and y==0):
    print("原点")
elif(x==0):
    print("y轴")
elif(y==0):
    print("x轴")
elif(x>0 and y>0):
    print("第一象限")
elif(x<0 and y>0):
    print("第二象限")
elif(x<0 and y<0):
    print("第三象限")
else:
    print("第四象限")
