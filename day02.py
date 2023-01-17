a=[]
print(bool(a)) #a가 비어있으니 0 => False출력

a.append(5)
print(bool(a)) #a가 0이 아니므로 1 => True출력

print(bool(set(a)))
print(bool(dict()))