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
|[-](#-)|[-](#-)|[-](#-)|[-](#-)|

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
1 <= s.length <= 1000
s[i] is either '0' or '1'.
#### Solutions :
  * [minSwaps.py](https://github.com/vikumsw/Algorithms_For_Problem_Solving/blob/master/src/main/python/minSwaps.py)
---
