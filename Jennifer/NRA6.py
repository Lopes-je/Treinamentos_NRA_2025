PA = int(input("Qual o valor da progressão?"))

i = 0 
while i < 11:
    print (i)
    i += PA


resp = int(input("Quer mais sequencias? 1 sim, 0 não."))
if resp == 1:
    while i < 21:
        print (i)
        i += PA 

else:
    print("fim")