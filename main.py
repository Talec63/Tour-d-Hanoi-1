import timeit

def Hanoi(n , dep, inter, arr):
    if n==0:
        return 0
    Hanoi(n-1, dep, arr, inter)
    Hanoi(n-1, arr, inter, dep)
    
    
dep = "a"
inter = "b"
arr = "c"
n = 2

print("Déplacer le disque {} de la tige {} vers la tige {}.".format(n,dep,arr))      
Hanoi(n,dep, inter,arr)

#timeit.timeit(Hanoi(n,dep, inter,arr))