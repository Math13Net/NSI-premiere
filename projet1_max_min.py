# complément de travail autour de l'exercice ce didactique Max_Min
# vu dans le Bloc 1 - Représentation des données - Semaine 1


def val_abs(a):
  """return the number without its sign : always positive"""
  if a >= 0 :
    return a
  else :
    return -a


def min2(a,b):
  """return the lowest number between a and b"""
  if a > b :
    return b
  else :
    return a

def min2_bis(a,b):
  """return the lower number between a and b
  works with val_abs() function
  mininum is the mean of a and b minus half of the distance between them"""
  return 0.5*(a+b) - 0.5*(val_abs(b-a))


def max2(a,b):
  """return the highest number between a and b"""
  if a > b :
    return a
  else :
    return b

def max2_bis(a,b):
  """return the highest number between a and b
  works with val_abs() function
  maximum is the mean of a and b plus half of the distance between them"""
  return 0.5*(a+b) + 0.5*(val_abs(b-a))

def min3(a,b,c):
  """return the lowest number between a, b, c
  uses min2 function"""
  return min2(min2(a,b),c)

def min3_bis(a,b,c):
  """return the lowest number between a, b, c
  works without the function min2()"""
  return min2(min2(a,b),c)
  
def max3(a,b,c):
  """return the highest number between a, b, c
  uses max2 function"""
  return max2(max2(a,b),c)

def max3_bis(a,b,c):
  """return the highest number between a, b, c
  works without the function min2()
  works with the function val_abs()"""
  return 0.5*( a+ 0.5*(b+c+val_abs(b-c)) + val_abs( a - 0.5*(b+c+val_abs(b-c)) )  )

def min3_bis(a,b,c):
  """return the lowest number between a, b, c
  works without the function max2()
  works with the function val_abs()"""
  return 0.5*( a+ 0.5*(b+c-val_abs(b-c)) - val_abs( a - 0.5*(b+c-val_abs(b-c)) )  )

def max_min_3(t,a,b,c):
  """return the maximun or the minimun of 3 figures a, b, c
  uses min2() and max2() function
  use M if u want the maximum
  use m if u want the minimum"""
  if t=="m":
    return min2(min2(a,b),c)
  else :
    return max2(max2(a,b),c)
