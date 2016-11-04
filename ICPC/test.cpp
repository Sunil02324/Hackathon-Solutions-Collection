#include <iostream>
#include <algorithm>
using namespace std;
 
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int a[n],i;
        for(i=0;i<n;i++)
            cin>>a[i];
        int a1[n] = {};
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    if(a[i]*a[j] == a[k]){
                        a1[k]=1;
                    }
                }
            }
        }
        int z = 0;
        for(z=0;z<n;z++)
            if(a1[z]==0)
                break;
        if(z!=n)
            cout<<"no"<<endl;
        else
            cout<<"yes"<<endl;
   } 
}


#include <bits/stdc++.h>
using namespace std;
int main(){
    long long int t;
    cin>>t;
    while(t--){
        long long int n,c=0;
        cin>>n;
        while(n--){
            long long int a;
            cin>>a;
            if(a!=0 && a!=1)
                c++;
       }
        if(c<2)
            cout<<"yes"<<endl;
        else
            cout<<"no"<<endl;
    }
    return 0;
}