""" -------------------------------- Remove Consecutive Duplicates -------------------------------

Given a string, S, remove all the consecutive duplicates that are present in the given string. That means, if 'aaa' is present in the string then it should become 'a' in the output string.

#### Input format :
    String S
#### Output format :
    Modified string

#### Constraints :
    0 <= |S| <= 10^7
    where |S| represents the length of string, S.

#### Sample Input 1:
    aabccbaa
#### Sample Output 1:
    abcba

#### Sample Input 2:
    xxyyzxx
#### Sample Output 2:
    xyzx
"""

def removeDuplicates(s): 
    index=1 
    while index<len(s): 
        if s[index] == s[index-1]: 
            nextIndex = index+1 
            length = len(s) 
            while nextIndex<length and s[nextIndex]==s[index]: 
                nextIndex += 1 
            s = s[:index] + s[nextIndex:] 
        else: 
            index += 1 
    return s 
# Main 
s1=input() 
print(removeDuplicates(s1))

"""
s=input()
ns=s[0]
for i in s:
    if i!=ns[-1]:
        ns+=i
print(ns)
"""
        
    