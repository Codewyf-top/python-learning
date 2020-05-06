#import this
temp = input("不妨猜一下codewyf现在心里想的是哪个数字：")
guess = int(temp)
"""
if guess == 8:
    print("你可真是个小机灵鬼 !")
    print("但是猜中了也没有奖励.")
else:
    print("难受～猜错了，codewyf现在想的是8!")

print("GAME OVER")"""
#条件分支
"""secret = 8
if guess == secret:
    print("你可真是个小机灵鬼 !")
    print("但是猜中了也没有奖励.")
else:
    if guess > secret:
        print("太大了")
    else:
        print("太小了")"""
#循环
secret = 8
while guess != secret:
    if guess > secret:
        print("太大了")
    else:
        print("太小了")

    temp = input("Please try again:")
    guess = int(temp)

print("你可真是个小机灵鬼")
