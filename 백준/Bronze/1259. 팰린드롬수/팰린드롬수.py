while True:
    s = input()
    if s=='0':
        break
    tmp = ''.join(reversed(list(s)))
    if s == ''.join(tmp):
        print('yes')
    else:
        print('no')