"""
----------------------------------------- Reverse Each Word ----------------------------------------------

Given a string S, reverse each word of a string individually. For eg. if a string is "abc def", 
reversed string should be "cba fed".

#### Input Format :
    String S
#### Output Format :
    Modified string

#### Constraints :
    0 <= |S| <= 10^7
    where |S| represents the length of string, S.

#### Sample Input 1:
    Welcome to Coding Ninjas
#### Sample Output 1:
    emocleW ot gnidoC sajniN

#### Sample Input 2:
    Give proper names to variables and functions
#### Sample Output 2:
    eviG reporp seman ot selbairav dna snoitcnuf
"""
def reverse(s): 
    ans = '' 
    for char in s: 
        ans = char + ans 
    return ans 

def reverseEachWord(s): 
    length = len(s) 
    index=0 
    while index<length: 
        if s[index] in ' \t\n': 
            index += 1 # Ignore white spaces 
        else: 
            start = index # Start of word found 
            index += 1 
            while index<length and s[index] not in ' \t\n': 
                index += 1 
            s = s[:start] + reverse(s[start:index]) + s[index:] 
    return s 
# Main 
s=input() 
print(reverseEachWord(s))