def div_calc(a,b):
    """
    나누기 연산 함수
    :param a: 분자
    :param b: 분모
    :return: 계산 결과
    """
    return a/b
print(div_calc(15,3))

try:
    expr = input("분자 분모를 입력해 주세요(띄어쓰기로 구분): ").split()
    print(int(expr[0]) /int(expr[1]))
    # print(int(expr[4])) index error
except ValueError as err:
    print(f"숫자만 입력 가능합니다.({err})")
except ZeroDivisionError as err:
    print(f"분모에 0이 올 수 없습니다. ({err})")
except IndexError as err:
    print(f"입력 값의 범위에 문제가 있습니다. ({err})")
except Exception as other:
    print(f"알 수 없는 오류가 발생했습니다. ({other})")
else: #예외가 발생하지 않았을 때 동작
    print('프로그램이 정상적으로 작동했습니다.', end = '\n')
finally: #예외 발생 여부와 관계없이 동작
    print('프로그램 종료')