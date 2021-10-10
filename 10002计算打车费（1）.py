# 描述
# 某市出租车的收费标准：
# 小于等于3千米收10元；
# 超过3千米，每千米加收2元；
# 请设计一个计费程序，能根据打车里程自动计算打车费用。

# 输入
# 只有一行，包括1个实数，表示打车里程数。

# 输出
# 只有一行，包括1个实数（保留两位小数），表示打车费用。
d=float(input())
if d<=3:
    price=10
    print(format(price, '.2f'))
else:
    price=(d-3)*2+10
    print(format(price, '.2f'))