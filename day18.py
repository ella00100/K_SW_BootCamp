def count_down(n):
    if n == 0:
        print('발사!')
    else:
        print(n)
        count_down(n-1)
count_down(5)

def print_star(n):
    if n>0:
        print_star(n-1)
        print("★"*n)
print_star(5)