# 描述
# 小丽在编程课上学会了拆位运算，她已经可以拆出一个两位整数的十位和个位了，她想知道这个整数的十位/个位的结果是多少，请编程帮她实现？（请注意，计算结果要保留1位小数）

# 输入
# 输入一个两位的正整数n，且n的个位一定不为0。

# 输出
# 输出这个两位正整数十位除以个位的计算结果，结果保留1位小数。
a=int(input())
a1=a//10
a2=(a-10*a1)
sum=a1/a2
print(format(sum, '.1f'))