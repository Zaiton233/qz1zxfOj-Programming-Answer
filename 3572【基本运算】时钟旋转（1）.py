# 描述
# 时钟上面的时针从m时走到n时旋转了多少度？（m<=n，且m和n都是1~12之间的整数）（4.2.4）

# 输入
# 2个整数m和n

# 输出
# 一个整数代表时针旋转的度数
a,b=map(int,input().split())
print(30*(b-a))