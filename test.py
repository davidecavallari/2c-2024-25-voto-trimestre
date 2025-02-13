prodotto1 = float(input("Inserisci l'importo del primo prodotto "))
prodotto2 = float(input("Inserisci l'importo del secondo prodotto "))
if prodotto1<prodotto2:
    spesa = prodotto2 + (prodotto1*0.5)
else:
    spesa = prodotto1 + (prodotto2*0.5)
print("L'importo da pagare alla fine è di", spesa)
print(type(spesa))