#list

score = ('B+', 'A+', 'C+') #튜플 생성
print(score[1], score[2])
temp = list(score)  #리스트로 변환
temp[1] = 'C+'
temp[2] = 'A+'
score = tuple(temp) #다시 튜플로 전환
print(score[1], score[2])

big_bang = ['GD', '태양', '탑', '대성'] #리스트 생성
bts = ['RM', '뷔']
big_bang.append('태진아') #맨 뒤에 항목 추가
print(big_bang)
big_bang.insert(1,'김장훈') #1번 자리에 항목 추가
print(big_bang)
big_bang.remove('김장훈') #항목 지우기
print(big_bang)
bts = bts + big_bang #리스트 합치기
print(bts)
bts.append(big_bang)
print(bts)
print(bts[-1][1]) #태양 출력
print(bts.pop()) #마지막 항목 삭제
print(bts)
print(bts.pop(0)) #첫번째 항목 삭제
print(bts)
del bts[5] #5번 항목 지우기
print(bts)
bts.remove('탑')
print(bts)
