#Binary Based Divider
###Problem
Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
###Solution
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
(0<sub>3</sub>)2<sup>2</sup>5 + 
(1<sub>4</sub>)2<sup>3</sup>5 + 2  
57 = (1 + 2 + 0 + 8)*5 + 2

So result is 1 + 2 + 0 + 8 = 11




