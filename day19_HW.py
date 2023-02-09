import tkinter as tk

def Sierpinski(x,y,size):       #시작점의 위치와 한 변의 길이를 매개변수로 받아옴
    if size >= 20:              # 한 변의 길이가 20보다 크다면
        Sierpinski(x,y,size/2)  # 왼쪽 아래 작은 삼각형 재귀
        Sierpinski(x+size/2,y,size/2) # 오른쪽 아래 작은 삼각형 재귀
        Sierpinski(x+size/4, int(y-size*(3**0.5)/4), size/2) # 위쪽 작은 삼각형 재귀
    else:                    #  다각형 그리기 => 세 꼭지점 지정,             채우기 색, 선 색 : 빨강"
        canvas.create_polygon(x,y, x+size,y, x+size/2,y-size*(3**0.5)/2, fill='red', outline = 'red')

wsize = 500   #화면크기

window = tk.Tk() #창 생성
window.title("Sierpinski") # 창 제목 생성
canvas = tk.Canvas(window, height= wsize, width= wsize, bg = 'white')

Sierpinski(wsize/5, wsize/5*4, wsize*2/3)

canvas.pack()
window.mainloop()