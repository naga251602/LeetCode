class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> um;
        vector<string> res;
        int l = 0;
        
        for (int r = 0; r < s.size(); r ++) {
            if (r - l + 1 == 10) {
                string key = s.substr(l, 10);
                um[key] ++;

                if (um[key] == 2) res.push_back(key);
                l ++;
            }

        }

        return res;
    }
};