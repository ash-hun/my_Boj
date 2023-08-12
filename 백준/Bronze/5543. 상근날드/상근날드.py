burger = []
drink = []
res = 4000
for i in range(3):
    a = input()
    burger.append(int(a))

for j in range(2):
    b = input()
    drink.append(int(b))

for A in range(3):
    for B in range(2):
        sett = burger[A] + drink[B] - 50
        if(res>sett):
            res = sett

print(res)