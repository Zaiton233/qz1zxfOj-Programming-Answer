# 输入2个1000以内的正整数a和b，a < b，输出从a到b的所有整数，数字之间留一个空格。

# Input
# 一行2个正整数：a和b，a < b，范围在[1,1000]。

# Output
# 一行，从a到b的正整数。
a=int(input())
b=int(input())
i=a
ii=b+1
while i<ii:
    print(i,end=' ')
    i=i+1