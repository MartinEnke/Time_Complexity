''''''
'''
Basic Approach
Step 1: Understand the Problem
Before jumping into coding, let’s take a moment to understand the problem:
What are you trying to find? Two numbers in the array that add up to the target.
What should the output be? The indices of these two numbers.
What are the constraints? Each input has one solution, and you cannot use the same element twice.
Questions to Consider:
How would you manually solve this problem with a small set of numbers?
What does it mean to "find two numbers"? What information do you need to keep track of as you search?
Step 2: Try a Simple Example
Start with a simple example to get a feel for the problem:
If nums = [1, 2, 3] and target = 4, how would you find the pair?
What if the list is [1, 3, 5] and the target is 8?
Exercise: Write down the steps you would take to find the pair manually. 
What do you check first? What do you do next?'''


nums = [1, 4, 6, 3, 2, 6]
target = 6

two_nums = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            two_nums = [i, j]
            break  # optional: stop at first pair
    if two_nums:
        break

print(two_nums)  # Output: [0, 2] → 1 + 3 = 4
'''
The naive solution uses two nested loops to check all possible pairs of numbers. 
The outer loop starts from the first element, and the inner loop starts from the 
next element to avoid using the same element twice. 
When a pair is found that adds up to the target, their indices are returned. 
The function returns an empty list if no solution is found.


Naive solution efficiency

What is the time complexity of the naive solution to the two sum problem, 
which uses nested loops to check every pair of numbers?


O(n)
O(n^2)
O(log n)
O(n log n)

The correct answer is O(n^2). 
In the naive solution, we use two nested loops to compare each number with 
every other number in the array. This results in checking n * (n-1) / 2 pairs, 
which simplifies to O(n^2) in Big O notation. This quadratic time complexity means 
the algorithm becomes significantly slower as the input size increases.


Efficient Approach

Step 4: Reflect on Efficiency
After considering the basic approach, let’s reflect:
What did you notice? Is there a way to avoid checking some pairs?
Challenge: 
Can you think of a way to track which numbers you’ve already seen as you go through the list?
Hints:
Think about how you can keep track of numbers you’ve already encountered.
How can you quickly check if the number needed to reach the target 
(let’s call it the “complement”) has been seen before?
Exercise: 
Without coding, write down a strategy or plan that could potentially reduce 
the number of checks you need to make. What data structure might help?

Step 5: Consider Alternative Approaches
Let’s think about different ways to approach the problem:
Brainstorm: Can you use any data structures that would help you remember numbers 
and check for complements efficiently?

Exercise: Sketch out an approach that might allow you to solve the problem in fewer steps.
Questions to Guide You:
How would your approach change if you could instantly know whether the complement to a number exists in the array?
What data structure could provide that information quickly?
Hints
Hint 1: Consider using a dictionary (hashmap) to store numbers and their indices 
as you iterate through the array.
Hint 2: For each number, calculate the complement (target - current number) 
and check if it's already in the dictionary.

Step 6: Try Coding Your Approach
Now that you’ve thought about different strategies, try to code your chosen approach:
Start Simple: Implement the basic, straightforward approach first.
Experiment: After that, try your optimized idea. How does it compare?
'''


def twoSum(nums, target):
    nums_dict = {}  # define inside the function for safety

    for i in range(len(nums)):
        nums_dict[nums[i]] = i

    two_nums = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict and nums_dict[complement] != i:
            two_nums = [i, nums_dict[complement]]
            break

    return two_nums

print(twoSum([1, 4, 6, 3, 2, 6], 6))

'''
Success: True
Performance ratio: 32.72x optimal
Feedback: Solution is correct but not optimal. It runs 32.7x slower than an optimal solution. 
Consider using a hash table for O(n) complexity.
'''


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}  # num → index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []

print(twoSum([1, 4, 6, 3, 2, 6], 6))

'''
Excellent! Solution is correct and efficient.
'''

'''
Conclusion

The idea is to keep track of which numbers you have seen so far. 
You store them in a Python dictionary, using the number as key, and its index as value.
When you loop through the numbers in nums, you can calculate which other number 
you need to complete the sum: complement = target - sum. complement is the number 
you’re looking for in the dictionary of saved numbers.
If the number is there, you can efficiently return the index, 
since you used the number as key and its index as value. If the number is not yet there, 
you add it to the dictionary of numbers seen so far.
Two Sum Time Complexity

What is the time complexity of the optimal solution to the Two Sum problem 
as presented in the code?


O(log n)
O(n)
O(1)
O(n^2)

The correct answer is O(n). 
The solution uses a single pass through the input array (n iterations), 
and each operation within the loop (dictionary lookup, insertion) is O(1) on average. 
This results in a linear time complexity of O(n).

Check It!
Conclusion
That was not easy – whether you found the solution or not, well done! 💯
By following these steps, you’ve explored the “Two Sum” problem from multiple angles. 
The key takeaway is that taking the time to think critically about different approaches 
can lead to more efficient solutions. Keep practicing, and soon you’ll be able to apply 
these strategies to other problems as well!
'''