"""
-----------------------  Extract Unique characters  ---------------------

Given a string, you need to remove all the duplicates. That means, 
the output string should contain each character only once. The respective 
order of characters should remain same.

#### Input format :
    String S

#### Output format :
    Output String

#### Constraints :
    0 <= Length of S <= 10^8

#### Sample Input 1 :
    ababacd
#### Sample Output 1 :
    abcd

#### Sample Input 2 :
    abcde
#### Sample Output 2 :
    abcde
"""

def uniqueChars(s): 
    ans = '' 
    m = {} 
    for char in s: 
        if char not in m: 
            ans = ans + char 
            m[char] = True 
    return ans 

# Main
string = input()
print(uniqueChars(string))
