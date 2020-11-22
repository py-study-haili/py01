# if嵌套

has_ticket = True
knife_length = 18

if has_ticket:
    print('车票检查通过，请进站')
    if knife_length > 15:
        print('携带了危险物品,有 %d长' %knife_length)
    else:
        print('无管制危险品')
else:
    print('没票，不允许进站')
