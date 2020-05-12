"""
成绩按照分数划分等级：90分以上为A，80～90为B，60～80为C，60以下为D
"""
score = int(input("请输入您的分数："))

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 60 <= score < 80:
    print("C")
elif 0 <= score < 60:
    print("D")
else:print("无效成绩录入")