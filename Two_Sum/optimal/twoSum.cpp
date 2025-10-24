class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;

        int pos_1, pos_2;

        for(int i = 0; i< nums.size() ; i ++) {
            m[target - nums[i]] = i;
        }

        for(int i = 0; i < nums.size(); i ++) {
            if (m[nums[i]] != 0 && m[nums[i]] != i) {
                pos_1 = m[nums[i]];
                pos_2 = i;
            }
        }

        return {pos_1, pos_2};
    }
};