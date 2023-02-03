pokemons = []  # 빈 배열

def add_data(pokemon):
    pokemons.append(None)      #공간 확보
    #pokemons[len(pokemons) - 1] = pokemon  #마지막 번지에 pokemon추가
    pokemons[-1] = pokemon     #위와 같은 코드

add_data('피카츄')
add_data('라이츄')
add_data('파이리')
add_data('꼬부기')
add_data('이상해')

print(pokemons)