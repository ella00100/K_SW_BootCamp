def add_data(pokemon):
    '''
    선형 리스트에 원소 추가
    :param pokemon: int
    :return: void
    '''
    pokemons.append(None)
    pokemons[-1] = pokemon


def insert_data(idx, pokemon):
    '''
    선형 리스트의 idx위치에 원소 삽입
    :param idx: int
    :param pokemon: str
    :return: void
    '''
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon


def delete_data(idx):
    '''
    선형 리스트의 idx위치 원소 삭제
    :param idx: int
    :return: void
    '''
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None

    for i in range(idx + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None

    del (pokemons[len_pokemons - 1])

def delete_alldata(idx):
    '''
    지정위치 이후 모든 데이터 삭제
    :param idx: int
    :return : void
    '''
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None

    for i in range(idx + 1, len_pokemons):
        pokemons[i] = None

    for i in range(idx, len_pokemons):
        pokemons.pop()

pokemons = []
select = -1

if __name__ == "__main__":

    while (select != 4):

        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

        if (select == 1):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif (select == 2):
            idx = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(idx, data)
            print(pokemons)
        elif (select == 3):
            idx = int(input("삭제할 위치--> "))
            delete_data(idx)
            print(pokemons)
        elif (select == 4):
            print(pokemons)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue

