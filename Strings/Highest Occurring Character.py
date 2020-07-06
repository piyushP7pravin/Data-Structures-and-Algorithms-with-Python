"""
---------------------------------- Highest Occurring Character -------------------------------------

Given a string, S, find and return the highest occurring character present in the given string.
If there are 2 characters in the input string with same frequency, return the character which comes first.

Note : Assume all the characters in the given string are lowercase.

#### Input format :
    String S
#### Output format :
    Highest occurring character

#### Constraints :
    0 <= |S| <= 10^7
    where |S| represents the length of string, S.

#### Sample Input 1:
    abdefgbabfba
#### Sample Output 1:
    b

#### Sample Input 2:
    xy
#### Sample Output 2:
    x
"""

def maxChar(s): 
    freqCount = {} 
    ans = s[0] 
    for char in s: 
        if char in freqCount: 
            freqCount[char] += 1 
            if freqCount[char] > freqCount[ans]: 
                ans = char
        else: freqCount[char] = 1 
    for char in s: 
        if char==ans: 
            return ans 
        if freqCount[char]==freqCount[ans]: 
            return char 
    return ans 

# Main 
s=input() 
print(maxChar(s))