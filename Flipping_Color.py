import turtle
import random as r

# pre-defined variables
# used to find the tile
tile_dict = {}
tile_list = []
# used to find the color
color_dict = {}
color_list = ["red", "yellow", "purple", "#33cc8c", "blue"]
# coordinates of tiles on the board
tile_x_range = [-100.0, -75.0, -50.0, -25.0, 0.0]
tile_y_range = [100.0, 75.0, 50.0, 25.0, 0.0]
# coordinates of color set, y's are the same
color_x_range = [-110.0, -85.0, -60.0, -35.0, -10.0]
color_y = -25.0
# position of clicked tile on the board
pos = [-100.0, 100.0]


# get the tile's position from the event of clicked tile
# regularize the coordinate
def get_pos(x, y):
    for tile_x in tile_x_range:
        if tile_x - 10 <= x <= tile_x + 10:
            pos[0] = tile_x
            break

    for tile_y in tile_y_range:
        if tile_y - 10 <= y <= tile_y + 10:
            pos[1] = tile_y
            break


def change(x, y):
    # get the color's position from the event of clicked color set
    # regularize the x-coordinate
    # color_y is fixed, no need to regularize
    xt = -100.0
    for i in range(0, 5):
        if color_x_range[i] - 10 <= x <= color_x_range[i] + 10:
            xt = color_x_range[i]
            break

    # get the color for change to
    col_ind = color_dict[(xt, color_y)]
    color = color_list[col_ind]
    # get the tile whose color is to change
    # use pos got previously
    tile_ind = tile_dict[(pos[0], pos[1])]
    tile = tile_list[tile_ind]

    search_color = tile.color()  # the relative color to be changed

    # search, for the tile to change color
    queue = [tile]
    # a dict of mapping tile (turtle) to the index of the tile in tile_list (integer)
    tile_index_dict = {tile: tile_ind}
    while queue:
        tmp = queue.pop(0)
        tmp.color(color)  # change color
        # search for the neighbour tiles with the same color
        index = tile_index_dict[tmp]
        row = index // 5
        col = index % 5
        # neighbours
        # judge for not out of bound index
        if row - 1 >= 0:
            neighbour = tile_list[(row - 1) * 5 + col]
            if neighbour.color() == search_color:
                tile_index_dict[neighbour] = (row - 1) * 5 + col
                queue.append(neighbour)
        if row + 1 <= 4:
            neighbour = tile_list[(row + 1) * 5 + col]
            if neighbour.color() == search_color:
                tile_index_dict[neighbour] = (row + 1) * 5 + col
                queue.append(neighbour)
        if col - 1 >= 0:
            neighbour = tile_list[row * 5 + (col - 1)]
            if neighbour.color() == search_color:
                tile_index_dict[neighbour] = row * 5 + (col - 1)
                queue.append(neighbour)
        if col + 1 <= 4:
            neighbour = tile_list[row * 5 + (col + 1)]
            if neighbour.color() == search_color:
                tile_index_dict[neighbour] = row * 5 + (col + 1)
                queue.append(neighbour)

    window.update()  # update the figure


# open a screen
window = turtle.Screen()
window.setup(0.75, 0.75)
window.title("Color Flipping")
window.tracer(0)  # off auto change

# generate the tile board
tur = turtle.Turtle()
tur.shape("square")
tur.color(color_list[r.randint(0, 4)])
tur.penup()
tur.goto(-100, 100)
tur.onclick(get_pos)
# cnt for number of tiles, used for tile_dict
cnt = 0

for rows in range(0, 5):
    ti = tur.clone()
    ti.color(color_list[r.randint(0, 4)])
    ti.penup()
    ti.goto(tur.xcor(), tur.ycor() - rows * 25)
    ti.onclick(get_pos)
    tile_dict[(tur.xcor(), tur.ycor() - rows * 25)] = cnt
    tile_list.append(ti)
    cnt += 1
    for cols in range(1, 5):
        tj = ti.clone()
        ti.color(color_list[r.randint(0, 4)])
        tj.penup()
        tj.goto(ti.xcor() + cols * 25, ti.ycor())
        tj.onclick(get_pos)
        tile_dict[(ti.xcor() + cols * 25, ti.ycor())] = cnt
        tile_list.append(tj)
        cnt += 1

# generate the color set
t = tur.clone()
t.color(color_list[0])
t.penup()
t.goto(tur.xcor() - 10, tur.ycor() - 125)
t.onclick(change)
color_dict[(tur.xcor() - 10, tur.ycor() - 125)] = 0
cnt = 1
for col_num in range(1, 5):
    ti = t.clone()
    ti.color(color_list[col_num])
    ti.penup()
    ti.goto(t.xcor() + col_num * 25, t.ycor())
    ti.onclick(change)
    color_dict[(t.xcor() + col_num * 25, t.ycor())] = cnt
    cnt += 1

window.update()  # update the figure

window.mainloop()  # keep
