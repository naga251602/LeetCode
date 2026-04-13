class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        int i;

        for(i = 0; i < nums.size(); i ++) {
            int k = target - nums[i];
            if (m.find(nums[i]) != m.end()) return {m[nums[i]], i};
            else m.insert({k, i});
        }

        return {};
    }
};