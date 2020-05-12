import random
secret = random.randint(1,10)
temp = input("请猜猜wyf现在心里想的是什么数字：")
guess = int(temp)
times = 1

while guess != secret and times <= 3:
    if guess < secret :
        print("太小了")
    else:
        print("太大了")

    temp = input("请继续猜测：")
    guess = int(temp)
    times = times + 1

if guess == secret and times < 3:
    print("你可这是个小机灵鬼")
else:
    print("难受啊，次数用完了！")

print("GAME OVER！")