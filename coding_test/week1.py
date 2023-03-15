#3
#40 40 40
from sys import stdin

n = int(stdin.readline())
d_time = list(map(int,stdin.readline().split()))
M_fee=Y_fee=0

for time in d_time:
    M_fee += (time//60 +1) * 15
    Y_fee += (time//30 +1) * 10

if M_fee < Y_fee:
    print(f'M {M_fee}')
elif M_fee > Y_fee:
    print(f'Y {Y_fee}')
else:
    print(f'Y M {M_fee}')


