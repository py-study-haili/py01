row=1
lineRow=1
while row<10:
    lineRow=1
    while lineRow <=row:
        # spaceNum="   "
        # if row*lineRow<10 :
        #     spaceNum="   "
        # else:
        #     spaceNum="  "
        # print("%d" % lineRow , '*' ,"%d" % row ,'=' , row*lineRow,end=spaceNum)
        print("%d * %d = %d" % (lineRow, row, row * lineRow),end="\t")
        lineRow+=1
    row+=1
    print('')