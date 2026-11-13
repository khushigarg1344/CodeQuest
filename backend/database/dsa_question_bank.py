import json

DSA_PROBLEMS = [

    # 1. Second Largest Element
    {
        "title": "Second Largest Element",
        "description": "Given an array of integers, find and print the second largest distinct element. You may assume at least two distinct elements exist.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "6\n10 5 20 8 20 15",
        "sample_output": "15",
        "test_cases_json": json.dumps([
            {"input": "6\n10 5 20 8 20 15", "output": "15"},
            {"input": "5\n1 2 3 4 5", "output": "4"},
            {"input": "4\n-5 -2 -9 -1", "output": "-2"}
        ])
    },

    # 2. Sum of Array Elements
    {
        "title": "Sum of Array Elements",
        "description": "Given an array of N integers, calculate and print the sum of all its elements.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "15",
        "test_cases_json": json.dumps([
            {"input": "5\n1 2 3 4 5", "output": "15"},
            {"input": "4\n-1 -2 -3 -4", "output": "-10"},
            {"input": "3\n10 0 20", "output": "30"}
        ])
    },

    # 3. Count Even and Odd Elements
    {
        "title": "Count Even and Odd Elements",
        "description": "Given an array of N integers, count how many elements are even and how many are odd. Print the even count followed by the odd count.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "6\n1 2 3 4 5 6",
        "sample_output": "3 3",
        "test_cases_json": json.dumps([
            {"input": "6\n1 2 3 4 5 6", "output": "3 3"},
            {"input": "4\n2 4 6 8", "output": "4 0"},
            {"input": "3\n1 3 5", "output": "0 3"}
        ])
    },

    # 4. Find Minimum Element
    {
        "title": "Find Minimum Element",
        "description": "Given an array of N integers, find and print the smallest element.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "5\n8 3 9 1 6",
        "sample_output": "1",
        "test_cases_json": json.dumps([
            {"input": "5\n8 3 9 1 6", "output": "1"},
            {"input": "4\n-5 -2 -9 -1", "output": "-9"},
            {"input": "3\n7 7 7", "output": "7"}
        ])
    },

    # 5. Linear Search
    {
        "title": "Linear Search",
        "description": "Given an array of N integers and a target value X, print the index of the first occurrence of X. Print -1 if X is not present. Use zero-based indexing.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "5 3\n10 20 30 40 50",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "5 3\n10 20 30 40 50", "output": "2"},
            {"input": "4 8\n1 2 3 4", "output": "-1"},
            {"input": "5 2\n7 8 7 9 7", "output": "0"}
        ])
    },

    # 6. Count Occurrences
    {
        "title": "Count Occurrences in Array",
        "description": "Given an array of N integers and a target X, count and print the number of times X appears in the array.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "6 2\n1 2 2 3 2 4",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "6 2\n1 2 2 3 2 4", "output": "3"},
            {"input": "4 5\n1 2 3 4", "output": "0"},
            {"input": "3 7\n7 7 7", "output": "3"}
        ])
    },

    # 7. Left Rotate Array by One
    {
        "title": "Left Rotate Array by One",
        "description": "Given an array of N integers, rotate it to the left by one position. The first element moves to the last position. Print the resulting array.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "2 3 4 5 1",
        "test_cases_json": json.dumps([
            {"input": "5\n1 2 3 4 5", "output": "2 3 4 5 1"},
            {"input": "3\n10 20 30", "output": "20 30 10"},
            {"input": "1\n99", "output": "99"}
        ])
    },

    # 8. Right Rotate Array by One
    {
        "title": "Right Rotate Array by One",
        "description": "Given an array of N integers, rotate it to the right by one position. The last element moves to the first position. Print the resulting array.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "5 1 2 3 4",
        "test_cases_json": json.dumps([
            {"input": "5\n1 2 3 4 5", "output": "5 1 2 3 4"},
            {"input": "3\n10 20 30", "output": "30 10 20"},
            {"input": "1\n99", "output": "99"}
        ])
    },

    # 9. Move Zeros to End
    {
        "title": "Move Zeros to End",
        "description": "Given an array of N integers, move all zeros to the end while maintaining the relative order of non-zero elements. Print the resulting array.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "6\n0 1 0 3 12 0",
        "sample_output": "1 3 12 0 0 0",
        "test_cases_json": json.dumps([
            {"input": "6\n0 1 0 3 12 0", "output": "1 3 12 0 0 0"},
            {"input": "5\n1 2 3 4 5", "output": "1 2 3 4 5"},
            {"input": "4\n0 0 0 0", "output": "0 0 0 0"}
        ])
    },

    # 10. Remove Duplicates from Sorted Array
    {
        "title": "Remove Duplicates from Sorted Array",
        "description": "Given a sorted array of N integers, remove duplicate values and print the unique elements in their original sorted order.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "7\n1 1 2 2 3 4 4",
        "sample_output": "1 2 3 4",
        "test_cases_json": json.dumps([
            {"input": "7\n1 1 2 2 3 4 4", "output": "1 2 3 4"},
            {"input": "5\n1 1 1 1 1", "output": "1"},
            {"input": "4\n1 2 3 4", "output": "1 2 3 4"}
        ])
    }
    
    ,

    # 11. Maximum Difference
    {
        "title": "Maximum Difference in Array",
        "description": "Given an array of N integers, find the maximum value of arr[j] - arr[i] such that j > i. Print the maximum difference. If no positive difference exists, print 0.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "6\n7 1 5 3 6 4",
        "sample_output": "5",
        "test_cases_json": json.dumps([
            {"input": "6\n7 1 5 3 6 4", "output": "5"},
            {"input": "5\n9 7 5 3 1", "output": "0"},
            {"input": "4\n1 2 3 4", "output": "3"}
        ])
    },

    # 12. Find Missing Number
    {
        "title": "Find Missing Number",
        "description": "An array contains N-1 distinct integers from 1 to N. Find and print the missing number.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "5\n1 2 4 5",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "5\n1 2 4 5", "output": "3"},
            {"input": "4\n1 2 3", "output": "4"},
            {"input": "6\n2 3 4 5 6", "output": "1"}
        ])
    },

    # 13. Check if Array is Sorted
    {
        "title": "Check if Array is Sorted",
        "description": "Given an array of N integers, check whether it is sorted in non-decreasing order. Print YES if sorted, otherwise print NO.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "5\n1 2 2 4 5",
        "sample_output": "YES",
        "test_cases_json": json.dumps([
            {"input": "5\n1 2 2 4 5", "output": "YES"},
            {"input": "4\n1 3 2 4", "output": "NO"},
            {"input": "3\n7 7 7", "output": "YES"}
        ])
    },

    # 14. Leaders in an Array
    {
        "title": "Leaders in an Array",
        "description": "An element is a leader if it is greater than or equal to every element to its right. The last element is always a leader. Print all leaders from left to right, separated by spaces.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "6\n16 17 4 3 5 2",
        "sample_output": "17 5 2",
        "test_cases_json": json.dumps([
            {"input": "6\n16 17 4 3 5 2", "output": "17 5 2"},
            {"input": "5\n1 2 3 4 5", "output": "5"},
            {"input": "4\n5 4 3 2", "output": "5 4 3 2"}
        ])
    },

    # 15. Equilibrium Index
    {
        "title": "Equilibrium Index",
        "description": "Find the first zero-based index where the sum of elements strictly to the left equals the sum of elements strictly to the right. Print -1 if no such index exists.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5\n1 3 5 2 2",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "5\n1 3 5 2 2", "output": "2"},
            {"input": "3\n1 2 3", "output": "-1"},
            {"input": "1\n10", "output": "0"}
        ])
    },

    # 16. Maximum Subarray Sum
    {
        "title": "Maximum Subarray Sum",
        "description": "Given an array of N integers, find the maximum sum of any non-empty contiguous subarray.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "9\n-2 1 -3 4 -1 2 1 -5 4",
        "sample_output": "6",
        "test_cases_json": json.dumps([
            {"input": "9\n-2 1 -3 4 -1 2 1 -5 4", "output": "6"},
            {"input": "5\n-5 -2 -8 -1 -3", "output": "-1"},
            {"input": "4\n1 2 3 4", "output": "10"}
        ])
    },

    # 17. Two Sum - Sorted Array
    {
        "title": "Two Sum in Sorted Array",
        "description": "Given a sorted array of N integers and a target X, find two distinct elements whose sum equals X. Print their zero-based indices in increasing order. If no pair exists, print -1 -1. Exactly one valid pair exists when a solution is present.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5 9\n1 2 3 7 11",
        "sample_output": "1 3",
        "test_cases_json": json.dumps([
            {"input": "5 9\n1 2 3 7 11", "output": "1 3"},
            {"input": "4 10\n1 2 3 4", "output": "-1 -1"},
            {"input": "3 6\n1 2 4", "output": "1 2"}
        ])
    },

    # 18. Rotate Array by K
    {
        "title": "Rotate Array by K Positions",
        "description": "Given an array of N integers and an integer K, rotate the array to the right by K positions. Print the resulting array. K may be greater than N.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5 2\n1 2 3 4 5",
        "sample_output": "4 5 1 2 3",
        "test_cases_json": json.dumps([
            {"input": "5 2\n1 2 3 4 5", "output": "4 5 1 2 3"},
            {"input": "4 6\n1 2 3 4", "output": "3 4 1 2"},
            {"input": "3 0\n7 8 9", "output": "7 8 9"}
        ])
    },

    # 19. Majority Element
    {
        "title": "Majority Element",
        "description": "Given an array of N integers, find the element that appears more than floor(N/2) times. A majority element is guaranteed to exist.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "7\n2 2 1 1 1 2 2",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "7\n2 2 1 1 1 2 2", "output": "2"},
            {"input": "5\n3 3 3 2 1", "output": "3"},
            {"input": "1\n9", "output": "9"}
        ])
    },

    # 20. Rearrange Positive and Negative
    {
        "title": "Rearrange Positive and Negative Numbers",
        "description": "Given an array containing positive, negative and zero values, rearrange it so that all negative values appear first, followed by all non-negative values. Preserve the original relative order within each group. Print the resulting array.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "6\n1 -2 3 -4 0 5",
        "sample_output": "-2 -4 1 3 0 5",
        "test_cases_json": json.dumps([
            {"input": "6\n1 -2 3 -4 0 5", "output": "-2 -4 1 3 0 5"},
            {"input": "4\n-1 -2 3 4", "output": "-1 -2 3 4"},
            {"input": "3\n1 2 3", "output": "1 2 3"}
        ])
    }
    
    ,

    # 21. Prefix Sum Queries
    {
        "title": "Prefix Sum Range Queries",
        "description": "Given an array of N integers and Q queries, each containing L and R (zero-based, inclusive), print the sum of elements from index L to R for every query.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5 3\n1 2 3 4 5\n0 2\n1 3\n2 4",
        "sample_output": "6\n9\n12",
        "test_cases_json": json.dumps([
            {"input": "5 3\n1 2 3 4 5\n0 2\n1 3\n2 4", "output": "6\n9\n12"},
            {"input": "4 2\n-1 2 -3 4\n0 3\n1 2", "output": "2\n-1"},
            {"input": "3 1\n5 5 5\n1 1", "output": "5"}
        ])
    },

    # 22. Product of Array Except Self
    {
        "title": "Product of Array Except Self",
        "description": "Given an array of N integers, print an array where each element is the product of all original elements except the element at the same index. Do not use division.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "4\n1 2 3 4",
        "sample_output": "24 12 8 6",
        "test_cases_json": json.dumps([
            {"input": "4\n1 2 3 4", "output": "24 12 8 6"},
            {"input": "3\n2 3 4", "output": "12 8 6"},
            {"input": "4\n1 0 3 4", "output": "0 12 0 0"}
        ])
    },

    # 23. Subarray with Given Sum
    {
        "title": "Subarray with Given Sum",
        "description": "Given an array of N non-negative integers and a target S, find a non-empty contiguous subarray whose sum equals S. Print its one-based starting and ending indices. If no such subarray exists, print -1.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5 12\n1 2 3 7 5",
        "sample_output": "2 4",
        "test_cases_json": json.dumps([
            {"input": "5 12\n1 2 3 7 5", "output": "2 4"},
            {"input": "4 5\n1 2 3 4", "output": "2 3"},
            {"input": "3 20\n1 2 3", "output": "-1"}
        ])
    },

    # 24. Longest Subarray with Sum K
    {
        "title": "Longest Subarray with Sum K",
        "description": "Given an array of N integers and an integer K, find the length of the longest non-empty contiguous subarray whose sum equals K. Print 0 if no such subarray exists.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "6 5\n1 2 3 1 1 1",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "6 5\n1 2 3 1 1 1", "output": "3"},
            {"input": "5 0\n1 -1 2 -2 3", "output": "4"},
            {"input": "3 10\n1 2 3", "output": "0"}
        ])
    },

    # 25. Maximum Consecutive Ones
    {
        "title": "Maximum Consecutive Ones",
        "description": "Given an array containing only 0s and 1s, find and print the maximum number of consecutive 1s.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "8\n1 1 0 1 1 1 0 1",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "8\n1 1 0 1 1 1 0 1", "output": "3"},
            {"input": "5\n0 0 0 0 0", "output": "0"},
            {"input": "4\n1 1 1 1", "output": "4"}
        ])
    },

    # 26. Merge Two Sorted Arrays
    {
        "title": "Merge Two Sorted Arrays",
        "description": "Given two sorted arrays of sizes N and M, merge them into one sorted array and print the result.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "4 3\n1 3 5 7\n2 4 6",
        "sample_output": "1 2 3 4 5 6 7",
        "test_cases_json": json.dumps([
            {"input": "4 3\n1 3 5 7\n2 4 6", "output": "1 2 3 4 5 6 7"},
            {"input": "3 2\n1 2 3\n4 5", "output": "1 2 3 4 5"},
            {"input": "2 3\n5 8\n1 3 9", "output": "1 3 5 8 9"}
        ])
    },

    # 27. Sort Array of 0s, 1s and 2s
    {
        "title": "Sort Array of 0s 1s and 2s",
        "description": "Given an array containing only 0, 1 and 2, sort it in non-decreasing order and print the result.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "6\n0 2 1 2 0 1",
        "sample_output": "0 0 1 1 2 2",
        "test_cases_json": json.dumps([
            {"input": "6\n0 2 1 2 0 1", "output": "0 0 1 1 2 2"},
            {"input": "4\n2 2 2 2", "output": "2 2 2 2"},
            {"input": "5\n0 1 2 0 1", "output": "0 0 1 1 2"}
        ])
    },

    # 28. Container With Most Water
    {
        "title": "Container With Most Water",
        "description": "Given N non-negative integers representing vertical line heights at consecutive positions, find the maximum water area formed by choosing two lines and the x-axis. The area is the distance between the lines multiplied by the smaller height.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "9\n1 8 6 2 5 4 8 3 7",
        "sample_output": "49",
        "test_cases_json": json.dumps([
            {"input": "9\n1 8 6 2 5 4 8 3 7", "output": "49"},
            {"input": "4\n1 1 1 1", "output": "3"},
            {"input": "2\n5 10", "output": "5"}
        ])
    },

    # 29. Trapping Rain Water
    {
        "title": "Trapping Rain Water",
        "description": "Given N non-negative integers representing elevation heights, calculate the total amount of rainwater that can be trapped between the bars and print it.",
        "difficulty": "Hard",
        "topic": "Arrays",
        "xp_reward": 150,
        "sample_input": "6\n3 0 0 2 0 4",
        "sample_output": "10",
        "test_cases_json": json.dumps([
            {"input": "6\n3 0 0 2 0 4", "output": "10"},
            {"input": "6\n0 1 0 2 1 0", "output": "1"},
            {"input": "5\n1 2 3 4 5", "output": "0"}
        ])
    },

    # 30. Maximum Product Subarray
    {
        "title": "Maximum Product Subarray",
        "description": "Given an array of N integers, find the maximum product of any non-empty contiguous subarray and print it.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5\n2 3 -2 4 -1",
        "sample_output": "48",
        "test_cases_json": json.dumps([
            {"input": "5\n2 3 -2 4 -1", "output": "48"},
            {"input": "4\n-2 0 -1 -3", "output": "3"},
            {"input": "3\n-2 -3 -4", "output": "12"}
        ])
    }
    
    ,

    # 31. Best Time to Buy and Sell Stock
    {
        "title": "Best Time to Buy and Sell Stock",
        "description": "Given an array where each element represents a stock price on a day, find the maximum profit from one buy followed by one sell. If no profit is possible, print 0.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "6\n7 1 5 3 6 4",
        "sample_output": "5",
        "test_cases_json": json.dumps([
            {"input": "6\n7 1 5 3 6 4", "output": "5"},
            {"input": "5\n7 6 4 3 1", "output": "0"},
            {"input": "5\n1 2 3 4 5", "output": "4"}
        ])
    },

    # 32. Find Peak Element
    {
        "title": "Find Peak Element",
        "description": "Given an array of N integers, find an index of a peak element. A peak element is strictly greater than its existing neighbors. Treat missing boundary neighbors as negative infinity. Print any valid zero-based peak index. The array is guaranteed to contain a peak.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5\n1 3 20 4 1",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "5\n1 3 20 4 1", "output": "2"},
            {"input": "3\n1 2 3", "output": "2"},
            {"input": "4\n4 3 2 1", "output": "0"}
        ])
    },

    # 33. Search in Rotated Sorted Array
    {
        "title": "Search in Rotated Sorted Array",
        "description": "A sorted array of distinct integers has been rotated at an unknown pivot. Given the array and target X, print the zero-based index of X, or -1 if it is absent.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "7 0\n4 5 6 7 0 1 2",
        "sample_output": "4",
        "test_cases_json": json.dumps([
            {"input": "7 0\n4 5 6 7 0 1 2", "output": "4"},
            {"input": "5 3\n5 1 2 3 4", "output": "3"},
            {"input": "4 8\n1 2 3 4", "output": "-1"}
        ])
    },

    # 34. Find First and Last Position
    {
        "title": "Find First and Last Position",
        "description": "Given a sorted array of N integers and a target X, print the first and last zero-based positions of X. Print -1 -1 if X does not exist.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "8 8\n5 7 7 8 8 10 10 12",
        "sample_output": "3 4",
        "test_cases_json": json.dumps([
            {"input": "8 8\n5 7 7 8 8 10 10 12", "output": "3 4"},
            {"input": "5 3\n1 2 4 5 6", "output": "-1 -1"},
            {"input": "4 2\n2 2 2 2", "output": "0 3"}
        ])
    },

    # 35. Search Insert Position
    {
        "title": "Search Insert Position",
        "description": "Given a sorted array of distinct integers and a target X, print the index where X is found. If it is absent, print the index where it should be inserted to maintain sorted order.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "4 5\n1 3 5 6",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "4 5\n1 3 5 6", "output": "2"},
            {"input": "4 2\n1 3 5 6", "output": "1"},
            {"input": "3 7\n1 3 5", "output": "3"}
        ])
    },

    # 36. Minimum in Rotated Sorted Array
    {
        "title": "Minimum in Rotated Sorted Array",
        "description": "A strictly increasing sorted array has been rotated at an unknown pivot. Find and print its minimum element. The array contains distinct values.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5\n3 4 5 1 2",
        "sample_output": "1",
        "test_cases_json": json.dumps([
            {"input": "5\n3 4 5 1 2", "output": "1"},
            {"input": "4\n4 5 6 7", "output": "4"},
            {"input": "3\n2 1 3", "output": "1"}
        ])
    },

    # 37. Kth Largest Element
    {
        "title": "Kth Largest Element",
        "description": "Given an array of N integers and an integer K, find and print the Kth largest element in sorted order, counting duplicates.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "6 2\n3 2 1 5 6 4",
        "sample_output": "5",
        "test_cases_json": json.dumps([
            {"input": "6 2\n3 2 1 5 6 4", "output": "5"},
            {"input": "5 1\n7 4 6 3 9", "output": "9"},
            {"input": "5 3\n1 1 2 2 3", "output": "2"}
        ])
    },

    # 38. Count Subarrays with Sum K
    {
        "title": "Count Subarrays with Sum K",
        "description": "Given an array of N integers and an integer K, count the number of non-empty contiguous subarrays whose sum equals K.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5 3\n1 2 3 -2 2",
        "sample_output": "4",
        "test_cases_json": json.dumps([
            {"input": "5 3\n1 2 3 -2 2", "output": "4"},
            {"input": "3 0\n1 -1 0", "output": "3"},
            {"input": "4 5\n1 2 3 4", "output": "0"}
        ])
    },

    # 39. Longest Consecutive Sequence
    {
        "title": "Longest Consecutive Sequence",
        "description": "Given an unsorted array of N integers, find and print the length of the longest sequence of consecutive integer values. The sequence elements need not be adjacent in the array.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "6\n100 4 200 1 3 2",
        "sample_output": "4",
        "test_cases_json": json.dumps([
            {"input": "6\n100 4 200 1 3 2", "output": "4"},
            {"input": "5\n1 2 0 1 3", "output": "4"},
            {"input": "4\n10 30 20 40", "output": "1"}
        ])
    },

    # 40. Three Sum
    {
        "title": "Three Sum",
        "description": "Given an array of N integers, determine whether there are three distinct elements whose sum equals zero. Print YES if such a triplet exists, otherwise print NO.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "6\n-1 0 1 2 -1 -4",
        "sample_output": "YES",
        "test_cases_json": json.dumps([
            {"input": "6\n-1 0 1 2 -1 -4", "output": "YES"},
            {"input": "4\n1 2 3 4", "output": "NO"},
            {"input": "3\n-2 0 2", "output": "YES"}
        ])
    }
    
    ,

    # 41. Set Matrix Zeroes
    {
        "title": "Set Matrix Zeroes",
        "description": "Given an N x M matrix, if an element is zero, set its entire row and column to zero. Print the modified matrix row by row.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "3 3\n1 1 1\n1 0 1\n1 1 1",
        "sample_output": "1 0 1\n0 0 0\n1 0 1",
        "test_cases_json": json.dumps([
            {"input": "3 3\n1 1 1\n1 0 1\n1 1 1", "output": "1 0 1\n0 0 0\n1 0 1"},
            {"input": "2 3\n1 2 0\n4 5 6", "output": "0 0 0\n4 5 0"},
            {"input": "2 2\n1 2\n3 4", "output": "1 2\n3 4"}
        ])
    },

    # 42. Spiral Matrix Traversal
    {
        "title": "Spiral Matrix Traversal",
        "description": "Given an N x M matrix, print its elements in clockwise spiral order, starting from the top-left corner.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "3 3\n1 2 3\n4 5 6\n7 8 9",
        "sample_output": "1 2 3 6 9 8 7 4 5",
        "test_cases_json": json.dumps([
            {"input": "3 3\n1 2 3\n4 5 6\n7 8 9", "output": "1 2 3 6 9 8 7 4 5"},
            {"input": "2 3\n1 2 3\n4 5 6", "output": "1 2 3 6 5 4"},
            {"input": "1 4\n1 2 3 4", "output": "1 2 3 4"}
        ])
    },

    # 43. Transpose Matrix
    {
        "title": "Transpose Matrix",
        "description": "Given an N x M matrix, print its transpose. The transpose has M rows and N columns.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "2 3\n1 2 3\n4 5 6",
        "sample_output": "1 4\n2 5\n3 6",
        "test_cases_json": json.dumps([
            {"input": "2 3\n1 2 3\n4 5 6", "output": "1 4\n2 5\n3 6"},
            {"input": "2 2\n1 2\n3 4", "output": "1 3\n2 4"},
            {"input": "1 3\n7 8 9", "output": "7\n8\n9"}
        ])
    },

    # 44. Diagonal Sum of Matrix
    {
        "title": "Diagonal Sum of Matrix",
        "description": "Given an N x N square matrix, calculate the sum of its primary diagonal elements and print the result.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "3\n1 2 3\n4 5 6\n7 8 9",
        "sample_output": "15",
        "test_cases_json": json.dumps([
            {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "15"},
            {"input": "2\n5 1\n2 4", "output": "9"},
            {"input": "1\n8", "output": "8"}
        ])
    },

    # 45. Row with Maximum Ones
    {
        "title": "Row with Maximum Ones",
        "description": "Given an N x M binary matrix, find the zero-based index of the row containing the maximum number of ones. If multiple rows have the same maximum count, print the smallest index.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "3 4\n0 1 1 1\n1 1 1 1\n0 0 1 1",
        "sample_output": "1",
        "test_cases_json": json.dumps([
            {"input": "3 4\n0 1 1 1\n1 1 1 1\n0 0 1 1", "output": "1"},
            {"input": "2 3\n1 0 0\n0 1 0", "output": "0"},
            {"input": "2 2\n0 0\n0 0", "output": "0"}
        ])
    },

    # 46. Rotate Matrix 90 Degrees
    {
        "title": "Rotate Matrix 90 Degrees Clockwise",
        "description": "Given an N x N square matrix, rotate it 90 degrees clockwise and print the resulting matrix.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "3\n1 2 3\n4 5 6\n7 8 9",
        "sample_output": "7 4 1\n8 5 2\n9 6 3",
        "test_cases_json": json.dumps([
            {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "7 4 1\n8 5 2\n9 6 3"},
            {"input": "2\n1 2\n3 4", "output": "3 1\n4 2"},
            {"input": "1\n5", "output": "5"}
        ])
    },

    # 47. Missing and Repeating Number
    {
        "title": "Find Missing and Repeating Number",
        "description": "An array contains N integers from 1 to N. Exactly one number is missing and exactly one different number occurs twice. Print the repeating number followed by the missing number.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5\n1 3 3 4 5",
        "sample_output": "3 2",
        "test_cases_json": json.dumps([
            {"input": "5\n1 3 3 4 5", "output": "3 2"},
            {"input": "3\n1 1 3", "output": "1 2"},
            {"input": "4\n4 3 3 1", "output": "3 2"}
        ])
    },

    # 48. Find Duplicate Number
    {
        "title": "Find Duplicate Number",
        "description": "An array contains N+1 integers, each between 1 and N inclusive. Exactly one distinct value is repeated one or more times. Find and print that duplicate value.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "5\n1 3 4 2 2",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "5\n1 3 4 2 2", "output": "2"},
            {"input": "4\n3 1 3 4", "output": "3"},
            {"input": "6\n2 5 1 1 4 3", "output": "1"}
        ])
    },

    # 49. Maximum Circular Subarray Sum
    {
        "title": "Maximum Circular Subarray Sum",
        "description": "Given an array of N integers arranged in a circle, find the maximum sum of a non-empty contiguous circular subarray. Print the maximum sum.",
        "difficulty": "Hard",
        "topic": "Arrays",
        "xp_reward": 150,
        "sample_input": "7\n8 -8 9 -9 10 -11 12",
        "sample_output": "22",
        "test_cases_json": json.dumps([
            {"input": "7\n8 -8 9 -9 10 -11 12", "output": "22"},
            {"input": "3\n-3 -2 -5", "output": "-2"},
            {"input": "4\n5 -2 3 4", "output": "12"}
        ])
    },

    # 50. Next Permutation
    {
        "title": "Next Permutation",
        "description": "Given an array of N integers representing a permutation, rearrange it into the lexicographically next greater permutation. If no greater permutation exists, rearrange it into ascending order. Print the resulting array.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "3\n1 2 3",
        "sample_output": "1 3 2",
        "test_cases_json": json.dumps([
            {"input": "3\n1 2 3", "output": "1 3 2"},
            {"input": "3\n3 2 1", "output": "1 2 3"},
            {"input": "3\n1 1 5", "output": "1 5 1"}
        ])
    }
    
    ,

    # 51. Reverse a String
    {
        "title": "Reverse a String",
        "description": "Given a string, print the string in reverse order.",
        "difficulty": "Easy",
        "topic": "Strings",
        "xp_reward": 50,
        "sample_input": "hello",
        "sample_output": "olleh",
        "test_cases_json": json.dumps([
            {"input": "hello", "output": "olleh"},
            {"input": "CodeQuest", "output": "tseuQedoC"},
            {"input": "a", "output": "a"}
        ])
    },

    # 52. Check Palindrome String
    {
        "title": "Check Palindrome String",
        "description": "Given a string, check whether it reads the same forward and backward. Print YES if it is a palindrome; otherwise, print NO. Treat uppercase and lowercase letters as different.",
        "difficulty": "Easy",
        "topic": "Strings",
        "xp_reward": 50,
        "sample_input": "madam",
        "sample_output": "YES",
        "test_cases_json": json.dumps([
            {"input": "madam", "output": "YES"},
            {"input": "hello", "output": "NO"},
            {"input": "level", "output": "YES"}
        ])
    },

    # 53. Count Vowels and Consonants
    {
        "title": "Count Vowels and Consonants",
        "description": "Given a string containing English letters and spaces, count the vowels and consonants. Ignore spaces. Print the vowel count followed by the consonant count.",
        "difficulty": "Easy",
        "topic": "Strings",
        "xp_reward": 50,
        "sample_input": "hello world",
        "sample_output": "3 7",
        "test_cases_json": json.dumps([
            {"input": "hello world", "output": "3 7"},
            {"input": "CodeQuest", "output": "4 5"},
            {"input": "AEIOU", "output": "5 0"}
        ])
    },

    # 54. Character Frequency
    {
        "title": "Character Frequency",
        "description": "Given a string and a character on the next line, count how many times that character occurs in the string. Treat uppercase and lowercase as different.",
        "difficulty": "Easy",
        "topic": "Strings",
        "xp_reward": 50,
        "sample_input": "programming\ng",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "programming\ng", "output": "2"},
            {"input": "banana\na", "output": "3"},
            {"input": "hello\nz", "output": "0"}
        ])
    },

    # 55. Remove Duplicate Characters
    {
        "title": "Remove Duplicate Characters",
        "description": "Given a string, remove repeated characters while preserving the order of their first occurrence. Print the resulting string.",
        "difficulty": "Easy",
        "topic": "Strings",
        "xp_reward": 50,
        "sample_input": "programming",
        "sample_output": "progamin",
        "test_cases_json": json.dumps([
            {"input": "programming", "output": "progamin"},
            {"input": "banana", "output": "ban"},
            {"input": "aaaa", "output": "a"}
        ])
    },

    # 56. Check Anagram Strings
    {
        "title": "Check Anagram Strings",
        "description": "Given two lowercase strings on separate lines, check whether they contain exactly the same characters with the same frequencies. Print YES if they are anagrams; otherwise, print NO.",
        "difficulty": "Easy",
        "topic": "Strings",
        "xp_reward": 50,
        "sample_input": "listen\nsilent",
        "sample_output": "YES",
        "test_cases_json": json.dumps([
            {"input": "listen\nsilent", "output": "YES"},
            {"input": "hello\nworld", "output": "NO"},
            {"input": "aabb\nbbaa", "output": "YES"}
        ])
    },

    # 57. First Non-Repeating Character
    {
        "title": "First Non-Repeating Character",
        "description": "Given a string, find the first character that occurs exactly once. Print that character. If no such character exists, print -1.",
        "difficulty": "Easy",
        "topic": "Strings",
        "xp_reward": 50,
        "sample_input": "swiss",
        "sample_output": "w",
        "test_cases_json": json.dumps([
            {"input": "swiss", "output": "w"},
            {"input": "aabbc", "output": "c"},
            {"input": "aabb", "output": "-1"}
        ])
    },

    # 58. Longest Common Prefix
    {
        "title": "Longest Common Prefix",
        "description": "Given N strings, find and print their longest common prefix. If no common prefix exists, print -1.",
        "difficulty": "Easy",
        "topic": "Strings",
        "xp_reward": 50,
        "sample_input": "3\nflower\nflow\nflight",
        "sample_output": "fl",
        "test_cases_json": json.dumps([
            {"input": "3\nflower\nflow\nflight", "output": "fl"},
            {"input": "3\napple\nape\napril", "output": "ap"},
            {"input": "2\ncat\ndog", "output": "-1"}
        ])
    },

    # 59. Longest Substring Without Repeating Characters
    {
        "title": "Longest Substring Without Repeating Characters",
        "description": "Given a string, find the length of the longest substring containing no repeated characters. Print its length.",
        "difficulty": "Medium",
        "topic": "Strings",
        "xp_reward": 100,
        "sample_input": "abcabcbb",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "abcabcbb", "output": "3"},
            {"input": "bbbbb", "output": "1"},
            {"input": "pwwkew", "output": "3"}
        ])
    },

    # 60. String Compression
    {
        "title": "String Compression",
        "description": "Compress a string by replacing each consecutive group of identical characters with the character followed by its count. Print the compressed string. Include the count even when it is 1.",
        "difficulty": "Medium",
        "topic": "Strings",
        "xp_reward": 100,
        "sample_input": "aaabbc",
        "sample_output": "a3b2c1",
        "test_cases_json": json.dumps([
            {"input": "aaabbc", "output": "a3b2c1"},
            {"input": "abcd", "output": "a1b1c1d1"},
            {"input": "aaaaa", "output": "a5"}
        ])
    }

    ,

    # 64. Frequency of Array Elements
    {
        "title": "Frequency of Array Elements",
        "description": "Given an array of N integers, print each distinct element and its frequency in the order in which each element first appears. Print each element and frequency on a separate line.",
        "difficulty": "Easy",
        "topic": "Hashing",
        "xp_reward": 50,
        "sample_input": "7\n1 2 2 3 1 4 2",
        "sample_output": "1 2\n2 3\n3 1\n4 1",
        "test_cases_json": json.dumps([
            {"input": "7\n1 2 2 3 1 4 2", "output": "1 2\n2 3\n3 1\n4 1"},
            {"input": "5\n5 5 5 5 5", "output": "5 5"},
            {"input": "4\n1 2 3 4", "output": "1 1\n2 1\n3 1\n4 1"}
        ])
    },

    # 65. Two Sum Using Hashing
    {
        "title": "Two Sum Using Hashing",
        "description": "Given an array of N integers and a target K, find two distinct elements whose sum equals K. Print their zero-based indices in ascending order. If no pair exists, print -1.",
        "difficulty": "Easy",
        "topic": "Hashing",
        "xp_reward": 50,
        "sample_input": "4 9\n2 7 11 15",
        "sample_output": "0 1",
        "test_cases_json": json.dumps([
            {"input": "4 9\n2 7 11 15", "output": "0 1"},
            {"input": "3 6\n3 2 4", "output": "1 2"},
            {"input": "3 10\n1 2 3", "output": "-1"}
        ])
    },

    # 66. First Repeating Element
    {
        "title": "First Repeating Element",
        "description": "Given an array of N integers, find the first element from the left that occurs more than once in the array. Print the element, or -1 if no element repeats.",
        "difficulty": "Easy",
        "topic": "Hashing",
        "xp_reward": 50,
        "sample_input": "7\n10 5 3 4 3 5 6",
        "sample_output": "5",
        "test_cases_json": json.dumps([
            {"input": "7\n10 5 3 4 3 5 6", "output": "5"},
            {"input": "5\n1 2 3 4 5", "output": "-1"},
            {"input": "4\n7 7 2 2", "output": "7"}
        ])
    },

    # 67. First Non-Repeating Element
    {
        "title": "First Non-Repeating Element",
        "description": "Given an array of N integers, find the first element from the left that occurs exactly once. Print the element, or -1 if no such element exists.",
        "difficulty": "Easy",
        "topic": "Hashing",
        "xp_reward": 50,
        "sample_input": "7\n4 5 1 2 1 4 5",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "7\n4 5 1 2 1 4 5", "output": "2"},
            {"input": "4\n1 1 2 2", "output": "-1"},
            {"input": "5\n3 3 4 5 5", "output": "4"}
        ])
    },

    # 68. Count Pairs with Given Sum
    {
        "title": "Count Pairs with Given Sum",
        "description": "Given an array of N integers and a target K, count the number of index pairs (i, j) such that i < j and arr[i] + arr[j] = K. Each pair of indices is counted separately.",
        "difficulty": "Medium",
        "topic": "Hashing",
        "xp_reward": 100,
        "sample_input": "5 6\n1 5 7 -1 5",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "5 6\n1 5 7 -1 5", "output": "3"},
            {"input": "4 4\n2 2 2 2", "output": "6"},
            {"input": "3 10\n1 2 3", "output": "0"}
        ])
    },

    # 69. Group Anagrams
    {
        "title": "Group Anagrams",
        "description": "Given N lowercase words, group words that are anagrams of each other. Print each group on a separate line, preserving the order in which groups first appear and the original order of words within each group.",
        "difficulty": "Medium",
        "topic": "Hashing",
        "xp_reward": 100,
        "sample_input": "5\neat\ntea\ntan\nate\nnat",
        "sample_output": "eat tea ate\ntan nat",
        "test_cases_json": json.dumps([
            {"input": "5\neat\ntea\ntan\nate\nnat", "output": "eat tea ate\ntan nat"},
            {"input": "3\nabc\nbca\nxyz", "output": "abc bca\nxyz"},
            {"input": "4\ncat\ntac\nact\ndog", "output": "cat tac act\ndog"}
        ])
    },

    # 70. Longest Consecutive Sequence Using Hashing
    {
        "title": "Longest Consecutive Sequence Using Hashing",
        "description": "Given an unsorted array of N integers, find the length of the longest sequence of consecutive integer values. The values do not need to appear next to each other in the array.",
        "difficulty": "Medium",
        "topic": "Hashing",
        "xp_reward": 100,
        "sample_input": "6\n100 4 200 1 3 2",
        "sample_output": "4",
        "test_cases_json": json.dumps([
            {"input": "6\n100 4 200 1 3 2", "output": "4"},
            {"input": "5\n1 2 2 3 4", "output": "4"},
            {"input": "4\n10 30 20 40", "output": "1"}
        ])
    },

    # 71. Subarray with Zero Sum
    {
        "title": "Subarray with Zero Sum",
        "description": "Given an array of N integers, determine whether any non-empty contiguous subarray has a sum of zero. Print YES if one exists; otherwise, print NO.",
        "difficulty": "Medium",
        "topic": "Hashing",
        "xp_reward": 100,
        "sample_input": "5\n4 2 -3 1 6",
        "sample_output": "YES",
        "test_cases_json": json.dumps([
            {"input": "5\n4 2 -3 1 6", "output": "YES"},
            {"input": "3\n1 2 3", "output": "NO"},
            {"input": "4\n1 -1 2 3", "output": "YES"}
        ])
    }
    
    ,

    # 72. Binary Search
    {
        "title": "Binary Search",
        "description": "Given a sorted array of N integers and a target K, find the zero-based index of K using binary search. Print -1 if K is not present.",
        "difficulty": "Easy",
        "topic": "Searching & Sorting",
        "xp_reward": 50,
        "sample_input": "5 4\n1 2 4 6 8",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "5 4\n1 2 4 6 8", "output": "2"},
            {"input": "5 7\n1 3 5 7 9", "output": "3"},
            {"input": "4 10\n1 2 3 4", "output": "-1"}
        ])
    },

    # 73. Recursive Binary Search
    {
        "title": "Recursive Binary Search",
        "description": "Given a sorted array of N integers and a target K, implement binary search recursively. Print the zero-based index of K, or -1 if it is not present.",
        "difficulty": "Easy",
        "topic": "Searching & Sorting",
        "xp_reward": 50,
        "sample_input": "5 7\n1 3 5 7 9",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "5 7\n1 3 5 7 9", "output": "3"},
            {"input": "4 1\n1 2 3 4", "output": "0"},
            {"input": "4 8\n1 2 3 4", "output": "-1"}
        ])
    },

    # 74. Lower Bound
    {
        "title": "Lower Bound",
        "description": "Given a sorted array of N integers and a target K, find the smallest zero-based index where the array element is greater than or equal to K. If no such index exists, print N.",
        "difficulty": "Easy",
        "topic": "Searching & Sorting",
        "xp_reward": 50,
        "sample_input": "5 4\n1 2 4 4 6",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "5 4\n1 2 4 4 6", "output": "2"},
            {"input": "5 3\n1 2 4 5 6", "output": "2"},
            {"input": "3 10\n1 2 3", "output": "3"}
        ])
    },

    # 75. Upper Bound
    {
        "title": "Upper Bound",
        "description": "Given a sorted array of N integers and a target K, find the smallest zero-based index where the array element is strictly greater than K. If no such index exists, print N.",
        "difficulty": "Easy",
        "topic": "Searching & Sorting",
        "xp_reward": 50,
        "sample_input": "5 4\n1 2 4 4 6",
        "sample_output": "4",
        "test_cases_json": json.dumps([
            {"input": "5 4\n1 2 4 4 6", "output": "4"},
            {"input": "5 3\n1 2 4 5 6", "output": "2"},
            {"input": "3 10\n1 2 3", "output": "3"}
        ])
    },

    # 76. Bubble Sort
    {
        "title": "Bubble Sort",
        "description": "Given an array of N integers, sort it in ascending order using the Bubble Sort algorithm. Print the sorted elements separated by spaces.",
        "difficulty": "Easy",
        "topic": "Searching & Sorting",
        "xp_reward": 50,
        "sample_input": "5\n5 1 4 2 8",
        "sample_output": "1 2 4 5 8",
        "test_cases_json": json.dumps([
            {"input": "5\n5 1 4 2 8", "output": "1 2 4 5 8"},
            {"input": "4\n4 3 2 1", "output": "1 2 3 4"},
            {"input": "3\n1 2 3", "output": "1 2 3"}
        ])
    },

    # 77. Merge Sort
    {
        "title": "Merge Sort",
        "description": "Given an array of N integers, sort it in ascending order using the Merge Sort algorithm. Print the sorted elements separated by spaces.",
        "difficulty": "Medium",
        "topic": "Searching & Sorting",
        "xp_reward": 100,
        "sample_input": "6\n38 27 43 3 9 82",
        "sample_output": "3 9 27 38 43 82",
        "test_cases_json": json.dumps([
            {"input": "6\n38 27 43 3 9 82", "output": "3 9 27 38 43 82"},
            {"input": "5\n5 4 3 2 1", "output": "1 2 3 4 5"},
            {"input": "4\n-2 5 0 -1", "output": "-2 -1 0 5"}
        ])
    },

    # 78. Quick Sort
    {
        "title": "Quick Sort",
        "description": "Given an array of N integers, sort it in ascending order using the Quick Sort algorithm. Print the sorted elements separated by spaces.",
        "difficulty": "Medium",
        "topic": "Searching & Sorting",
        "xp_reward": 100,
        "sample_input": "6\n10 7 8 9 1 5",
        "sample_output": "1 5 7 8 9 10",
        "test_cases_json": json.dumps([
            {"input": "6\n10 7 8 9 1 5", "output": "1 5 7 8 9 10"},
            {"input": "5\n3 3 2 1 2", "output": "1 2 2 3 3"},
            {"input": "4\n-5 0 8 -2", "output": "-5 -2 0 8"}
        ])
    },

    # 79. Count Inversions in an Array
    {
        "title": "Count Inversions in an Array",
        "description": "An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j]. Given an array of N integers, count and print the total number of inversions.",
        "difficulty": "Hard",
        "topic": "Searching & Sorting",
        "xp_reward": 150,
        "sample_input": "5\n2 4 1 3 5",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "5\n2 4 1 3 5", "output": "3"},
            {"input": "4\n4 3 2 1", "output": "6"},
            {"input": "3\n1 2 3", "output": "0"}
        ])
    }

    ,

    # 80. Insert Node at End of Linked List
    {
        "title": "Insert Node at End of Linked List",
        "description": "Given N integers representing a linked list and an integer X, insert X at the end of the list. Print the resulting list.",
        "difficulty": "Easy",
        "topic": "Linked Lists",
        "xp_reward": 50,
        "sample_input": "4\n1 2 3 4\n5",
        "sample_output": "1 2 3 4 5",
        "test_cases_json": json.dumps([
            {"input": "4\n1 2 3 4\n5", "output": "1 2 3 4 5"},
            {"input": "0\n\n10", "output": "10"},
            {"input": "1\n7\n9", "output": "7 9"}
        ])
    },

    # 81. Delete Node by Value
    {
        "title": "Delete Node by Value",
        "description": "Given N integers representing a linked list and an integer X, delete the first occurrence of X. If X is not present, leave the list unchanged. Print the resulting list. If the list becomes empty, print EMPTY.",
        "difficulty": "Easy",
        "topic": "Linked Lists",
        "xp_reward": 50,
        "sample_input": "5\n1 2 3 2 4\n2",
        "sample_output": "1 3 2 4",
        "test_cases_json": json.dumps([
            {"input": "5\n1 2 3 2 4\n2", "output": "1 3 2 4"},
            {"input": "3\n1 2 3\n5", "output": "1 2 3"},
            {"input": "1\n7\n7", "output": "EMPTY"}
        ])
    },

    # 82. Reverse a Linked List
    {
        "title": "Reverse a Linked List",
        "description": "Given N integers representing a singly linked list, reverse the linked list and print its elements.",
        "difficulty": "Easy",
        "topic": "Linked Lists",
        "xp_reward": 50,
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "5 4 3 2 1",
        "test_cases_json": json.dumps([
            {"input": "5\n1 2 3 4 5", "output": "5 4 3 2 1"},
            {"input": "1\n10", "output": "10"},
            {"input": "0\n", "output": "EMPTY"}
        ])
    },

    # 83. Find Middle of Linked List
    {
        "title": "Find Middle of Linked List",
        "description": "Given N integers representing a singly linked list, find the middle node using the zero-based index. If N is even, print the second middle element.",
        "difficulty": "Easy",
        "topic": "Linked Lists",
        "xp_reward": 50,
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "5\n1 2 3 4 5", "output": "3"},
            {"input": "4\n1 2 3 4", "output": "3"},
            {"input": "1\n9", "output": "9"}
        ])
    },

    # 84. Detect Cycle in Linked List
    {
        "title": "Detect Cycle in Linked List",
        "description": "Given N integers representing the values of a linked list and an integer P representing the zero-based index where the last node connects back to an earlier node, determine whether the list contains a cycle. If P is -1, the last node does not connect to another node. Print YES if a cycle exists; otherwise, print NO.",
        "difficulty": "Medium",
        "topic": "Linked Lists",
        "xp_reward": 100,
        "sample_input": "4\n1 2 3 4\n1",
        "sample_output": "YES",
        "test_cases_json": json.dumps([
            {"input": "4\n1 2 3 4\n1", "output": "YES"},
            {"input": "3\n1 2 3\n-1", "output": "NO"},
            {"input": "1\n5\n0", "output": "YES"}
        ])
    }

    ,

    # 85. Implement Stack Using Array
    {
        "title": "Implement Stack Using Array",
        "description": "Implement a stack supporting PUSH X, POP, and TOP operations. The first input is Q, the number of operations. For PUSH X, insert X. For POP, remove and print the top element, or print -1 if empty. For TOP, print the top element without removing it, or print -1 if empty.",
        "difficulty": "Easy",
        "topic": "Stacks & Queues",
        "xp_reward": 50,
        "sample_input": "7\nPUSH 10\nPUSH 20\nTOP\nPOP\nTOP\nPOP\nPOP",
        "sample_output": "20\n20\n10\n-1",
        "test_cases_json": json.dumps([
            {"input": "7\nPUSH 10\nPUSH 20\nTOP\nPOP\nTOP\nPOP\nPOP", "output": "20\n20\n10\n-1"},
            {"input": "4\nPOP\nPUSH 5\nTOP\nPOP", "output": "-1\n5\n5"},
            {"input": "3\nPUSH 1\nPUSH 2\nPOP", "output": "2"}
        ])
    },

    # 86. Valid Parentheses
    {
        "title": "Valid Parentheses",
        "description": "Given a string containing only the characters (, ), {, }, [ and ], determine whether the brackets are correctly balanced and properly nested. Print YES if valid; otherwise, print NO.",
        "difficulty": "Easy",
        "topic": "Stacks & Queues",
        "xp_reward": 50,
        "sample_input": "{[()]}",
        "sample_output": "YES",
        "test_cases_json": json.dumps([
            {"input": "{[()]}", "output": "YES"},
            {"input": "([)]", "output": "NO"},
            {"input": "(((", "output": "NO"}
        ])
    },

    # 87. Next Greater Element
    {
        "title": "Next Greater Element",
        "description": "Given an array of N integers, find the first element to the right of each element that is strictly greater than it. If no such element exists, print -1 for that position. Print all answers separated by spaces.",
        "difficulty": "Medium",
        "topic": "Stacks & Queues",
        "xp_reward": 100,
        "sample_input": "4\n4 5 2 25",
        "sample_output": "5 25 25 -1",
        "test_cases_json": json.dumps([
            {"input": "4\n4 5 2 25", "output": "5 25 25 -1"},
            {"input": "4\n13 7 6 12", "output": "-1 12 12 -1"},
            {"input": "3\n1 2 3", "output": "2 3 -1"}
        ])
    },

    # 88. Implement Queue Using Array
    {
        "title": "Implement Queue Using Array",
        "description": "Implement a queue supporting ENQUEUE X, DEQUEUE, and FRONT operations. The first input is Q, the number of operations. ENQUEUE X inserts X at the rear. DEQUEUE removes and prints the front element, or prints -1 if empty. FRONT prints the front element without removing it, or -1 if empty.",
        "difficulty": "Easy",
        "topic": "Stacks & Queues",
        "xp_reward": 50,
        "sample_input": "7\nENQUEUE 10\nENQUEUE 20\nFRONT\nDEQUEUE\nFRONT\nDEQUEUE\nDEQUEUE",
        "sample_output": "10\n10\n20\n20\n-1",
        "test_cases_json": json.dumps([
            {"input": "7\nENQUEUE 10\nENQUEUE 20\nFRONT\nDEQUEUE\nFRONT\nDEQUEUE\nDEQUEUE", "output": "10\n10\n20\n20\n-1"},
            {"input": "4\nDEQUEUE\nENQUEUE 5\nFRONT\nDEQUEUE", "output": "-1\n5\n5"},
            {"input": "3\nENQUEUE 1\nENQUEUE 2\nDEQUEUE", "output": "1"}
        ])
    },

    # 89. First Non-Repeating Character in a Stream
    {
        "title": "First Non-Repeating Character in a Stream",
        "description": "Given a lowercase string, process its characters from left to right. After each character is added, print the first character seen exactly once so far. If no character is non-repeating, print -1. Separate answers with spaces.",
        "difficulty": "Medium",
        "topic": "Stacks & Queues",
        "xp_reward": 100,
        "sample_input": "aabc",
        "sample_output": "a -1 b b",
        "test_cases_json": json.dumps([
            {"input": "aabc", "output": "a -1 b b"},
            {"input": "zz", "output": "z -1"},
            {"input": "abc", "output": "a a a"}
        ])
    }

    ,

    # 90. Binary Tree Level Order Traversal
    {
        "title": "Binary Tree Level Order Traversal",
        "description": "Given a binary tree in level-order format, print its nodes level by level from left to right. The first input is N, followed by N space-separated node values. Use -1 to represent a missing child. Print all actual node values in level-order.",
        "difficulty": "Easy",
        "topic": "Binary Trees & BST",
        "xp_reward": 50,
        "sample_input": "7\n1 2 3 4 5 6 7",
        "sample_output": "1 2 3 4 5 6 7",
        "test_cases_json": json.dumps([
            {"input": "7\n1 2 3 4 5 6 7", "output": "1 2 3 4 5 6 7"},
            {"input": "5\n1 2 3 -1 4", "output": "1 2 3 4"},
            {"input": "1\n10", "output": "10"}
        ])
    },

    # 91. Height of Binary Tree
    {
        "title": "Height of Binary Tree",
        "description": "Given a binary tree in level-order format, find its height measured in the number of nodes along the longest root-to-leaf path. The first input is N, followed by N node values. Use -1 to represent a missing child. Print 0 for an empty tree.",
        "difficulty": "Easy",
        "topic": "Binary Trees & BST",
        "xp_reward": 50,
        "sample_input": "7\n1 2 3 4 5 6 7",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "7\n1 2 3 4 5 6 7", "output": "3"},
            {"input": "5\n1 2 3 -1 4", "output": "3"},
            {"input": "1\n10", "output": "1"}
        ])
    },

    # 92. Count Leaf Nodes
    {
        "title": "Count Leaf Nodes",
        "description": "Given a binary tree in level-order format, count the number of leaf nodes. A leaf node is a node with no left or right child. The first input is N, followed by N node values. Use -1 to represent a missing child.",
        "difficulty": "Easy",
        "topic": "Binary Trees & BST",
        "xp_reward": 50,
        "sample_input": "7\n1 2 3 4 5 6 7",
        "sample_output": "4",
        "test_cases_json": json.dumps([
            {"input": "7\n1 2 3 4 5 6 7", "output": "4"},
            {"input": "5\n1 2 3 -1 4", "output": "2"},
            {"input": "1\n10", "output": "1"}
        ])
    },

    # 93. Search in Binary Search Tree
    {
        "title": "Search in Binary Search Tree",
        "description": "Given N distinct integers, insert them into a Binary Search Tree in the given order. Then search for the target value K. Print YES if K exists in the BST; otherwise, print NO.",
        "difficulty": "Easy",
        "topic": "Binary Trees & BST",
        "xp_reward": 50,
        "sample_input": "5 4\n8 3 10 1 6",
        "sample_output": "YES",
        "test_cases_json": json.dumps([
            {"input": "5 6\n8 3 10 1 6", "output": "YES"},
            {"input": "5 7\n8 3 10 1 6", "output": "NO"},
            {"input": "1 5\n5", "output": "YES"}
        ])
    },

    # 94. Validate Binary Search Tree
    {
        "title": "Validate Binary Search Tree",
        "description": "Given a binary tree in level-order format, determine whether it satisfies the Binary Search Tree property: every node's left subtree contains only smaller values and its right subtree contains only larger values. The first input is N, followed by N node values. Use -1 to represent a missing child. Print YES if valid; otherwise, print NO.",
        "difficulty": "Medium",
        "topic": "Binary Trees & BST",
        "xp_reward": 100,
        "sample_input": "7\n5 3 8 2 4 6 9",
        "sample_output": "YES",
        "test_cases_json": json.dumps([
            {"input": "7\n5 3 8 2 4 6 9", "output": "YES"},
            {"input": "3\n5 6 8", "output": "NO"},
            {"input": "3\n5 3 7", "output": "YES"}
        ])
    },

    # 95. Breadth First Search in Graph
    {
        "title": "Breadth First Search in Graph",
        "description": "Given an undirected graph with N vertices numbered 0 to N-1 and M edges, perform Breadth First Search starting from vertex S. Visit adjacent vertices in ascending order. Print the traversal order. The input contains N M, followed by M edges, followed by S.",
        "difficulty": "Easy",
        "topic": "Graphs",
        "xp_reward": 50,
        "sample_input": "5 4\n0 1\n0 2\n1 3\n2 4\n0",
        "sample_output": "0 1 2 3 4",
        "test_cases_json": json.dumps([
            {"input": "5 4\n0 1\n0 2\n1 3\n2 4\n0", "output": "0 1 2 3 4"},
            {"input": "4 2\n0 1\n2 3\n2", "output": "2 3"},
            {"input": "3 0\n1", "output": "1"}
        ])
    },

    # 96. Count Connected Components
    {
        "title": "Count Connected Components",
        "description": "Given an undirected graph with N vertices numbered 0 to N-1 and M edges, count the number of connected components. The input contains N M, followed by M edges. Print the component count.",
        "difficulty": "Medium",
        "topic": "Graphs",
        "xp_reward": 100,
        "sample_input": "5 2\n0 1\n3 4",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "5 2\n0 1\n3 4", "output": "3"},
            {"input": "4 3\n0 1\n1 2\n2 3", "output": "1"},
            {"input": "3 0", "output": "3"}
        ])
    },

    # 97. Shortest Path in an Unweighted Graph
    {
        "title": "Shortest Path in an Unweighted Graph",
        "description": "Given an undirected unweighted graph with N vertices numbered 0 to N-1 and M edges, find the minimum number of edges in a path from source S to destination D. The input contains N M, followed by M edges, followed by S D. Print -1 if D is unreachable from S.",
        "difficulty": "Medium",
        "topic": "Graphs",
        "xp_reward": 100,
        "sample_input": "5 5\n0 1\n0 2\n1 3\n2 3\n3 4\n0 4",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "5 5\n0 1\n0 2\n1 3\n2 3\n3 4\n0 4", "output": "3"},
            {"input": "4 2\n0 1\n2 3\n0 3", "output": "-1"},
            {"input": "3 2\n0 1\n1 2\n1 1", "output": "0"}
        ])
    },

    # 98. Count Subsets with Given Sum
    {
        "title": "Count Subsets with Given Sum",
        "description": "Given an array of N integers and a target K, count the number of subsets whose elements sum to K. Each array index can be used at most once. Different index selections count as different subsets. The empty subset is allowed when K is zero. Print the count.",
        "difficulty": "Medium",
        "topic": "Recursion & Backtracking",
        "xp_reward": 100,
        "sample_input": "3 3\n1 2 3",
        "sample_output": "2",
        "test_cases_json": json.dumps([
            {"input": "3 3\n1 2 3", "output": "2"},
            {"input": "4 5\n1 2 3 4", "output": "2"},
            {"input": "3 0\n1 2 3", "output": "1"}
        ])
    },

    # 99. Minimum Coins
    {
        "title": "Minimum Coins",
        "description": "Given N coin denominations and a target amount K, find the minimum number of coins required to make exactly K. You may use each denomination unlimited times. Print -1 if the amount cannot be formed.",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "xp_reward": 100,
        "sample_input": "3 11\n1 2 5",
        "sample_output": "3",
        "test_cases_json": json.dumps([
            {"input": "3 11\n1 2 5", "output": "3"},
            {"input": "2 3\n2 4", "output": "-1"},
            {"input": "3 0\n1 2 5", "output": "0"}
        ])
    },

    # 100. Activity Selection
    {
        "title": "Activity Selection",
        "description": "Given N activities with their start and finish times, select the maximum number of non-overlapping activities that can be performed by one person. An activity can start at the exact time another activity finishes. Print the maximum number of selected activities. Each activity is given on a separate line as start finish.",
        "difficulty": "Medium",
        "topic": "Greedy",
        "xp_reward": 100,
        "sample_input": "6\n1 2\n3 4\n0 6\n5 7\n8 9\n5 9",
        "sample_output": "4",
        "test_cases_json": json.dumps([
            {"input": "6\n1 2\n3 4\n0 6\n5 7\n8 9\n5 9", "output": "4"},
            {"input": "3\n1 3\n2 4\n3 5", "output": "2"},
            {"input": "1\n4 6", "output": "1"}
        ])
    }

]
