#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const ll mod = 1e9+7;
 
ll cnt[1000010], ans[1000010];
set<ll> st;
 
int main() {
	ll i, j, n, q, k;
	scanf("%lld", &n);
	for(i=1; i<=n; ++i) {
		scanf("%lld", &j);
		st.insert(j);
		cnt[j]++;
	}
	for(auto it=st.begin(); it!=st.end(); ++it) {
		ll x=*it;
		for(j=x*x, k=x; j<=1e6; j+=x, ++k) {
			if(k==x) {
				ll z=cnt[x]*cnt[x]-cnt[x];
				z/=2LL;
				ans[j]=(ans[j]+z)%mod;
			}
			else	ans[j]=(ans[j]+cnt[x]*cnt[k])%mod;
		}
	}
	scanf("%lld", &q);
	while(q--) {
		scanf("%lld", &k);
		i=1;
		ll fin=0;
		while(i*i<k) {
			if(k%i==0) {
				fin=(fin+ans[i]+ans[k/i])%mod;
				//cout<<i<<" "<<k/i<<" "<<ans[i]<<" "<<ans[k/i]<<endl;
			}
			i++;
		}
		if(i*i==k) {
			fin=(fin+ans[i])%mod;
		}
		printf("%lld\n", fin);
	}
	return 0;
} 