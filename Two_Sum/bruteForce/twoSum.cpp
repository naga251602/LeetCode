class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int pos_1, pos_2;

        // time complexity O (n ** 2)
        for(int i = 0; i < nums.size(); i ++) {
            for(int j = i + 1; j < nums.size(); j ++) {
                if (nums[i] + nums[j] == target) {
                    pos_1 = i;
                    pos_2 = j;
                    break;
                }
            }
        }
        return {pos_1, pos_2};
    }
};