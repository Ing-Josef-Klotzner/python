//Author Vitalii
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <memory.h>
#include <fstream>
using namespace std;
#define FILL(a, val) memset((a), (val), sizeof(a));
namespace SuffixArray
{
    // const int MAXSIZE = 200002;
    const int ALPHABET = 28;
    vector<int> getSuffixArray (string& s)
    {
        int n = s.size ();
        int p [n], c [n], cnt [n + ALPHABET];
        int pn [n], cn [n];
        FILL (cnt, 0);
        for (int i = 0; i < n; ++i) ++cnt [s [i]];
        for (int i = 1; i < ALPHABET; ++i) cnt [i] += cnt [i - 1];
        for (int i = 0; i < n; ++i) p [--cnt [s [i]]] = i;
        int count = 1;
        c [p [0]] = 0;  // count - 1;
        for (int i = 1; i < n; ++i)
        {
            if (s [p [i]] != s [p [i - 1]]) ++count;
            c [p [i]] = count - 1;
        }
        for (int h = 0; (1<<h) < n; ++h)
        {
            for (int i = 0; i < n; ++i)
            {
                pn [i] = p [i] - (1<<h);
                if (pn [i] < 0) pn [i] += n;
            }
            FILL(cnt, 0);
            for (int i = 0; i < n; ++i) ++cnt [c [i]];
            for (int i = 1; i < count; ++i) cnt [i] += cnt [i - 1];
            for (int i = n-1; i >= 0; --i) p [--cnt [c [pn [i]]]] = pn [i];
            count = 1;
            cn [p [0]] = 0; // count - 1;
            for (int i = 1; i < n; ++i)
            {
                int pos1 = (p [i] + (1 << h)) % n;
                int pos2 = (p [i - 1] + (1 << h)) % n;
                if (c [p [i]] != c [p [i - 1]] || c [pos1] != c [pos2])
                    ++count;
                cn [p [i]] = count - 1;
            }
            for (int i = 0; i < n; ++i) c [i] = cn [i];
        }
        vector<int> res;
        res.reserve (n);
        for (int i = 0; i < n; ++i) res.push_back (c [i]);
//        for (int i = 0; i < n; i++)
//            cout << s [res [i]];
//        cout << endl;
        return res;
    }
}
string morganAndString (string& a, string& b)
{
    a.push_back('a');
    b.push_back('b');
    string s = a+b;
    vector<int> suffixArray = SuffixArray::getSuffixArray(s);
    cout << "SuffixArray finished" << endl;
    string res = "";
    int pos1=0, pos2=0;
    while (true)
    {
        if (pos1 >= (a.size () - 1) && pos2 >= (b.size () - 1)) break;
        if (pos1 >= (a.size () - 1))
        {
            res += b[pos2++];
            continue;
        }
        if (pos2 >= (b.size()-1))
        {
            res += a[pos1++];
            continue;
        }
        if (suffixArray [pos1] < suffixArray [a.size () + pos2]) res += a [pos1++];
        else res += b [pos2++];
    }
    return res;
}

int main()
{
    ofstream fout (std::getenv ("OUTPUT_PATH"));
    int t;
    cin >> t;
    cin.ignore (numeric_limits<streamsize>::max (), '\n');
    for (int t_itr = 0; t_itr < t; t_itr++) {
        string a, b;
        cin >> a >> b;
        string result = morganAndString (a, b);
        fout << result << "\n";
    }
    fout.close ();
    return 0;
}
