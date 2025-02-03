# Voto trimestre
## Descrizione
Realizziamo un programma che chieda in input:
1. La nostra materia peggiore
2. Il voto in quella materia a fine periodo

e ci scriva in output se abbiamo un debito oppure no in quella materia a fine periodo.
## Diagramma di flusso
L'algoritmo che andremo a implementare ha questa forma:

![Diagramma di flusso dell'algoritmo](diagramma-flusso-voto.jpg)
## Codifica Python
Implementiamo l'algoritmo per mezzo del linguaggio di programmazione Python.
```
materia = input("Qual è la materia che detesti di più? ")
voto = int(input("Che voto hai preso alla fine? "))
if voto < 6:
    print("Hai un debito in", materia) # il TAB davanti al print() è obbligatorio!
else:
    print("Tutto a posto in", materia)
```



