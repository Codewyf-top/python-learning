import random
secret = random.randint(1,10)
temp=input("请猜猜codewyf现在心里想的是什么数字：")
guess = int(temp)
times = 1

while guess != secret and times < 3:
    if guess > secret:
        print("太大了")
    else:
        print("太小了")
    times = times + 1

    temp = input("Please try again:")
    guess = int(temp)


if (times <= 3) and (guess == secret):
    print("你可真是个小机灵鬼")
    print("但是你猜中了也没有奖励")
else:
    print("您当前的次数已经用尽，请稍后再试！")
