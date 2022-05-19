# -*- coding: utf-8 -*-
"""
Created on Thu May 19 03:24:08 2022

@author: carlos
"""

from pyswip import Prolog
prolog =Prolog()

#padres de enrique ,julia, felix 
prolog.assertz("padres(enrique,lidia,hector)")
prolog.assertz("padres(julia,lidia,hector)")
prolog.assertz("padres(felix,lidia,hector)")

#tias y primos
prolog.assertz("padres(marco,maria,lucas)")
prolog.assertz("padres(cristina,lucia,alberto)")

# padre: jose,mario, hijos: hector maria lidia

prolog.assertz("papa(hector,jose)")
prolog.assertz("papa(maria,jose)")
prolog.assertz("papa(lidia,mario)")
prolog.assertz("papa(alberto,mario)")
#abuelos y nietos

prolog.assertz("abuelo(A,N):-padres(N,M,P),(papa(M,A);papa(P,A))")

# sus hermanos de mis padres(tias) ,maria ,alberto
prolog.assertz("hermanos(hector,maria)")
prolog.assertz("hermanos(lidia,alberto)")

#primos
prolog.assertz("primos(A,B):-padres(A,M,P),padres(B,M1,P1),(hermanos(M,P1);hermanos(P,M1);hermanos(P,P1))")

#list(prolog.query("padre(juan,X)"))==[{"X": "maria"},{"Y":"julio"}]
print("") 
print("ABUELOS Y SUS NIETOS")
for elemento in prolog.query("abuelo(X,Y)"):
    print(elemento["X"], "es el abuelo de ", elemento["Y"],"soy su nieto")
    
print("")  
print("PRIMOS")    
for elemento in prolog.query("primos(X,Y)"):
    print(elemento["X"], "es el primo de ", elemento["Y"])    
    
    
    
    
    
    
    