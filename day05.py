def calculate_fee(*args):
    """
    놀이공원 요금 계산 프로그램
    :param args: ages(가변 type)
    :return: total fee
    """
    total=0
    for age in args:
        if 19 <= age:
            total = total + 10000
        else:
            total = total + 3000
    return total

print(calculate_fee(20, 20, 25))
print(calculate_fee(15, 20))