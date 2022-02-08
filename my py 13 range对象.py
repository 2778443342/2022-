sum_all=0          #1-100所有数的累加和
sum_even=0        #1-100偶数的累加和
sum_odd=0          #1-100奇数的累加和
for x in range(101):
    sum_all +=x
    if x%2==1:
        sum_odd +=x
    else:
        sum_even +=x
print("1-100累计和{0},奇数和{1},偶数和{2}".format(sum_all,sum_odd,sum_even))