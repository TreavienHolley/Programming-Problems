class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            seen = {}

            for i in range(len(nums)):
                #value in seen?
                if nums[i] in seen:
                    return [seen[nums[i]],i]
                #if not add in seen
                else:
                    seen[target - nums[i]] = i

            # can add `retun None` incase there are nothing but we assume there always is