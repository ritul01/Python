A=input()
ans=str()
for i in A:
  if i.islower():
    if i=='a':
      ans+='y'
    elif i=='b':
      ans+='z'
    else:
      ans+=chr(ord(i)-2)
  elif i.isupper():
    if i=='A':
      ans+='X'
    elif i=='B':
      ans+='Y'
    elif i=='C':
      ans+='Z'
    else:
      ans+=chr(ord(i)-3)
  elif i.isspace() or i.isnumeric():
      ans+=i
  print(ans,end="")