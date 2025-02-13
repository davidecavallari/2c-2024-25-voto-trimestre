num1 = int(input("Inserisci primo numero: "))
num2 = int(input("Inserisci secondo numero: "))

if num1 < num2: # devo scambiare num1 con num2
    tempo = num1
    num1 = num2
    num2 = tempo

print("Il maggiore è", num1)
print("Il minore è", num2)