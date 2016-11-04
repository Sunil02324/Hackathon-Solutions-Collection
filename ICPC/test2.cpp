#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
long long binary_search(long *A,long long N,long val){
	long long beg=0;
	long long end=N-1;
	long long mid;
	while(beg<=end){
		mid=(beg+end)/2;
		if(beg==end&&A[mid]!=val)
			return -1;
		else if(A[mid]==val)
			return mid;
		else if(A[mid]>val)
			end=mid-1;
		else
			beg=mid+1;
 
	}
	return -1;
}
long long mod_exp(long long x,long long y,long long p){
 
    long long res = 1;      // Initialize result
 
    x = x % p;  // Update x if it is more than or 
                // equal to p
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;
 
        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;  
    }
    return res;
 
 
}
int main() {
	long testcases;
	cin>>testcases;
	long *ini=new long[750001];
	long *fin=new long[750001];
	long long N;
	long *dp=new long[750001];
	bool one_present;
	while(testcases--){
		one_present=false;
		cin>>N;
		long inp;
		for(int i=0;i<N;i++){
			cin>>inp;
			if(inp==1){
				one_present=true;		
				i--;
			}
			else{
 
				ini[i]=inp;
			}
 
		}
		if(one_present)
			N-=1;
		sort(ini,ini+N);
		for(int i=0;i<N;i++)
			dp[i]=0;
		for(int i=0;i<N;i++)
			fin[i]=0;
		long M=ini[N-1];
		for(int i=N-1;i>=0;i--){
			for(int j=2;;j++){
				long long pro=ini[i]*j;
				if(pro>M)
					break;
				else{
					long long ind=binary_search(ini,N,pro);
					if(ind!=-1){
						dp[i]+=(dp[ind]+1);
						fin[ind]=1;
					}
				}
			}
 
		}
		long long ans=0;
		for(int i=0;i<N;i++){
			if(fin[i]==0){
				ans=(ans+mod_exp(2,dp[i],1000000007))%1000000007;
			}
		}
		//considering empty set
		ans=(ans+1)%1000000007;
		if(one_present)
			ans=(ans*2)%1000000007;
		cout<<ans<<endl;
 
 
	}
 
	return 0;
}