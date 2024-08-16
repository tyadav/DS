def isPallindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPallindrome(s)

if ans:
    print("Yes")
else:
    print("No")