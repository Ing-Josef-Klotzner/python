#include <bits/stdc++.h>
using namespace std;
const int N=5500;
const long long P=1000000007;

vector <int> pr,pr2;

vector <int> v[N+1];
int f[N+1],F,FR[N+1];
int n,r;
int fa,fad;

void input(){
    scanf("%d%d",&n,&r);
    for (int i=1;i<n;i++){
        int x,y;
        scanf("%d%d",&x,&y);
        v[x].push_back(y);
        v[y].push_back(x);
    }
}

void go(int x,int fr,int deep){
    f[x]=F;
    if (deep==r) return;
    for (int i=0;i<v[x].size();i++)
    if (v[x][i]!=fr)
        go(v[x][i],x,deep+1);
}

void dfs(int x,int fr,int dis){
    FR[x]=fr;
    if (dis>fad) fad=dis,fa=x;
    for (int i=0;i<v[x].size();i++)
    if (v[x][i]!=fr && f[v[x][i]]==F)
        dfs(v[x][i],x,dis+1);
}

long long geth(int x,int fr,int deep){
    vector <long long > h;
    for (int i=0;i<v[x].size();i++)
    if (v[x][i]!=fr && f[v[x][i]]==F)
        h.push_back(geth(v[x][i],x,deep+1));
    sort(h.begin(),h.end());
    long long hr=pr[deep];
    for (int i=0;i<h.size();i++)
    hr = (hr * pr2[deep] + h[i])%P;
    return hr;
}


long long get(int I){
    F++;
    go(I,I,0);

    fa=fad=0;
    dfs(I,I,0);

    fad=0;
    dfs(fa,fa,0);
    int din=fad;

    long long hasR=1;
    while (din>=0){
        if ((fad%2==0 && din==fad/2) || (fad%2==1 && (din==fad/2 || din==(fad+1)/2)))
            hasR*=geth(fa,fa,0);
        fa=FR[fa];
        din--;
    }
    return hasR;
}

bool ispr(int x){
    for (int i=2;i*i<=x;i++)
    if (x%i==0) return 0;
    return 1;
}

void sol(){

    int x=400;
    while (pr.size()<=n){
        while (!ispr(x)) x++;
        pr.push_back(x++);
        while (!ispr(x)) x++;
        pr2.push_back(x++);
    }

    set <long long> S;
    for (int i=1;i<=n;i++)
        S.insert(get(i));
    printf("%d\n",int(S.size()));
}

int main() {
    input();
    sol();
    return 0;
}
