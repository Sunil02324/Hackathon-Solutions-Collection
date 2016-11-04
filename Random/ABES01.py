t = int(raw_input())
while t>0:
	t = t-1
	a,b = map(int, raw_input().split())
	print ((a%9)*(b%9))%9

#include <iostream>
# using namespace std;
 
# int main() {
# 	int t;
# 	cin>>t;
# 	while(t--)
# 	{
# 		string a,b;
# 		cin>>a>>b;
# 		int ans1=0;
# 		int ans2=0;
# 		for(int i=0;i<a.length();i++)
# 		{
# 			ans1=ans1+a[i]-'0';
# 		}
# 		for(int i=0;i<b.length();i++)
# 		{
# 			ans2=ans2+b[i]-'0';
# 		}
# 		int res1=ans1%9;
# 		int res2=ans2%9;
# 		int res=(res1*res2)%9;
# 		cout<<res<<endl;
# 	}
# 	return 0;
# } 