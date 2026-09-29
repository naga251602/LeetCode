class Solution {
public:
    int countSpecialIntegers(vector<int>& nums) {
        int count = 0;
        unordered_map<int, vector<int>> um;

        for (size_t i = 0; i < nums.size(); ++ i) {
            um[nums[i]].push_back(i);
        }

        for(auto item: um) {
            if (item.second.size() > 2) {
                int diff = -1;
                size_t i = 1;

                for (; i < item.second.size(); ++ i) {
                    if (diff != -1 && diff == item.second[i] - item.second[i-1]) continue;
                    else if (diff != -1) break;
                    diff = item.second[i] - item.second[i-1];
                }

                if (i == item.second.size()) count ++;
            }
        }

        return count;
    }
};