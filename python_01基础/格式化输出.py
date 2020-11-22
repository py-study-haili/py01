# 定义字符串变量 name 输出 我的名字叫 小明， 请多多关照！
name = "小明"
print("我的名字叫%s" % name)

# 定义整数变量  student_no,输出 我的学号是000001

student_no=1
print("我的学号是%06d" % student_no)

# 定义小数 price、weight、money,
# 输出 苹果单价 9.00 元/斤,购买了5.00斤,总共45.00元
price=8.5
weight=7.5
money=price*weight
print("苹果单价 %.02f 元/斤，购买了 %.02f 斤， 总共 %.02f 元" % (price,weight,money))

scale=10
print('数据比例是 %.02f' % scale)
print('格式化字符串 %04d' % scale)
print('格式化字符串 %.2f%%' % scale)

# 定义一个小数 bit 输出 数据比例是 32.5%
bit=0.325
print('数据比例是 %.1f%%' % (bit*100))