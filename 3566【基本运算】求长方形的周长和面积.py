# 描述
# 从键盘读入2个整数，分别代表一个长方形的长和宽，请计算长方形的周长和面积；

# 输入
# 从键盘读入2个整数，用空格隔开

# 输出
# 输出有2行，第1行代表周长，第2行代表面积
a,b =map(int,input('').split())
print(2*a+2*b)
print(a*b)