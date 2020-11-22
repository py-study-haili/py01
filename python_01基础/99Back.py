start=9
lineStart=1
while start>0:
    lineStart=1
    while lineStart<=start:
        print('*',end="")
        lineStart+=1
    print('')
    start-=1