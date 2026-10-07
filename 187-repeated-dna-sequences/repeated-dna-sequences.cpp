class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> um;
        vector<string> res;
        int l = 0;
        
        for (int r = 0; r < s.size(); r ++) {
            if (r - l + 1 == 10) {
                um[s.substr(l, 10)] ++;
                l ++;
            }

        }

        for (auto &item: um) {
            if (item.second > 1) res.push_back(item.first);
        }

        return res;
    }
};