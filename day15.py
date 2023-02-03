def find_and_insert_data(friend, k_count):
    findPos = -1
    for i in range(len(katok)):
        pair = katok[i]
        if k_count >= pair[1]:
            findPos = i
            break
    if findPos == -1:
        findPos = len(katok)
    insert_data(findPos, (friend, k_count))

def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 넘어갔습니다")
        return
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

katok = [('서영',200),('예지',150),('예은',90),('서인',30),('성현', 15)]

if __name__ == "__main__":
    while True:
        data = input("추가할 친구--> ")
        count = int(input("카톡 횟수--> "))
        find_and_insert_data(data,count)
        print(katok)




