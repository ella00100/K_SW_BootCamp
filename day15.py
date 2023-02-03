
def print_poly(px):
    '''
    다항식을 format에 맞게 출력하는 함수
    :param px: 계수를 원소로 가지고 있는 리스트
    :return: 다항식
    '''
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수
        if i> 0 and coef > 0:
            poly_str = poly_str + "+"
        elif coef == 0:
            term = term-1
            continue
        if term == 0:
            poly_str = poly_str + f'{coef}'
        else:
            poly_str = poly_str + f'{coef}x^{term} '
        term = term - 1

    return poly_str


def calc_poly(xVal, px):
    '''
    다항식의 산술연산을 하는 함수
    :param xVal: int x
    :param px: 계수를 원소로 가지고 있는 리스트
    :return: 다항식 계산 값
    '''
    return_value = 0
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = px[i]  # 계수
        return_value += coef * x_value ** term
        term = term - 1

    return return_value


## 전역 변수 선언 부분 ##
px = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = print_poly(px)
    print(pStr)

    x_value = int(input("X값 입력 : "))

    px_value = calc_poly(x_value, px)
    print(px_value)


