#include <iostream>
#include <vector>

typedef long long ll;
using namespace std;

ll beautifulQuadruples(int a, int b, int c, int d) {
    ll ans = 0;
    vector<int> tmp(4);
    tmp[0] = a, tmp[1] = b, tmp[2] = c; tmp[3] = d;
    sort(tmp.begin(), tmp.end());
    a = tmp[0], b = tmp[1], c = tmp[2], d = tmp[3];
    for (int i = 1; i <= a; ++i)
        for (int j = i; j <= b; ++j)
            for (int k = j; k <= c; ++k)
                for (int l = k; l <= d; ++l)
                    if (i ^ j ^ k ^ l) ++ans;
    return ans;
}

int main() {
    cout << beautifulQuadruples(1150, 1547, 853, 423);
    return 0;
}


