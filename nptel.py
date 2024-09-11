def insert(L,x):
    sorted_L=L[:]

for i in range(len(sorted_L)):
    if sorted_L[i]>x:
        sorted_L.insert(i,x)
        return sorted_L
    
sorted_L.append(x)
return sorted_L