class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;

        for(int i = 0; i < nums.size(); i ++) {
            m[target - nums[i]] = i;
        }

        int i = 0;
        for(i = 0; i < nums.size(); i ++) {
            if (m.find(nums[i]) != m.end() && m[nums[i]] != i) break;
        }

        return {i, m[nums[i]]};
    }
};