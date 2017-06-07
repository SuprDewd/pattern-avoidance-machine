#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = 2147483647;

%(contains)s

int main() {
    cin.sync_with_stdio(false);

    int n;
    cin >> n;

    int *perm = new int[n];
    rep(i,0,n) {
        perm[i] = i+1;
    }

    do {
        if (!contains(n, perm)) {
            rep(i,0,n) {
                if (i != 0) cout << " ";
                cout << perm[i];
            }
            cout << endl;
        }
    } while (next_permutation(perm, perm + n));

    return 0;
}

