/*
Description
牛牛最近学习了C++入门课程，这门课程的总成绩计算方法是：
总成绩=作业成绩 × 20% + 小测成绩 × 30% + 期末考试成绩 × 50%
牛牛想知道，这门课程自己最终能得到多少分。

Input
三个非负整数A、B、C，分别表示牛牛的作业成绩、小测成绩和期末考试成绩。相邻两个数之间用一个空格隔开，三项成绩满分都是100分。

Output
一个整数，即牛牛这门课程的总成绩，满分也是100分。*/

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main()
{
	int a, b, c, sum;
	cin >> a;
	cin >> b;
	cin >> c;
	sum = 0.2*a + 0.3*b + 0.5*c;
	cout << sum << endl;
}