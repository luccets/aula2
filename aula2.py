var = int(input("digite um numero inteiro maior ou igual a 2: "))
ultimo =1
penultimo = 1
print(ultimo)
print(penultimo)
for a in range(1,var+1,1) :
    fibonacci = ultimo + penultimo
    penultimo = ultimo 
    ultimo = fibonacci
    a += 1
    if fibonacci <= var:
        print(fibonacci)
