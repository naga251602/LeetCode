class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() <= 1) return s.length();

        unordered_set<char> st;
        int l = 0, i;
        int max_len = 1;

        for(i = 0; i < s.length(); i ++) {
            if (i == l || st.find(s[i]) == st.end()) st.insert(s[i]);
            else {
                max_len = max(max_len, i - l);
                st.erase(s[l]);
                l ++;
                i --;
            }
        }

        
        return max(max_len, i - l);
    }
};