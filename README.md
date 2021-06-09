# Algorithms_For_Problem_Solving
Programming Challenges and Solutions for Fun

|   |   |   |   |
|:---:|:---:|:---:|:---:|
|[Count the Islands](#CountTheIslands)|[String of Parentheses](#StringofParentheses)|[Minimum Coins](#Minimum_Coins)|[FindSquare](#FindSquare)|
|[Can you make a palindrome from a given string](#Canyoumakeapalindromefromagivenstring)|[Intersect Area of two Rectangles](#IntersectAreaoftwoRectangles)|[Integer Palindrome Checker](#IntegerPalindromeChecker)| [Stack Using Heap](#StackUsingHeap) |
|[Smallest Sparse Number](#smallestSparseNumber)|  [N<sup>th</sup> Sevenish Number](#Nthsevenishnumber)|[Max & Min](#Max_&_Min)|[Maximum Subarray Sum of a Circular Array](#Maximum_Subarray_Sum_of_a_Circular_Array) |
|[Sherlock and Anagrams](#Sherlock_and_Anagrams)|[Hash Tables: Ransom Note](#Hash_Tables_Ransom_Note)|[Minimum Swaps 2](#Minimum_Swaps_2)|[New Year Chaos](#New_Year_Chaos)|
|[Two Strings](#Two_Strings)|[Array Manipulation](#Array_Manipulation)|[Super Palindromes](Super_Palindromes)|[Moving Robot](Moving_Robot)|
|[Minimum Cost](#Minimum_Cost)|[Min Stack](#Min_Stack)|[Valid Parentheses](#Valid_Parentheses)|[Minimum Number of Swaps to Make the Binary String Alternating](#Minimum_Swaps)|
|[Sum of All Subset XOR Totals](#XOR_Totals)|[Finding Pairs With a Certain Sum](#FindSumPairs)|[Largest Number](#Largest_Number)|[Best Team With No Conflicts](#Best_Team_With_No_Conflicts)|
|[Longer Contiguous Segments of Ones than Zeros](#Ones_than_Zeros)|[Minimum Speed to Arrive on Time](#minSpeedOnTime)|[Smaller Strings](#SmallerStrings)|[Jump Game](#JumpGame)|
|[Top K Frequent Words](#topKFrequent)|[Course Schedule II](#Course_Schedule)|[Redundant Connection](#RedundantConnection)|[Binary Search](#BinarySearch)|
|[Merge Sort](#MergeSort)|[Sqrt(x)](#Sqrt)|[Search for a Range](#searchRange)|[First Bad Version](#firstBadVersion)|
|[Find Peak Element](#findPeakElement)|[Reverse Linked List](#reverseList)|[Swap Nodes in Pairs](#swapPairs)|[Fibonacci Number ](#fib)|
|[Merge Two Sorted Lists](#mergeTwoLists)|[Maximum Depth of Binary Tree](#maxDepth)|[Factorial](#Factorial)|[Climbing Stairs](#climbStairs)|
|[Determine Whether Matrix Can Be Obtained By Rotation](#findRotation)|[Reduction Operations to Make the Array Elements Equal](#reductionOperations)|[Pascal's Triangle II](#PascalTriangle)|[-](#-)|
---
### N<sup>th</sup> Sevenish Number<a name="Nthsevenishnumber"></a>
#### Challenge : 
Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.

#### Solutions :
  * [NthSevenish.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/NthSevenish.py)
  
---
### Count the Islands<a name="CountTheIslands"></a>
#### Challenge : 
  Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a   group of 1s that are neighboring whose perimeter is surrounded by water.
  For example, this matrix has 4 islands.
  1 0 0 0 0  
  0 0 1 1 0  
  0 1 1 0 0  
  0 0 0 0 0  
  1 1 0 0 1  
  1 1 0 0 1

#### Solutions :
  * [CounttheIslands.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/Solutions/CounttheIslands.py)
  * [CounttheIslands2.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/Solutions/CountTheIslands2.py)
---
### String of Parentheses<a name="StringofParentheses"></a>
#### Challenge : 
  Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).
#### Solutions :
  * [StringofParentheses.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/Solutions/StringofParentheses.py)
---
### Minimum Coins<a name="Minimum_Coins"></a>
#### Challenge : 
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
#### Solutions :
  * [MinCoins.java](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/java/MinCoins.java)
---
### FindSquare<a name="FindSquare"></a>
#### Challenge : 
Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.
#### Solutions :
  * [FindSquare.java](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/java/FindSquare.java)
---
### Stack Using Heap<a name="StackUsingHeap"></a>
#### Challenge :
Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
#### Solutions :
  * [StackFromHeap.java](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/java/StackFromHeap.java)
---
### Can you make a palindrome from a given string<a name="Canyoumakeapalindromefromagivenstring"></a>
#### Challenge :
Given a string, determine whether any permutation of it is a palindrome.
For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
#### Solutions :
  * [CanMakePalindrome.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/CanMakePalindrome.py)
---
### Intersect Area of two Rectangles<a name="IntersectAreaoftwoRectangles"></a>
#### Challenge :
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.
For example, given the following rectangles:  
```
{  
    "top_left": (1, 4),  
    "dimensions": (3, 3) # width, height  
}  
and  
{  
    "top_left": (0, 5),  
    "dimensions": (4, 3) # width, height  
}  
return 6. 
``` 
#### Solutions :
  * [RectangleIntersection.java](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/java/RectangleIntersection.java)
---
### Integer Palindrome Checker<a name="IntegerPalindromeChecker"></a>
#### Challenge :
Write a program that checks the given integer is a palindrome. For a example, 
121, 888 are palindromes. 678 is not a palindrome.
Do not convert the integer into a string.
#### Solutions :
  * [IntegerPalindrome.java](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/java/IntegerPalindrome.java)
---
### Smallest Sparse Number<a name="smallestSparseNumber"></a>
#### Challenge :
We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse, but 22 (10110) is not.
For a given input N, find the smallest sparse number greater than or equal to N.
Do this in faster than O(N log N) time.
#### Solutions :
  * [smallestSparseNumber.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/smallestSparseNumber.py)
---
### Sherlock and Anagrams<a name="Sherlock_and_Anagrams"></a>
#### Challenge :
[Read the problem in Hacker Rank](https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem)
#### Solutions :
  * [sherlock-and-anagrams.cpp](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/C%2B%2B/sherlock-and-anagrams.cpp)
---
### Max & Min<a name="Max_&_Min"></a>
#### Challenge :
Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
#### Solutions :
  * [maxMinFind235.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/maxMinFind235.py)
---
### Maximum Subarray Sum of a Circular Array<a name="Maximum_Subarray_Sum_of_a_Circular_Array"></a>
#### Challenge :
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.
For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.
Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
#### Solutions :
  * [LargestSubArray.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/LargestSubArray.py)
---
### Hash Tables: Ransom Note<a name="Hash_Tables_Ransom_Note"></a>
#### Challenge :
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is "No".  
[Read the problem in Hacker Rank](https://www.hackerrank.com/challenges/ctci-ransom-note/problem)
#### Solutions :
  * [ctci-ransom-note.cpp](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/C%2B%2B/ctci-ransom-note.cpp)
---
### Minimum Swaps 2<a name="Minimum_Swaps_2"></a>
#### Challenge :
You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.  
[Read the problem in Hacker Rank](https://www.hackerrank.com/challenges/minimum-swaps-2/problem)
#### Solutions :
  * [minimum-swaps-2.cpp](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/C%2B%2B/minimum-swaps-2.cpp)
---
### New Year Chaos<a name="New_Year_Chaos"></a>
#### Challenge :
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n=8 and person 5 bribes person 4, the queue will look like this: 1,2,3,5,4,6,7,8.

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!  
[Read the problem in Hacker Rank](https://www.hackerrank.com/challenges/new-year-chaos/problem)
#### Solutions :
  * [NewYearChaos.java](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/java/NewYearChaos.java)
---
### Two Strings<a name="Two_Strings"></a>
#### Challenge :
Given two strings, determine if they share a common substring. A substring may be as small as one character.
For example, the words "a", "and", "art" share the common substring "a". The words "be" and "cat" do not share a substring.  
[Read the problem in Hacker Rank](https://www.hackerrank.com/challenges/two-strings/problem)
#### Solutions :
  * [TwoStrings.cpp](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/C%2B%2B/TwoStrings.cpp)
---
### Array Manipulation<a name="Array_Manipulation"></a>
#### Challenge :
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.  
[Read the problem in Hacker Rank](https://www.hackerrank.com/challenges/crush/problem)
#### Solutions :
  * [Array Manipulation.cpp](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/C%2B%2B/Array%20Manipulation.cpp)
---
### Super Palindromes<a name="Super_Palindromes"></a>
#### Challenge :
Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.
Now, given two positive integers L and R, return the number of superpalindromes in the inclusive range [L,R]
#### Solutions :
  * [SuperPalindrome.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/SuperPalindrome.py)
---
### Moving Robot<a name="Moving_Robot"></a>
#### Challenge :
On a infinite plane, a robot initially stands at (0,0) and faces north. The robot can recieve one of three insructions:
'G': go straight 1 unit  
'L': turn 90 degrees to the left    
'R': turn 90 degrees to the right  
The robot performs the instructions given in order, and repeats them forever.  
return true if there exists a circle, in the plane such that the robot never leaves the circle.   
Input: "GGLLGG"  
Ouput: true  
#### Solutions :
  * [IsLooping.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/IsLooping.py)
---

### Minimum Cost<a name="Minimum_Cost"></a>
#### Challenge :
A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.
#### Solutions :
  * [LowestCost.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/LowestCost.py)
---

### Min Stack<a name="Min_Stack"></a>
#### Challenge :
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#### Solutions :
  * [minStack.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/minStack.py)
---

### Valid Parentheses<a name="Valid_Parentheses"></a>
#### Challenge :
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#### Solutions :
  * [ValidParanthesis.java](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/java/ValidParanthesis.java)
---

### Minimum Number of Swaps to Make the Binary String Alternating<a name="Minimum_Swaps"></a>
#### Challenge :
Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.
The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
Any two characters may be swapped, even if they are not adjacent.
1 <= s.length <= 1000. 
s[i] is either '0' or '1'.
#### Solutions :
  * [minSwaps.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/minSwaps.py)
---


### Sum of All Subset XOR Totals<a name="XOR_Totals"></a>
#### Challenge :
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 
Note: Subsets with the same elements should be counted multiple times.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
1 <= nums.length <= 12.
1 <= nums[i] <= 20
#### Solutions :
  * [subsetXORSum.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/subsetXORSum.py)
---

### Finding Pairs With a Certain Sum<a name="FindSumPairs"></a>
#### Challenge :
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:
Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
Implement the FindSumPairs class:
FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
#### Solutions :
  * [FindSumPairs.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/FindSumPairs.py)
---


### Largest Number<a name="Largest_Number"></a>
#### Challenge :
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.
1 <= nums.length <= 100.
0 <= nums[i] <= 109.
#### Solutions :
  * [Largest_Number.java](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/java/Largest_Number.java)
  * [Largest_Number.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/Largest_Number.py)
---

### Best Team With No Conflicts<a name="Best_Team_With_No_Conflicts"></a>
#### Challenge :
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.
However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.
Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.
#### Solutions :
  * [bestTeamScore.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/bestTeamScore.py)
---

### Longer Contiguous Segments of Ones than Zeros<a name="Ones_than_Zeros"></a>
#### Challenge :
Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.

Constraints:

1 <= s.length <= 100.

s[i] is either '0' or '1'.
#### Solutions :
  * [checkZeroOnes.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/checkZeroOnes.py)
---

### Minimum Speed to Arrive on Time<a name="minSpeedOnTime"></a>
#### Challenge :
You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.
#### Solutions :
  * [minSpeedOnTime.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/minSpeedOnTime.py)
---

### Queue Reconstruction by Height<a name="reconstructQueue"></a>
#### Challenge :
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Constraints:

1 <= people.length <= 2000

0 <= hi <= 106

0 <= ki < people.length

It is guaranteed that the queue can be reconstructed.

#### Solutions :
  * [reconstructQueue.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/reconstructQueue.py)
---

### Smaller Strings<a name="SmallerStrings"></a>
#### Challenge :
You are given an integer K and a string S of length N, consisting of lowercase letters from the first K letters of the English alphabet. Find the number of palindrome strings of length N which are lexicographically smaller than S and consist of lowercase letters from the first K letters of the English alphabet.

A string composed of ordered letters a1,a2,…,an is lexicographically smaller than another string of the same length b1,b2,…,bn if ai<bi, where i is the first index where characters differ in the two strings. For example, the following strings are arranged in lexicographically increasing order: aaa, aab, aba, cab.

A palindrome is a string that is the same written forwards and backwards. For example, anna, racecar, aaa and x are all palindromes, while ab, frog and yoyo are not.

As the number of such strings can be very large, print the answer modulo 10^9+7.

#### Solutions :
  * [SmallerStrings.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/SmallerStrings.py)
---

### Jump Game<a name="JumpGame"></a>
#### Challenge :
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

Constraints:

2 <= s.length <= 105

s[i] is either '0' or '1'.

s[0] == '0'

1 <= minJump <= maxJump < s.length

#### Solutions :
  * [jumpGame.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/jumpGame.py)
  * [jumpGame_topDownDP.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/jumpGame_topDownDP.py)
---


### Top K Frequent Words<a name="topKFrequent"></a>
#### Challenge :
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

#### Solutions :
  * [topKFrequent1.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/topKFrequent1.py)
  * [topKFrequent_Heap1.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/topKFrequent_Heap1.py)
  * [topKFrequent_Heap2.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/topKFrequent_Heap2.py)
  * 
---

### Course Schedule II<a name="Course_Schedule"></a>
#### Challenge :
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

#### Solutions :
  * [findOrder_1.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/findOrder_1.py)
  * [findOrder_dfs.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/findOrder_dfs.py)
  * [findOrder_dfs2.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/findOrder_dfs2.py)
  * 
---

### Redundant Connection<a name="RedundantConnection"></a>
#### Challenge :
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

#### Solutions :
  * [findRedundantConnection.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/findRedundantConnection.py)
---

### Binary Search<a name="BinarySearch"></a>
#### Challenge :
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
#### Solutions :
  * [BinarySearch1.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/BinarySearch1.py)
---

### Merge Sort<a name="MergeSort"></a>
#### Challenge :
Implement merge sort
#### Solutions :
  * [MergeSort.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/MergeSort.py)
---

### Sqrt(x)<a name="Sqrt"></a>
#### Challenge :
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
#### Solutions :
  * [sqrtx.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/sqrtx.py)
---

### Search for a Range<a name="searchRange"></a>
#### Challenge :
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
#### Solutions :
  * [searchRange.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/searchRange.py)
  * [searchRange_BinarySearch.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/searchRange_BinarySearch.py)
---

### First Bad Version<a name="firstBadVersion"></a>
#### Challenge :
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
#### Solutions :
  * [firstBadVersion.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/firstBadVersion.py)
---

### Find Peak Element<a name="findPeakElement"></a>
#### Challenge :
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
#### Solutions :
  * [findPeakElement.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/findPeakElement.py)
  * [findPeakElement.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/findPeakElement2.py)
---

### Reverse Linked List<a name="reverseList"></a>
#### Challenge :
Given the head of a singly linked list, reverse the list, and return the reversed list.
#### Solutions :
  * [reverseList.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/reverseList.py)
---

### Reverse String <a name="reverseString"></a>
#### Challenge :
Write a function that reverses a string. The input string is given as an array of characters s.
#### Solutions :
  * [reverseString.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/reverseString.py)
---

### Swap Nodes in Pairs <a name="swapPairs"></a>
#### Challenge :
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#### Solutions :
  * [swapPairs.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/swapPairs.py)
---

### Fibonacci Number <a name="fib"></a>
#### Challenge :
he Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

#### Solutions :
  * [fib.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/fib.py)
---

### Interleaving String <a name="isInterleave"></a>
#### Challenge :
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

#### Solutions :
  * [isInterleave.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/isInterleave.py)
---


### Merge Two Sorted Lists <a name="mergeTwoLists"></a>
#### Challenge :
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Constraints:

The number of nodes in both lists is in the range [0, 50].

-100 <= Node.val <= 100

Both l1 and l2 are sorted in non-decreasing order.
#### Solutions :
  * [mergeTwoLists.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/mergeTwoLists.py)
---


### Maximum Depth of Binary Tree <a name="maxDepth"></a>
#### Challenge :
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#### Solutions :
  * [maxDepth.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/maxDepth.py)
---

### Factorial <a name="Factorial"></a>
#### Challenge :
Given an integer N, print the factorial of the N (mod 10^9+7).

Input:
First line contains one integer, T, number of test cases.
Each test case contains one integer, N.

Output:
For each test case you need to print the factorial of N (mod 10^9+7).

Constraints:
1<=T<=10^5
1<=N<=10^5


#### Solutions :
  * [Factorial_DP.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/Factorial_DP.py)
---

### Climbing Stairs <a name="climbStairs"></a>
#### Challenge :
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


#### Solutions :
  * [climbStairs_dp.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/climbStairs_DP.py)
  * [climbStairs_recursive.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/climbStairs_recursive.py)
---

### Determine Whether Matrix Can Be Obtained By Rotation <a name="findRotation"></a>
#### Challenge :
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

#### Solutions :
  * [findRotation.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/climbStairs_DP.py)
---

### Reduction Operations to Make the Array Elements Equal <a name="reductionOperations"></a>
#### Challenge :
Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.

#### Solutions :
  * [reductionOperations.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/reductionOperations.py)
---

### Pascal's Triangle II <a name="PascalTriangle"></a>
#### Challenge :
Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.

#### Solutions :
  * [getRow_iter.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/getRow_iter.py)
  * [getRow_recursion.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/getRow_recursion.py)
---
