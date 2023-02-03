
def print_poly(tx,px):
    '''
    다항식을 format에 맞게 출력하는 함수
    :param tx : 항 차수를 원소로 가지고 있는 리스트
    :param px: 계수를 원소로 가지고 있는 리스트
    :return: 다항식
    '''
    poly_str = "P(x) = "

    for i in range(len(px)):
        term = tx[i]   #항 차수
        coef = px[i]  # 계수

        if i> 0 and coef > 0:
            poly_str = poly_str + "+"
        elif coef == 0:
            continue

        if term == 0:
            poly_str = poly_str + f'{coef}'
        else:
            poly_str = poly_str + f'{coef}x^{term} '


    return poly_str


def calc_poly(xVal, tx, px):
    '''
    다항식의 산술연산을 하는 함수
    :param xVal: int x
    :param tx : 항 차수를 원소로 가지고 있는 리스트
    :param px: 계수를 원소로 가지고 있는 리스트
    :return: 다항식 계산 값
    '''
    return_value = 0

    for i in range(len(px)):
        term = tx[i]
        coef = px[i]  # 계수
        return_value += coef * x_value ** term

    return return_value


## 전역 변수 선언 부분 ##
tx = [300,20,0]
px = [7, -4, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = print_poly(tx,px)
    print(pStr)

    x_value = int(input("X값 입력 : "))

    px_value = calc_poly(x_value, tx,px)
    print(px_value)


