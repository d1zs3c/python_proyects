
frase1 = input("Introduce una frase palidroma: ").lower()

frase2 = frase1.replace(" ", "")
frase3 = frase2[::-1]

if frase2 == frase3:
    print("Es una frase palindroma.", frase1, "es lo mismo que", frase3)
else:
    print("No es palindromo")