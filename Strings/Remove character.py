"""
---------------------------------------  Remove character  ---------------------------------------------

Given a string and a character x. Write a function to remove all occurrences of x character from the given string.
Leave the string as it is, if the given character is not present in the string.

#### Input Format :
    Line 1 : String S
    Line 2 : Character c
#### Output Format :
    Modified string

#### Constraints :
    0 <= |S| <= 10^7
    where |S| represents the length of string, S.

#### Sample Input 1:
    welcome to coding ninjas
    o
#### Sample Output 1:
    welcme t cding ninjas

Sample Input 2:
    Think of edge cases before submitting solutions
    x
Sample Output 2:
    Think of edge cases before submitting solutions
"""

def removeChar(s, character): 
    ans = ""
    for char in s: 
        if char == character: 
            continue 
        ans += char 
    return ans 

# Main 
s=input() 
character=input() 
print(removeChar(s, character))