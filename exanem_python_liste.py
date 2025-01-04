lista=[11,22,30,45,23]

##Să se sorteze o listă care conține numere întregi în funcție de ultima cifră a numărului ( în ordine crescătoare a ultimei cifre din număr).

def ultima(x):
    if(x):
        return x%10

lista.sort(key=ultima)
print(lista)


#Implementați funcția nth care returnează al n-lea element dintr-o listă.

def nth(n,lista):
    return lista[n-1]

print(nth(2,lista))


# Implementați o funcție firstn care returnează o listă cu primele n elemente dintr-o listă dată.

def firstn(n,lista):
    return lista[:n]

print(firstn(2,lista))


#Implementați folosind reduce o funcție countif care ia ca parametru o funcție f cu valori boolene și o listă și returnează numărul de elemente pentru care funcția f e adevărată.

import functools

def par(x,y):
    if(y%2==0):
        return x+1
    else:
        return x

def countif(par,lista):
    print(functools.reduce(par,lista,0)) #print(functools.reduce(lambda x,y: x+1 if(par(y)) else x,lista,0)

countif(par,lista)


#Implementați similar o funcție sumif care calculează suma tuturor elementelor (presupuse întregi) pentru care funcția f e adevărată.

import functools

def cifre(x):
    if((x//10)%10==2):
        return x



def sumif(cifra,lista):
    print(functools.reduce(lambda x,y: x+y if cifre(y) else x,lista,0))

sumif(cifre,lista)


#Scrieți o funcție care ia o listă de cifre și returnează valoarea numărului cu cifrele respective.

lista1=[1,2,3,4]

def functie(p,lista1):
    if(len(lista1)>0):
        p= p*10+lista1[0]
        return functie(p,lista1[1:])
    else:
        return p

print(functie(0,lista1))


#Scrieți o funcție care ia o listă de cifre și returnează valoarea numărului cu cifrele respective in ordinea inversa.

def functie(p,lista1):
    if(len(lista1)>0):
        p= p*10+lista1[-1]
        return functie(p,lista1[:-1])
    else:
        return p

print(functie(0,lista1))


#Scrieți o funcție care ia o listă de cifre și returnează valoarea numărului format cu cifrele aflate pe pozitii pare , in ordinea aparitiei lor

lista2=[1,2,3,4,5,6,7]

def functie2(a,nr,lista2):
    if(len(lista2)>0):
        if(a%2==0):
            nr=nr*10+lista2[0]
            functie2(a+1,nr,lista2[1:])
        else:
            functie2(a+1,nr,lista2[1:])
    else:
        print(nr)
functie2(0,0,lista2)



