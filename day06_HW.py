# prob 9.4

class OopsException(Exception):
    pass

Trans = ['bus', 'subway', 'taxi']
ask = input('교통수단 입력 : ')
if ask not in Trans:
    raise OopsException(Trans)
else:
    print("정상 종료")