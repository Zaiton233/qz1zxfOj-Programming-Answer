# 描述
# 暑假来了，天气特别热，花花到冷饮店来买冷饮；已知雪糕2.5元/支，碎碎冰1.5元/支，花花买了x支雪糕和y支碎碎冰，
# 老板说今天有优惠，可以有1支雪糕免费，请问花花应该付给老板多少钱？

# 输入
# 两个整数x和y，分别代表了雪糕和碎碎冰的购买数量。

# 输出
# 一个小数，代表了花花应付给老板的金额（结果保留1位小数）。
x,y=map(int,input().split())
print(format(2.5*(x-1)+1.5*y, '.1f'))