class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        solutions = []
        prev = None
        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            else:
                prev = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    solutions.append([nums[l], nums[r], nums[i]])
                    prev_l = nums[l]
                    while prev_l == nums[l] and l < r:
                        l += 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
        
        return solutions





