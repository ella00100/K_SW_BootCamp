univ = "Inha University"
print(len(univ)) #길이 구하기 len
print(univ.split()) #문자열 나누기 split

#문자열 추출
print(univ[5:-6])
print(univ[5:])
print(univ[5:15])
print(univ[-10:])
print(univ[::2])
print(univ[0:15:2])

#문자열 합치기  .join
pokemons_list = ['피카츄', '꼬부기', '파이리','이상해씨']
pokemeons_string = ', '.join(pokemons_list)
print(pokemeons_string)

#문자열 교체  .replace
inha = 'a duck goes into a bar'
print(inha.replace('a', 'a famous'))
print(inha.replace('a', 'a famous',1))

#문자열 제거 .strip
subjects = '!   python, data structure, database   !'
print(subjects)
print(subjects.strip('!'))
Oh = 'What the ..!?!'
print(Oh.strip('!?!'))

#문자열 검색
subjects = '$ python, data struct, database    $$$'
print(subjects.find('data'),subjects.index('data'))
print(subjects.rfind('data'),subjects.rindex('data'))
print(subjects.count('data'))
print(subjects.find('inha')) #없으면 -1 출력
# print(subjects.index('inha')) #없으면 오류 발생

#정렬
setup = '안녕하세요'
print(setup.center(30))
print(setup.rjust(30))
print(setup.ljust(30))

