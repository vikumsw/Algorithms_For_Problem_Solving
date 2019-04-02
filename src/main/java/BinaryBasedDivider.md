# Binary Based Divider
### Problem
Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
### Solution
Lets take,  
N as numerator  
D as denominator  
b as coefficient which can take only [0, 1] (binary) values  
Then it is possible come with following equation

N = b<sub>0</sub>2<sup>0</sup>D + 
b<sub>1</sub>2<sup>1</sup>D + 
b<sub>2</sub>2<sup>2</sup>D + ..... +
b<sub>n</sub>2<sup>n</sup>D + remainder

Ex:  
57/5  
57 = 1x5 + 1x10 + 0x20 + 1x40 + 2  
57 = (1<sub>0</sub>)2<sup>0</sup>5 + 
(1<sub>1</sub>)2<sup>1</sup>5 + 
(0<sub>2</sub>)2<sup>2</sup>5 + 
(1<sub>3</sub>)2<sup>3</sup>5 + 2  
57 = (2<sup>0</sup> + 
2<sup>1</sup> + 
0 + 
2<sup>3</sup>)*5 + 2  
57 = (1 + 2 + 0 + 8)*5 + 2

57/5 = (1 + 2 + 0 + 8) + 2/5  
57/5 = 11 + 2/5 -> 11

So dividing logic is based on dissecting numerator into terms of  
D2<sup>0</sup>, D2<sup>1</sup>, D2<sup>2</sup>, ... ,D2<sup>n</sup>  
5,10,20,...,5*2<sup>n</sup>

### Algorithm by example

||||
|---|---|---|
|numerator   | 57 | 0011 1001b|  
|denominator | 5  | 0000 0101b|

#### Identifying largest term
For denominator 5 terms are 5, 10, 20, 40, 80, 160  
For numerator 57 largest term is 40 = 5*2^3

##### Position of most significant bit
57 -> 6  
5 -> 3  
Largest term,  
denominator\*2^(msbPos(numerator) - msbPos(denominator))  
5\*2^(6 - 3)  
5\*2^3 = 40

#### Implementation
Implementation is based on few variables which are initialized as below

|Variable|Initialized with|
|---        |---        |
|remaining  |numerator
|result     |0          |
|iterateCount |most significant bit position difference|
|term | largest possible denominator based term

#### Iteration example
|iterateCount|remaining|term|calc|result|
---|---|---|---|---
3|57|40|40***1** + 17|000 **1**b
2|17|20|20***0** + 17|001 **0**b
1|17|10|10***1** + 7 |010 **1**b
0|7 |5|&nbsp;&nbsp;5***1** + 2  |101 **1**b

So the result is 1011b = 11