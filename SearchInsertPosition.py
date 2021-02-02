# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# Used Interpolation Search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = (len(nums) - 1)
        while low <= high and target >= nums[low] and target <= nums[high]:
            if high != 0:
                index = low + \
                    int(((float(high - low) /
                          (nums[high] - nums[low])) * (target-nums[low])))
                if nums[index] == target:
                    return index
                if nums[index] < target:
                    low = index + 1
                else:
                    high = index - 1
            else:
                break
        nums.append(target)
        nums.sort()
        return nums.index(target)
