def affichage(tours) :
  d = len(tours[’départ’])
  i = len(tours[’intermédiaire’])
  a = len(tours[’arrivée’])
hauteur = max(d, i, a)
for h in range(hauteur, 0, -1) :
if d >= h : print( tours[’départ’][h-1], end=’ ’)
else : print(’ ’, end=’ ’)
if i >= h : print( tours[’intermédiaire’][h-1], end=’ ’)
else : print(’ ’, end=’ ’)
if a >= h : print( tours[’arrivée’][h-1])
else : print(’ ’)
print(’\u2AE0 \u2AE0 \u2AE0’)
print(’---------------------------------------------------------------’)