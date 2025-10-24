class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int pos = -1;

        for(int i = 0; i < nums.size(); i ++) {
            if (nums[i] != val) {
                swap(nums[pos+1], nums[i]);
                pos ++;
            }
        }

        return pos+1;
    }
};