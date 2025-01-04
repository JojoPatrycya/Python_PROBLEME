import functools


multime = {1,2,3,4,5,6,7,8}

lista_perechi = [(1,2),(3,4)]
lista1 = [{1,2,3},{3,4,5},{4,5,6,7,8}]

def tipar(multime):
    print("{",end="")
    functools.reduce(lambda _,elem: print(str(elem)+ ",",end=""),multime,0)
    print("}",end="")

tipar(multime)

def perechi(lista):
    return functools.reduce(lambda multime,element : multime | {element[0]},lista,set())
print('\n',perechi(lista_perechi))

def partition(functie,multime):
    multime1=functools.reduce(lambda acc,elem : acc | {elem} if functie(elem) else acc,multime,set())

    multime2=functools.reduce(lambda acc,elem : acc | {elem} if not functie(elem) else acc,multime,set())
    return multime1,multime2
print(partition(lambda x : x%2==0,multime))

def reuniune(lista):
    return functools.reduce(lambda multime,elem :  multime | elem,lista,set())
print(reuniune(lista1))

def spargere(nr):
    if nr:
        return {nr%10} | spargere(nr//10)
    else:
        return set()
def reuniune1(multime):
    return functools.reduce(lambda multime,nr: multime | spargere(nr),multime,set())
print(reuniune1( {1234, 123, 127}))

def intersectie(multime):
    return functools.reduce(lambda multime,nr: multime & spargere(nr),multime,spargere(list(multime)[0]))
print(intersectie( {1234, 123, 127}))

   
#Dictionare
dict=[('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]; Output: {'a': 10, 'b': 8, 'c': 2}

def adauga_pereche(dict,pereche):
    cheie,val = pereche
    if cheie in dict.keys():
        dict[cheie] += val
    else:
        dict[cheie] = val
    return dict

def creare_dict(lista):
    return functools.reduce(lambda dictionar,pereche : adauga_pereche(dictionar,pereche),lista,{})

print(creare_dict(dict))

def valore(pereche):
    cheie,val = pereche
    return val
def ad_val(dictionar,conditie):
    cheie,val=pereche
    dictionar

def dict_nou(lista):
    return functools.reduce(lambda dictionarul,val : 
    







    
    
    



    
    
