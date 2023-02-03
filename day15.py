def find_add_insert_data(pokemon, hp):
    '''
    입력된 데이터가 들어올 위치를 찾아 삽입하는 함수
    :param pokemon: str 포켓몬 이름
    :param hp: int 체력
    :return: void
    '''
    find_pos = -1                   # find_pos에 임의의 초기 값 부여

    for i in range(len(pokemons)):  # pokemons를 하나씩 돌면서
        pair = pokemons[i]          # pair에 할당
        if hp >= pair[1]:           # 만약 매개변수 hp가 현재 pair[0번지,1번지]의 1번지의 값보다 크거나 같으면
            find_pos = i            # find_pos = i
            break                   # 찾았으면 break

    if find_pos == -1:              # 위 for문에서 find_pos를 찾지 못했다면 find_pos == -1 일 것이므로
        find_pos = len(pokemon)     # find_pos는 마지막 위치

    insert_data(find_pos, [pokemon, hp])  #insert_data함수 호출


def insert_data(position, data):
    '''
    data를 지정 위치에 삽입하는 함수
    :param position: int 지정 위치
    :param data: list [pokemon, hp]
    :return: void
    '''
    if position < 0 or position > len(pokemons): #만약 지정 위치가 0보다 작거나 pokemons의 길이보다 길다면
        print("데이터를 삽입할 법위를 벗어났습니다.")  #오류 메세지 출력
        return

    pokemons.append(None)   #마지막 자리에 빈 공간 확보

    for i in range(-1 , position, -1):  # 마지막 위치에서 지정 위치까지 한 단계씩 당기면서
        pokemons[i] = pokemons[i - 1]   # 데이터 한칸 씩 뒤로 이동시키고
        pokemons[i - 1] = None          # 이전 칸 비우기

    pokemons[position] = data           # 새로운 데이터 삽입


#pokemons 초기값 설정
pokemons = [["피카츄", 200], ["파이리", 150], ["꼬부기", 90], ["라이츄", 30], ["버터풀", 15]]


if __name__ == "__main__":
    while True:
        data = input("추가할 포켓몬--> ")
        count = int(input("체력--> "))
        find_add_insert_data(data,count)
        print(pokemons)