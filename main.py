import timeit

def Hanoi(n , dep, inter, arr):
    if n==0:
        return 0
    Hanoi(n-1, dep, arr, inter)
    Hanoi(n-1, arr, inter, dep)
    
    
dep = "a"
inter = "b"
arr = "c"
n = 3

print("Déplacer le disque {} de la tige {} vers la tige {}.".format(n,dep,arr))      
Hanoi(n,dep, inter,arr)

my_setup = "from math import sqrt"
 # snippet of code whose time of execution needs to be measured
my_code = '''
def Hanoi(n , dep, inter, arr):
    if n==0:
        return 0
    Hanoi(n-1, dep, arr, inter)
    Hanoi(n-1, arr, inter, dep)
 '''
my_iterations = 100000
 # timeit function statement
mytime = timeit.timeit(setup = my_setup,
                    stmt = my_code,
                    number = my_iterations)
print(mytime) 