# 描述
# 花花去文具店买了1支笔和1块橡皮，已知笔x元/支，橡皮y元/块，花花付给了老板n元，请问老板应该找给花花多少钱？

# 输入
# 三个整数x、y、n，分别代表了笔的单价、橡皮的单价和花花付给老板的钱（已知花花付给老板的钱n>=x+y）。

# 输出
# 一个整数，代表老板应该找给花花的钱。
a,b,c =map(int,input('').split())
s=c-(a+b)
print(s)