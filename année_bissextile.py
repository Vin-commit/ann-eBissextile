#!/usr/bin/python3
# coding: utf-8


a = int(input(“Entrez l’année dont on veut savoir si elle est bissextile : “))
 # Placement de cette condition en premier car si a la vérifie alors a vérifie la suivante.
if (a % 400 == 0):
  print (“L’année est bissextile car elle est divisible par 400.”) 
elif (a%4 == 0):
   if (a%100 !=  0):
     print (“L’année est bissextile”)            
   else:
     print(“L’année n’est pas bissextile.”)
else:
   print (“L’année saisie n’est pas bisextile car elle ne vérifie aucune des conditions.”)    
----------------------------------------------------------------------- Résultat ---------------------------------------------------------------------------
  
https://fr.wikipedia.org/wiki/Ann%C3%A9e_bissextile


~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
"factorielle" 9 lines, 210 characters