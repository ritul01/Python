marks=[90,92,95]
print(marks)

marks=[90,92,95]
print(marks[1])

marks=[90,92,95]
print(marks[1:3])

for score in marks:
    print(score)

marks.append(97)
print(marks)    

marks.insert(0,99)
print(marks)
print(98 in marks)
print(len(marks))

i=0
while i<len(marks):
    print(marks[i])
    i=i+1

marks.clear()    
print(marks)