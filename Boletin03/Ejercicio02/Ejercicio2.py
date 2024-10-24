numC = "502936577942"
nume: int = 502936577942
res: int = 0
contador = 1

for num in numC:
    if contador%2 != 0:
        res+=(nume%10)*3
    else:
        res+=nume%10
    contador+=1
    nume = nume/10

print(int(res))
print(int(res+5))