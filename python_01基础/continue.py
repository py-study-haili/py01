# continue

i = 0
sum = 0

while i<10:
    i += 1
    if i == 6:
        continue
    sum += i
    print(i)
print('结果是 %d' % sum)