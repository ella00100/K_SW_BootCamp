def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon


def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None

    for i in range(idx + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None

    del (pokemons[len_pokemons - 1])


if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]
    print(pokemons)
    #insert_data(3, '라도란')
    delete_data(1)     #라이츄 삭제
    print(pokemons)
    #insert_data(6, '버터풀')
    delete_data(3)     #이상해 삭제
    print(pokemons)
