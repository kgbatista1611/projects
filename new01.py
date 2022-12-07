import random

fruit = ['banana', 'maçã', 'morango']
x, y, z = fruit
s = 35e10
f = -47e-22
d = 3+5j
k = random.randrange(3,10)

# Teste de condicional
txt = '''Hello, my name is Kleber Batista. I'm from Brazil.
     Me like really study, walk, drink coffee, see the river in my city'''
if 'Argentina' not in txt:
    print("\n No, not 'Argentina' in 'TXT'! \n TXT=", txt, "\n")

# Teste de sciling
new_test = "  Hello, sciling test"
print(new_test[-5:-2], "\n")
print(new_test.split(","), "\n")
print(new_test.replace('H', 'KK'), '\n')
print(new_test.upper(), '\n')
print(new_test.strip(), '\n')
print(new_test.lower(), '\n')
print(new_test[7:15], "\n \n")
print(new_test[:15], "\n \n")


print(k, "\n")
print(d, "\n")
print(f, "\n")
print(x, "\n")
print(s, "\n")
print(z, "\n")

# Aplicando metodo format
age = 36
txt00 = "My name is John, and I am {}"
print(txt00.format(age), "\n")

# Metodo de concatenação
age = int(36)
txt01 = "My name is John, I am " + str(age)
print(txt01, "\n")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))





