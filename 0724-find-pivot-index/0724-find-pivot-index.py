class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = sum(nums)

        # for num in nums:
        #     totalsum += num

        leftsum = 0

        for i in range(n):
            rightsum = totalsum - leftsum - nums[i]

            if leftsum == rightsum:
                return i

            leftsum += nums[i]

        return -1