marks=(90,92,94,94,95)
person="ram","shyam","singh"

print(marks.count(94))
print(marks.index(92))

#sets

marsks={90,92,94,94,95}
#print(marks)

for score in marks:
    print(score)

#dictionary

marks={"english":90,"maths":98}    
print(marks["maths"])
marks["english"]=94
print(marks)