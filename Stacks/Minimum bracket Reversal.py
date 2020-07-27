"""
Minimum bracket Reversal

Given a string expression which consists only ‘}’ and ‘{‘. The expression may not be balanced. You need to 
find the minimum number of bracket reversals which are required to make the expression balanced.

Return -1 if the given expression can't be balanced.

#### Input Format :
    String S
#### Output Format :
    Required count

#### Sample Input 1 :
    {{{
#### Sample Output 1 :
    -1

#### Sample Input 2 :
    {{{{}}
#### Sample Output 2 :
    1
"""

def isEmpty(stack) : 
    if len(stack) == 0 : 
        return True 
    else : 
        return False 
        
def getTop(stack) : 
    top = stack.pop() 
    stack.append(top) 
    return top

def countBracketReversals(string) : 
    if len(string) == 0 : 
        return 0 
    if len(string) % 2 != 0 : 
        return -1 # reversal isn't possible 
        
    stack = list()

    for i in range(len(string)) : 
        currentChar = string[i] 
        if currentChar == '{' : 
            stack.append(currentChar) 
        else : 
            # pop if there is a balanced pair 
            if not isEmpty(stack) and getTop(stack) == '{' : 
                stack.pop() 
            else : 
                stack.append(currentChar) 

    count = 0
    # only unbalanced brackets are there in stack now 
    while not isEmpty(stack) : 
        char1 = stack.pop() 
        char2 = stack.pop() 

        # i.e char1 = } and char2 = { then we need to reverse both of them 
        if char1 != char2 : 
            count += 2 

        # if both char1 and char2 are same i.e either the are {{ or }}, then we need only 1 reversal 
        else : 
            count += 1 
    return count

#main 
string = input().strip() 
print(countBracketReversals(string))