#include<bits/stdc++.h>
using namespace std;

int main(){
map<int, pair<string,int>> m;
int avl,total=0,amount,priority,price;
cin>>amount; // give total available amount
cin>>avl; // give number of dals available in dukan
vector<string> s(avl);
for(int i=0;i<avl;i++){
    cin>>s[i];
}

string dal;
while(cin){
    cin>>priority>>dal>>price;
     m[priority]=make_pair(dal,price);
     } 
for(auto it=m.begin();it!=m.end();it++)
{
    
    auto x=find(s.begin(),s.end(),(*it).second.first); //find the dal available in dukan based on the priority
    if(x!=s.end() && (*it).second.second<amount) {
    amount=200;
    total+=(*it).second.second;
    (*it).second.first="------";
amount-=total;
        
    }
}
cout<<"Total amount used for dals :"<<total<<endl;
cout<<"The updated list is :"<<endl;
for(auto it:m){
    cout<<(it).second.first<<" "<<(it).second.second<<endl;
}

    
}
