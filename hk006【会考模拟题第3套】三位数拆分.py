# 描述
# 读入一个三位数，求它的百位，十位，个位及它们的和

# 输入
# 读入一个整数（一定是一个三位数）

# 输出
# 第一行，分别为百位，十位，个位
# 第二行，为它们的和
a=int(input())
a1=a//100
a2=(a-100*a1)//10
a3=a-100*a1-10*a2
print(a1,end=" ")
print(a2,end=" ")
print(a3)
print(a1+a2+a3)