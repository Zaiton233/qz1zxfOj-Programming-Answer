#描述
#求恰好使s=1+1/2+1/3+…+1/n的值大于X时n的值。(2<=x<=10)

#输入
#输入只有一行，包括1个整数X。

#输出
#输出只有一行（这意味着末尾有一个回车符号），包括1个整数。
n=int(input())
i=1
sum=0
while sum<=n:
  sum=1/i+sum
  i=i+1
print(i-1)
