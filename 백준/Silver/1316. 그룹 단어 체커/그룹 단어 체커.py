def is_true(string):
    result = ""
    for i in string:
        if i not in result:
            result = result + i
        else:
            if i != result[-1]:
                return False
            else:
                result = result + i
    return True
 
num = int(input())
count = 0
for i in range(num):
    string = input()
    if is_true(string) == True:
        count = count + 1

print(count)