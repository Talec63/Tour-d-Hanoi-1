def Hanoi(n, dep, inter, arr):
  if n == 0:
    return 0
  else:
    Hanoi(n-1, dep, inter, arr)
    print("Déplacer le disque {} de la tige {} vers la tige {}.".format(n,dep,arr))
    Hanoi(n − 1, dep, inter, arr)

n = 10
dep = "a"
inter = "b"
arr = "c"
print(Hanoi(n, dep, inter, arr))
