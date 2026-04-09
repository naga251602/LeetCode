class Solution {
public:
    void sortColors(vector<int>& nums) {
        if (nums.size() == 1) return;

        int l = 0, r = nums.size() - 1, i;

        for(i = 0; i <= r; i ++) {
            if (nums[i] == 0) swap(nums[i], nums[l++]);
            else if (nums[i] == 2) {
                swap(nums[i], nums[r--]);
                i --;
            }
        }
    }
};