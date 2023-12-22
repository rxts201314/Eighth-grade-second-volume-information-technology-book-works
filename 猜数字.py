import random
the_number = random.randint(1,100)
print('你好，在电脑前的彦祖，亦非，让我们来玩一个猜数字的小游戏吧！')
guess = int(input('请您猜一个1到100之间的神秘数字吧！（包括1和100哦）'))
while guess != the_number:
    if guess > the_number:
        print(guess,'猜大了，请再猜一次！')
    if guess <the_number:
        print(guess,'猜小了，请再猜一次！')
    guess = int(input('再来一次'))
print(guess,'这就是最终的背后数字，恭喜你猜对了！')