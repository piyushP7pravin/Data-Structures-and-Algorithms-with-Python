""" ------------------------------- Check Permutation -------------------------------------

Given two strings, S and T, check if they are permutations of each other. Return true or false.
Permutation means - length of both the strings should same and should contain same set of characters. 
Order of characters doesn't matter.

#### Note : Input strings contain only lowercase english alphabets.

#### Input format :
    Line 1 : String 1
    Line 2 : String 2

#### Output format :
    'true' or 'false'

#### Constraints :
    0 <= |S| <= 10^7
    0 <= |T| <= 10^7
    where |S| represents the length of string, S.

#### Sample Input 1 :
    abcde
    baedc
#### Sample Output 1 :
    true

#### Sample Input 2 :
    abc
    cbd
#### Sample Output 2 :
    false
"""

def permutation(s1, s2): 
    freqCount = {} 
    for char in s1: 
        if char in freqCount:
             freqCount[char] += 1 
        else: 
            freqCount[char] = 1 
    for char in s2: 
        if char in freqCount: 
            if freqCount[char]==1: 
                del freqCount[char] 
            else: 
                freqCount[char] -= 1 
        else: 
            return False 
    if freqCount: 
        return False 
    return True 
# Main 
s1=input() 
s2=input() 
if permutation(s1, s2): 
    print('true') 
else: 
    print('false')

"""s1=input()
s2=input()
if len(s1)!=len(s2):
    print("false")
else:
    fa=[0]*256
    for i in s1:
        fa[ord(i)]+=1
    for i in s2:
        fa[ord(i)]-=1
    for i in fa:
        if i!=0:
            print("false")
            break
    else:
        print("true")
"""

'''
if len(s1)!=len(s2):
    print("false")
else:
    count=0
    for i in s1:
        for j in s2:
            if i==j:
                count+=1
                s2=s2.replace(j,".",1)
                break
    if count==len(s1):
        print("true")
    else:
        print("false")
'''