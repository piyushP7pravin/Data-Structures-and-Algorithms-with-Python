""" ---------------------------- Check Palindrome -------------------------------------

Given a String s, check it its palindrome. Return true if string is palindrome, else return false.
Palindrome strings are those, where string s and its reverse is exactly same.

#### Input Format :
        String S

#### Output Format :
        "true" if S is palindrome, else "false"
#### Constraints :
        0 <= |S| <= 10^7
        where |S| represents the length of string, S.

#### Sample Input 1 :
        abcdcba
#### Sample Output 1 :
        true 

#### Sample Input 2 :
    abcd
#### Sample Output 2 :
    false
"""

def checkPalindrome(string) : 
    i = 0 
    j = len(string) - 1 
    while i < j : 
        if string[i] != string[j] : 
            return False 
        i += 1 
        j -= 1 
    return True 
#main 
string = input().strip() 
if checkPalindrome(string) : 
    print('true') 
else : 
    print('false')