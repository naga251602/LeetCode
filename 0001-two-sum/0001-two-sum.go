func twoSum(nums []int, target int) []int {
    hm := make(map[int]int)

    for i := range len(nums) {
        if _, valid := hm[nums[i]]; valid {
            return []int{hm[nums[i]], i};
        }
        hm[target - nums[i]] = i;
    }
    
    return []int{-1, -1};
}