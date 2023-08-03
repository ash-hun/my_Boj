def recursion(s, l, r):
    global recur_cnt
    if l >= r:
        recur_cnt += 1
        return 1
    elif s[l] != s[r]:
        recur_cnt += 1
        return 0
    else:
        recur_cnt += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(input())
while N>=1:
    s = input()
    recur_cnt = 0
    returnVal = isPalindrome(s)
    print(returnVal, recur_cnt)
    N-=1