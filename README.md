# Algorithms_For_Problem_Solving
Programming Challenges and Solutions for Fun

|   |   |   |   |
|:---:|:---:|:---:|:---:|
|[Count the Islands](#CountTheIslands)|[String of Parentheses](#StringofParentheses)|[Minimum Coins](#Minimum_Coins)|[FindSquare](#FindSquare)|
|[Can you make a palindrome from a given string](#Canyoumakeapalindromefromagivenstring)|[Intersect Area of two Rectangles](#IntersectAreaoftwoRectangles)|[Integer Palindrome Checker](#IntegerPalindromeChecker)| [Stack Using Heap](#StackUsingHeap) |
|[Smallest Sparse Number](#smallestSparseNumber)|  [N<sup>th</sup> Sevenish Number](#Nthsevenishnumber) | -   |  - |

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

