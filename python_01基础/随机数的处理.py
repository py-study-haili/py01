# 随机数的处理

# 导入随机数函数
import random

randomNum = random.randint(1,10)

print(randomNum)

player = int(input('请出拳'))

if randomNum > player:
    print('电脑赢')
elif randomNum == player:
    print('平局')
else :
    print('玩家赢')