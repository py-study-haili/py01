# 计算 0-100之间所有偶数的累计求和结果

sum = 0

index = 0

while index<=100:
    if index % 2 ==0:
        print('偶数是 %d' % index)
        sum += index
    index += 1

print('0-100之间的所有偶数求和结果为 %d' %sum)