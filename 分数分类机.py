a = int(input('请输入您的分数:'))
if (a < 0 or a > 100):
    print('分数不合适,请重新输入分数')
elif (a < 60):
    print('分数不合格')
elif (a < 80):
    print('合格')
else:
    print('优秀')