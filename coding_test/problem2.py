
import sys

def find_best_route(route_a, route_b):
    a_dict = {address: idx for idx, address in enumerate(route_a)}
    b_dict = {address: idx for idx, address in enumerate(route_b)}
    overlap = set(a_dict.keys()) & set(b_dict.keys())
    overlap = list(overlap)
    overlap.sort(key=lambda x: (a_dict[x], b_dict[x]))
    return overlap

# 입력 처리
t = int(sys.stdin.readline().strip())

for _ in range(t):
    na, *route_a = map(str, sys.stdin.readline().split())
    nb, *route_b = map(str, sys.stdin.readline().split())

    # 최적 경로 찾기
    overlap = find_best_route(route_a, route_b)
    print(len(overlap))
