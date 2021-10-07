import turtle   #已解决
k = int(input("请输入棋盘边数："))  #棋盘边
t = turtle.Pen()
n = 20   #每条边距离为10
t.width(3)
t.speed(5)
o = ("red","blue","black","yellow")
for i in range(k): #（）中为所画的边数
    t.goto(0,-i*n)
    t.pendown()
    t.color(o[i%len(o)])  #随机颜色
    t.forward(k*n-n)  #边数*边距-边距，向（）中的距离前进
    t.penup()

t.right(90)  #顺时针旋转

for i in range(k):
    t.goto(i*n,0)
    t.pendown()
    t.color(o[i%len(o)])
    t.forward(k*n-n)
    t.penup()

turtle.done()  #保留运行界面

