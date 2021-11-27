import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("미로 찾기 게임")

canvas = Canvas(window, width=700, height=700, bg="#FFF8E5")
canvas.pack()

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

for y in range(14):
    for x in range(14):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50, fill='#C6D57E', outline='white')

x = 0
y = 1

# 플레이어, 도착지점 이미지 넣기
player_img = PhotoImage(file="동글이.png")
player = canvas.create_image(25, 75, image=player_img)

counter=0
for temp_a in maze:
    for temp_b in temp_a:
        if(temp_b==0):
            counter+=1
counter-=1

key_where1=random.randint(0,counter)
key_where2=random.randint(0,counter)
while key_where2==key_where1:
    key_where2=random.randint(0,counter)
key_where3=random.randint(0,counter)
while key_where3==key_where1 or key_where3==key_where2:
    key_where3=random.randint(0,counter)
key_where4=random.randint(0,counter)
while key_where4==key_where1 or key_where4==key_where2 or key_where4==key_where3:
    key_where4=random.randint(0,counter)
key_where5=random.randint(0,counter)
while key_where5==key_where1 or key_where5==key_where2 or key_where5==key_where3 or key_where5==key_where4:
    key_where5=random.randint(0,counter)
counter=0
key_x1=0
key_y1=0
key_x2=0
key_y2=0
key_x3=0
key_y3=0
key_x4=0
key_y4=0
key_x5=0
key_y5=0
print(counter)
print(key_where1)
print(key_where2)
print(key_where3)
print(key_where4)
print(key_where5)
for temp_a in range(len(maze)):
    for temp_b in range(len(maze[temp_a])):
        if(maze[temp_a][temp_b]==0):
            if(counter==key_where1):
                maze[temp_a][temp_b]=3
                key_y1=temp_b
                key_x1=temp_a
            if(counter==key_where2):
                maze[temp_a][temp_b]=4
                key_y2=temp_b
                key_x2=temp_a
            if(counter==key_where3):
                maze[temp_a][temp_b]=5
                key_y3=temp_b
                key_x3=temp_a
            if(counter==key_where4):
                maze[temp_a][temp_b]=6
                key_y4=temp_b
                key_x4=temp_a
            if(counter==key_where5):
                maze[temp_a][temp_b]=7
                key_y5=temp_b
                key_x5=temp_a
            counter+=1
score=0
cost=100


key_img=PhotoImage(file="열쇠.png")
key1 = canvas.create_image(25+(key_y1)*50, 25+(key_x1)*50, image=key_img,tags='gold_key1')
key2 = canvas.create_image(25+(key_y2)*50, 25+(key_x2)*50, image=key_img,tags='gold_key2')
key3 = canvas.create_image(25+(key_y3)*50, 25+(key_x3)*50, image=key_img,tags='gold_key3')
key4 = canvas.create_image(25+(key_y4)*50, 25+(key_x4)*50, image=key_img,tags='gold_key4')
key5 = canvas.create_image(25+(key_y5)*50, 25+(key_x5)*50, image=key_img,tags='gold_key5')
print(maze)
# img_end = PhotoImage(file="공주.png")
# end = canvas.create_image(455, 105, image=img_end)

canvas.create_text(350,25, text=str(score) + '점  남은 횟수:'+str(cost), font=('나눔고딕', 30), fill='white', tags='score')
# 방향키 조작

def player_move(event):
    global x, y,cost,score
    if event.keysym == "Up" and maze[y - 1][x] != 1:
        canvas.move(player, 0, -50)
        y -= 1
        cost-=1
        canvas.delete('score')
        canvas.create_text(350,25, text=str(score) + '점  남은 횟수:'+str(cost), font=('나눔고딕', 30), fill='white', tags='score')
        if(cost<0):
            messagebox.showinfo("미션 실패!","실패!")
    elif event.keysym == "Down" and maze[y + 1][x] != 1:
        canvas.move(player, 0, 50)
        y += 1
        cost -= 1
        canvas.delete('score')
        canvas.create_text(350,25, text=str(score) + '점  남은 횟수:' + str(cost), font=('나눔고딕', 30), fill='white', tags='score')
        if (cost < 0):
            messagebox.showinfo("미션 실패!","실패!")
    elif event.keysym == "Left" and maze[y][x - 1] != 1:
        canvas.move(player, -50, 0)
        x -= 1
        cost -= 1
        canvas.delete('score')
        canvas.create_text(350,25, text=str(score) + '점  남은 횟수:' + str(cost), font=('나눔고딕', 30), fill='white', tags='score')
        if (cost < 0):
            messagebox.showinfo("미션 실패!","실패!")
    elif event.keysym == "Right" and maze[y][x + 1] != 1:
        canvas.move(player, 50, 0)
        x += 1
        cost -= 1
        canvas.delete('score')
        canvas.create_text(350,25, text=str(score) + '점  남은 횟수:' + str(cost), font=('나눔고딕', 30), fill='white', tags='score')
        if (cost < 0):
            messagebox.showinfo("미션 실패!","실패!")
    if maze[y][x] == 2:
        if score<5:
            messagebox.showinfo("","열쇠가 더 필요합니다!")
        else:
            messagebox.showinfo("미션 성공!", "축하합니다!")
    if maze[y][x]==3:
        print("안녕하세요?")
        maze[y][x]=0
        canvas.delete('gold_key1')
        canvas.delete('score')
        score+=1
        cost -= 1
        canvas.delete('score')
        canvas.create_text(350,25, text=str(score) + '점  남은 횟수:' + str(cost), font=('나눔고딕', 30), fill='white', tags='score')
    if maze[y][x]==4:
        print("안녕하세요?")
        maze[y][x]=0
        canvas.delete('gold_key2')
        canvas.delete('score')
        score+=1
        cost -= 1
        canvas.delete('score')
        canvas.create_text(350,25, text=str(score) + '점  남은 횟수:' + str(cost), font=('나눔고딕', 30), fill='white', tags='score')
    if maze[y][x]==5:
        print("안녕하세요?")
        maze[y][x]=0
        canvas.delete('gold_key3')
        canvas.delete('score')
        score+=1
        cost -= 1
        canvas.delete('score')
        canvas.create_text(350,25, text=str(score) + '점  남은 횟수:' + str(cost), font=('나눔고딕', 30), fill='white', tags='score')
    if maze[y][x]==6:
        print("안녕하세요?")
        maze[y][x]=0
        canvas.delete('gold_key4')
        canvas.delete('score')
        score+=1
        cost -= 1
        canvas.delete('score')
        canvas.create_text(350,25, text=str(score) + '점  남은 횟수:' + str(cost), font=('나눔고딕', 30), fill='white', tags='score')
    if maze[y][x]==7:
        print("안녕하세요?")
        maze[y][x]=0
        canvas.delete('gold_key5')
        canvas.delete('score')
        score+=1
        cost -= 1
        canvas.delete('score')
        canvas.create_text(350,25, text=str(score) + '점  남은 횟수:' + str(cost), font=('나눔고딕', 30), fill='white', tags='score')

canvas.bind_all("<KeyPress>", player_move)

canvas.mainloop()
