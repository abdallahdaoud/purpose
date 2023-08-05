import turtle

def drawe(shape):
    for drawer in shape: # in this method you can draw many of shapes easily
        if drawer[0] == "f":
            board.forward(drawer[1])
        else:
            board.left(drawer[1])

board = turtle.Turtle()

squar = [["f", 100], ["l", 90], ["f", 100], ["l", 90], ["f", 100], ["l", 90], ["f", 100]] 
complexShape = []

i = 8 # = 360 / 45 # angle is 45
while i > 0:
    complexShape.append(["l", 45])
    complexShape.extend(squar)
    i -= 1

drawe(squar)

board.penup()
board.forward(200)
board.pendown()

drawe(complexShape)
# print(complexShape)

board.penup()
board.backward(500)
board.pendown()


drawer = 360
while drawer >= 0:
    board.forward(3)
    board.right(3)
    drawer -= 3

 
turtle.done()