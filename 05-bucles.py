

# bucle while

limit = 12

counter = 1
while counter < limit:
    print(counter)
    counter = counter + 1


# bucle for

names_i_like = ['Thomson', 'Thompson', 'Haddock', 'Snowy']

for name in names_i_like:
    print(f"I like this name: {name}")



# otro ejemplo con range
num = int(input("Ingresa el número máximo para jugar: "))


for num in range(1,num +1):
    print(num)