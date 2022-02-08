for x in(10,20,30):
    print(x*3)

for x in"abcdef":
    print(x)

d={"name":"高淇","age":18,"job":"程序员"}
#默认打印健
for x in d:
    print(x)
#打印健
for x in d.keys():
    print(x)
#打印值
for x in d.values():
    print(x)
#打印键值对
for x in d.items():
    print(x)