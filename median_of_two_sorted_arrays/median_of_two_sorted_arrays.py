class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i, j, pos, s, flag = 0, 0, 0, 0, -1
    

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                if (len(nums1) + len(nums2)) % 2 == 0 and pos == (len(nums1) + len(nums2)) // 2 - 1:
                    s += nums1[i]
                elif pos == (len(nums1) + len(nums2)) // 2:
                    s += nums1[i]
                    flag = 1
                    break
                i += 1
            else:
                if (len(nums1) + len(nums2)) % 2 == 0 and pos == (len(nums1) + len(nums2)) // 2 - 1:
                    s += nums2[j]
                elif pos == (len(nums1) + len(nums2)) // 2:
                    s += nums2[j]
                    flag = 1
                    break
                j += 1
            pos += 1
            print(s)
        
        while i < len(nums1) and flag == -1:
            if (len(nums1) + len(nums2)) % 2 == 0 and pos == (len(nums1) + len(nums2)) // 2 - 1:
                s += nums1[i]
            elif pos == (len(nums1) + len(nums2)) // 2:
                s += nums1[i]
                break
            i += 1
            pos += 1

        while j < len(nums2) and flag == -1:
            if (len(nums1) + len(nums2)) % 2 == 0 and pos == (len(nums1) + len(nums2)) // 2 - 1:
                s += nums2[j]
            elif pos == (len(nums1) + len(nums2)) // 2:
                s += nums2[j]
                break
            j += 1
            pos += 1
        
        return s / 2 if (len(nums1) + len(nums2)) % 2 == 0 else float(s)

        