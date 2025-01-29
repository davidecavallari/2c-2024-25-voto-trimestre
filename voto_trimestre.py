materia = input("Qual è la materia che detesti di più? ")
voto = int(input("Che voto hai preso alla fine? "))
if voto < 6:
    print("Hai un debito in", materia) # il TAB davanti al print() è obbligatorio!
else:
    print("Tutto a posto in", materia)