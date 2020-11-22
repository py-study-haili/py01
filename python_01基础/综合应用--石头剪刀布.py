# 综合应用 石头剪刀布

customer = int(input('请输入您要出的拳'))
cusTrans = ''
computer = 1

if customer ==1:
    cusTrans = '石头'
elif customer ==2:
    cusTrans = '剪刀'
else:
    cusTrans = '布'

print(cusTrans)
print('玩家出的拳头是 %d, 玩家出的拳头是 %d' %(customer,computer))

if (customer ==1 and computer == 2):
    print('玩家胜')
elif customer ==2 and computer == 3:
    print('玩家胜')
elif customer == 3 and computer == 1:
    print('玩家胜')
elif customer ==  computer:
    print('平局')
else:
    print('电脑胜')