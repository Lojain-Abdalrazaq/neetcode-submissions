class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # in this question, we have to use the hashmap to store the key-value pairs
        # key is the number in the list, value is the frequency
        # this solution satisfies the O(n) space complexity
        # but the built in sorting can cause O(m log m) time complexity with O(nlog n) in the worst case
        # so, I needed to find a sorting algorithim that has O(n) as time complexity as average
        # one possible sort to use is: BUCKET SORT
        nums_map = {}
        for i in range(len(nums)):
            if nums[i] in nums_map:
                nums_map[nums[i]] +=1
            else:
                nums_map[nums[i]] = 1

        # now, we have the nums_map.items() -> [(3,2), (2,2), (1,1)] ready to be sorted
        
        # sort the map according to the values
        # return first k elements
        # NOTE!!!: THE QUESTION DONT CARE ABOUT THE ORDER OF THE RETURNED ELEMENTS
        # SO , WE CAN USE THE BUCKET SORT, AND IF THERE IS MORE THAN ONE LEMEENT WITH THE SAME COUNT, 
        # LIKE: [2,2,1,1,4,5]
        # freq = [[],[],[],[],[],[]] -> after filling -> freq = [[],[5,4],[2,1],[],[],[]]
        # k = 2 -> output [1,2] or [2,1] all correct and the test cases always has the same results
        freq =[]
        # هون اما بعملها +1 او بتعامل معها زي اكنه الكاونت ناقص 1
        for i in range(len(nums)+1):
            freq.append([])

        # filling the bucket sort array
        for num, count in nums_map.items():
            freq[count].append(num)
        
        result = []
        for count in range(len(freq)-1,0, -1):
            for nums in freq[count]:
                result.append(nums)
                # early stop, very good step, no need to fill all th result array and then return the k elements...
                if len(result) == k:
                    return result