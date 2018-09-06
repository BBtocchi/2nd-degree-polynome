#-*-coding:UTF-8*

def racine(a, b, c):
  '''
  Programme qui calcule les racines d'un polynome du second degrés.
  Params :
  a -- premier coefficient du polynome (x)
  b -- deuxième coefficient du polynome (x^2)
  c -- troisième coefficient du polynome (constant)
  '''

  # on importe la fonction racine carré
  from math import sqrt
  i = 0
  delta = b^2-4*a*c #calcul de delta
  delta = int(delta)
  print("delta vaut ",delta)
  
  # on calcule les racines
  if delta == 0:
    print("il existe une unique solution, et elle vaut, ",-b/2*a)
  elif delta > 0:
    print("il existe deux solutions dans le domaine du reel, ces solutions sont: ")
    print("r1 = ", (-b-sqrt(delta))/2*a)
    print("r2 = ", (-b+sqrt(delta))/2*a)
  else:
    print("il existe deux solutions complexes")
    delta=complex(delta)
    print("delta vaut ",delta)
    print("r1 = ", (-b-sqrt(delta))/2*a)
    print("r2 = ", (-b+sqrt(delta))/2*a)


