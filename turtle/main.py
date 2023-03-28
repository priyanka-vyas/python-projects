#####Turtle Intro######

# import turtle as t
# import random
# t.colormode(255)
#
# #colors = ["red", "blue", "green", "yellow", "black", "grey", "purple", "pink", "orange", "brown"]
# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
#


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
#
# timmy_the_turtle.speed(8)
#
# for i in range (0,72):
#     ran_color = random_color()
#     timmy_the_turtle.color(ran_color)
#     timmy_the_turtle.circle(100)
#     current_heading=timmy_the_turtle.heading()
#     timmy_the_turtle.setheading(current_heading+5)
# timmy_the_turtle.circle(100)
#



# timmy_the_turtle.pensize(10)
# # for side in range(3, 11):
#
# timmy_the_turtle.speed(8)
#
# for i in range(0, 200):
#     c = random.choice(colors)
#     timmy_the_turtle.color(c)
#     n = random.randint(0, 2)
#     angle = random.randint(0, 2)
#     if n == 0:
#         timmy_the_turtle.forward(20)
#     elif n == 1:
#         timmy_the_turtle.backward(20)
#     if angle == 0:
#         timmy_the_turtle.left(90)
#     elif angle == 1:
#         timmy_the_turtle.right(90)
# c = random.choice(colors)
#     print(c)
#     colors.remove(c)
#     timmy_the_turtle.color(c)
#     angle = 360 / side
#     for i in range(0, side):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)




# import colorgram
# colors = colorgram.extract('D.jfif', 100)
# rgb_colors=[]
# print(colors)
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append((new_color))
#
# print(rgb_colors)
# for i in range(0,10):
#     for j in range(0,10):
#         c=random.choice(rgb_colors)
#         timmy_the_turtle.dot(20, c)
#         if i%2 == 0:
#             timmy_the_turtle.fd(40)
#         else:
#             timmy_the_turtle.bk(40)
#
#     timmy_the_turtle.right(90)



# timmy_the_turtle.color("black", "red")
# timmy_the_turtle.begin_fill()
# timmy_the_turtle.circle(80)
# timmy_the_turtle.end_fill()




