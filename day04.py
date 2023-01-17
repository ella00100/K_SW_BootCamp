#dictionary
students = {'name':'Ella', 'age': 23, 'eyes': [0.9, 1.1]}

for k in students:  #default로 key를 출력
    print(k)
print("\n")

for k in students.keys(): #key 출력 .keys
    print(k)
print("\n")

for k in students.values(): #value 출력  .values
    print(k)
print("\n")

for k, v in students.items(): #key와 value 출력 .items
    print(f'{k} : {v}')
print("\n")

#dictionary[key][위치]
print(f'이름은 {students["name"]}, 나이는 {students["age"]}세', end = "\n")
print(f'시력은 좌 : {students["eyes"][0]}, 우 : {students["eyes"][1]}')