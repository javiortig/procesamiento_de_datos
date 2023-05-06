

#### LISTA BASICO
a = [1,"a",True]
b = a # b = a es um puntero  
b = a.copy() # si quiero otra lista es b = a.copy()
b.append(40)

#### CONJUNTO Y DICCIONARIO
c_list = [1,"a",True]
a_set = {1,2,2,1,2,"a",False}
b_dict = {1:"Hi","2":True,"Hola":a_set,2:"asd",3:c_list}
b_dict[3].append(40)
c_list.append(32)

a_int=40
b_dict["Hola"] = "U-TAD"
b_dict["3-s"] = b_dict # Clave es inmutable y el valor es mutable.
# En la clave solo valores escalares, pero True se convierte en 1 y False en 0
# En el valor, cualquier cosa inclusive punteros a cosas raras!

a_set.add(10) #Conjunto es inmutable


#### FUNCIONES Y LA NADA - None es un tipo en python
def func1():
    pass

if func1()==None:
    print("Me ha devuelto la nada!")
else:
    print("Me ha devuelto algo!")
	
	
#### FUNCIONES - PARAMETROS y RETURN VIA TUPLAS. 

d_lista = [1,"a",True]
# En la parte derecha está empaquetando en una tupla.
# En la parte izquierada está desempaquetando de la tupla en variables.
(d_lista[2], d_lista[1], d_lista[0]) = (d_lista[0], d_lista[1], d_lista[2])

d_tupla = (1,"a",True)
d_lista[1] ="listo!"
print(d_lista[1],d_tupla[1])

def func2(x,y,z):
    return(x,y,z)

a,b,c=func2(12,True,"Pepe")
print(a,b,c)



#### FUNCIONES - PARAMETROS DEFAULT - EL ZEN DE PYTHON. 
def func2(y=True,z_lista=[], x=10, nivel_recursion=1):
    if (nivel_recursion<2):
        func2(x,y,z_lista.copy(),nivel_recursion+1)
    d_lista[2] = nivel_recursion
    return(x,y,z_lista)

a,b,c=func2()
print(a,b,c)

a,b,c=func2(True,d_lista.copy(),12,nivel_recursion=0)
print(a,b,c)


#### FUNCIONES - LAMBDA. 
def func1(x,y=10):
    a = 10
    return(x * 2+y+a)

print(func1(20))
lambda_func1 = lambda x,y=10,a=10: x * 2 + y +a
print(lambda_func1(20))


#### LIST COMPRENDIDA. 
collection = [0,1,2,3]
b = list() # b = []
for val in collection:
    if val % 2 == 0:
        b.append(val**2)
    else:
        b.append(val)
    
#[expr for val in collection if condition]

c_list_comprendida = [val**2 for val in collection if val % 2 == 0]
d_list_comprendida = [val**2  if val % 2 == 0 else val for val in collection]
#[expr for val in collection if condition]



	