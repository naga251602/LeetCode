class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int i = 0; 

        while (i < nums.size()) {
            if (nums[i] > 0){
                int pos = nums[i] - 1;
                if (pos <= nums.size() - 1 && nums[pos] != nums[i]) swap(nums[pos], nums[i]);
                else i ++;
            } else i ++;
            
        }

        for(i = 0; i < nums.size(); i++) {
            if (nums[i] != i+1) break;
        }

        return i + 1;
    }
};