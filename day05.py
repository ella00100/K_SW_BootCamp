import random
def calculate_fee3(args):   #매개변수를 리스트로 받음
    """
    놀이공원 요금 계산 프로그램 vr.3
    :param args: ages in list
    :return: [total fee, adults, children]  #반환 값 리스트로
    """
    total_fee= 0
    adults = 0
    children = 0
    for age in args:
        if 19 <= age:
            adults += 1
            total_fee = total_fee + 10000
        else:
            children += 1
            total_fee = total_fee + 3000
    return dict(total_c=len(args), adult_c = adults, child_c =children, total_f = total_fee)

no_of_visitor = int(input("몇 분이세요?"))
ages = [random.randint(1,60) for age in range(no_of_visitor)]
results = dict(calculate_fee3(ages))

print(f'총 {results["total_c"]}분이서 방문하셨고 어른 {results["adult_c"]}명, 아이 {results["child_c"]}명, 총 요금은 {results["total_f"]}원 입니다.')
