"""
--------------------------------------------- Compress the String -----------------------------------------

Write a program to do basic string compression. For a character which is consecutively repeated more than once, 
replace consecutive duplicate occurrences with the count of repetitions.
For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".

Note : Consecutive count of every character in input string is less than equal to 9.

#### Input Format :
    String S
#### Output Format :
    Compressed string 

#### Constraints :
    0 <= |S| <= 10^7
    where |S| represents the length of string, S.

#### Sample Input 1 :
    aaabbccdsa
#### Sample Output 1 :
    a3b2c2dsa

#### Sample Input 2 :
    aaabbcddeeeee
#### Sample Output 2 :
    a3b2cd2e5
"""

def compress(s): 
    ans = s[0] 
    i, length = 1, len(s) 
    while i<length: 
        if ans[-1]==s[i]: 
            count = 2 
            i += 1 
            while i<length and ans[-1]==s[i]: 
                count += 1 
                i += 1 
            ans += str(count) 
        else: 
            ans += s[i] 
            i += 1 
    return ans 
    
# Main 
s=input() 
print(compress(s))
