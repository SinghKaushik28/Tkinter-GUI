# import tkinter as tk
# import random as rd

# root = tk.Tk()
# root.title("Canvas Animation")

# canvas = tk.Canvas(root, width=400, height=300, bg="light green")
# canvas.pack()

# ball = canvas.create_oval(50, 50, 80, 80, fill="orange")
# dx, dy = 2, 2  # Speed

# def move_ball():
#     global dx, dy,ball
#     computer=rd.choice(["red","green","blue","black","grey","violet","neon pink","pink"])
#     canvas.move(ball, dx, dy)
#     x1, y1, x2, y2 = canvas.coords(ball)

#     # Bounce off walls
#     if x1 <= 0 or x2 >= 400:
#         dx = -dx
#         canvas.itemconfig(ball, fill=computer)
#     if y1 <= 0 or y2 >= 300:
#         dy = -dy
#         canvas.itemconfig(ball, fill=computer)

#     root.after(20, move_ball)  # Call function every 20ms


# move_ball()  # Start animation
# root.mainloop()

#for many ball
import tkinter as tk
import random as rd

root = tk.Tk()
root.title("Canvas Animation")

canvas = tk.Canvas(root, width=400, height=300, bg="light green")
canvas.pack()

ball = canvas.create_oval(50, 50, 80, 80, fill="orange")
dx, dy = 3,3
ball1 = canvas.create_oval(50, 50, 80, 80, fill="orange")
dx1, dy1 = 1,1
ball2 = canvas.create_oval(50, 50, 80, 80, fill="orange")
dx2, dy2 = 4,4
ball3 = canvas.create_oval(50, 50, 80, 80, fill="orange")
dx3, dy3 = 2, 2  # Speed

def move_ball():
    global dx, dy, dx1, dy1, dx2, dy2, dx3, dy3
    computer=rd.choice(["red","green","blue","black","grey","violet","light blue","pink"])
    canvas.move(ball, dx, dy)
    canvas.move(ball1, dx1, dy1)
    canvas.move(ball2, dx2, dy2)
    canvas.move(ball3, dx3, dy3)

    x1, y1, x2, y2 = canvas.coords(ball)
    x1_1, y1_1, x2_1, y2_1 = canvas.coords(ball1)
    x1_2, y1_2, x2_2, y2_2 = canvas.coords(ball2)
    x1_3, y1_3, x2_3, y2_3 = canvas.coords(ball3)
    # Bounce off walls
    if x1 <= 0 or x2 >= 400:
        dx = -dx
        canvas.itemconfig(ball, fill=computer)
    if y1 <= 0 or y2 >= 300:
        dy = -dy
        canvas.itemconfig(ball, fill=computer)

    if x1_1 <= 0 or x2_1 >= 400:
        dx1 = -dx1
        canvas.itemconfig(ball1, fill=computer)
    if y1_1 <= 0 or y2_1 >= 300:
        dy1 = -dy1
        canvas.itemconfig(ball1, fill=computer)

    if x1_2 <= 0 or x2_2 >= 400:
        dx2 = -dx2
        canvas.itemconfig(ball2, fill=computer)
    if y1_2 <= 0 or y2_2 >= 300:
        dy2 = -dy2
        canvas.itemconfig(ball2, fill=computer)

    if x1_3 <= 0 or x2_3 >= 400:
        dx3 = -dx3
        canvas.itemconfig(ball3, fill=computer)
    if y1_3 <= 0 or y2_3 >= 300:
        dy3 = -dy3
        canvas.itemconfig(ball3, fill=computer)

    root.after(20, move_ball)  # Call function every 20ms


move_ball()  # Start animation
root.mainloop()

#many balls with speed control 
# import tkinter as tk
# import random as rd

# root = tk.Tk()
# root.title("Canvas Animation")

# canvas = tk.Canvas(root, width=400, height=300, bg="light green")
# canvas.pack()

# ball = canvas.create_oval(50, 50, 80, 80, fill="orange")
# dx, dy = 3, 3
# ball1 = canvas.create_oval(50, 50, 80, 80, fill="orange")
# dx1, dy1 = 1, 1
# ball2 = canvas.create_oval(50, 50, 80, 80, fill="orange")
# dx2, dy2 = 4, 4
# ball3 = canvas.create_oval(50, 50, 80, 80, fill="orange")
# dx3, dy3 = 2, 2  # Speed

# # Initial speed
# speed = [20, 20, 20, 20]  # interval time for root.after (lower is faster)

# # Function to increase speed (decrease the interval)
# def increase_speed(ball_num):
#     global speed
#     if speed[ball_num] > 5:  # Limit the minimum speed
#         speed[ball_num] -= 5  # Decrease interval (faster movement)
#     print(f"Ball {ball_num + 1} speed after increase: {speed[ball_num]}")

# # Function to decrease speed (increase the interval)
# def decrease_speed(ball_num):
#     global speed
#     if speed[ball_num] < 100:  # Limit the maximum speed
#         speed[ball_num] += 5  # Increase interval (slower movement)
#     print(f"Ball {ball_num + 1} speed after decrease: {speed[ball_num]}")

# # Create "+" and "-" buttons for controlling speed
# btn_increase_1 = tk.Button(root, text="+ Ball 1", command=lambda: increase_speed(0))
# btn_increase_1.pack(side="left", padx=10)

# btn_decrease_1 = tk.Button(root, text="- Ball 1", command=lambda: decrease_speed(0))
# btn_decrease_1.pack(side="left", padx=10)

# btn_increase_2 = tk.Button(root, text="+ Ball 2", command=lambda: increase_speed(1))
# btn_increase_2.pack(side="left", padx=10)

# btn_decrease_2 = tk.Button(root, text="- Ball 2", command=lambda: decrease_speed(1))
# btn_decrease_2.pack(side="left", padx=10)

# btn_increase_3 = tk.Button(root, text="+ Ball 3", command=lambda: increase_speed(2))
# btn_increase_3.pack(side="left", padx=10)

# btn_decrease_3 = tk.Button(root, text="- Ball 3", command=lambda: decrease_speed(2))
# btn_decrease_3.pack(side="left", padx=10)

# btn_increase_4 = tk.Button(root, text="+ Ball 4", command=lambda: increase_speed(3))
# btn_increase_4.pack(side="left", padx=10)

# btn_decrease_4 = tk.Button(root, text="- Ball 4", command=lambda: decrease_speed(3))
# btn_decrease_4.pack(side="left", padx=10)

# def move_ball_1():
#     global dx, dy
#     computer = rd.choice(["red", "green", "blue", "black", "grey", "violet", "light blue", "pink"])
#     canvas.move(ball, dx, dy)
#     x1, y1, x2, y2 = canvas.coords(ball)
    
#     # Bounce off walls
#     if x1 <= 0 or x2 >= 400:
#         dx = -dx
#         canvas.itemconfig(ball, fill=computer)
#     if y1 <= 0 or y2 >= 300:
#         dy = -dy
#         canvas.itemconfig(ball, fill=computer)
    
#     # Schedule the next movement
#     root.after(speed[0], move_ball_1)

# def move_ball_2():
#     global dx1, dy1
#     computer = rd.choice(["red", "green", "blue", "black", "grey", "violet", "light blue", "pink"])
#     canvas.move(ball1, dx1, dy1)
#     x1_1, y1_1, x2_1, y2_1 = canvas.coords(ball1)
    
#     # Bounce off walls
#     if x1_1 <= 0 or x2_1 >= 400:
#         dx1 = -dx1
#         canvas.itemconfig(ball1, fill=computer)
#     if y1_1 <= 0 or y2_1 >= 300:
#         dy1 = -dy1
#         canvas.itemconfig(ball1, fill=computer)
    
#     # Schedule the next movement
#     root.after(speed[1], move_ball_2)

# def move_ball_3():
#     global dx2, dy2
#     computer = rd.choice(["red", "green", "blue", "black", "grey", "violet", "light blue", "pink"])
#     canvas.move(ball2, dx2, dy2)
#     x1_2, y1_2, x2_2, y2_2 = canvas.coords(ball2)
    
#     # Bounce off walls
#     if x1_2 <= 0 or x2_2 >= 400:
#         dx2 = -dx2
#         canvas.itemconfig(ball2, fill=computer)
#     if y1_2 <= 0 or y2_2 >= 300:
#         dy2 = -dy2
#         canvas.itemconfig(ball2, fill=computer)
    
#     # Schedule the next movement
#     root.after(speed[2], move_ball_3)

# def move_ball_4():
#     global dx3, dy3
#     computer = rd.choice(["red", "green", "blue", "black", "grey", "violet", "light blue", "pink"])
#     canvas.move(ball3, dx3, dy3)
#     x1_3, y1_3, x2_3, y2_3 = canvas.coords(ball3)
    
#     # Bounce off walls
#     if x1_3 <= 0 or x2_3 >= 400:
#         dx3 = -dx3
#         canvas.itemconfig(ball3, fill=computer)
#     if y1_3 <= 0 or y2_3 >= 300:
#         dy3 = -dy3
#         canvas.itemconfig(ball3, fill=computer)
    
#     # Schedule the next movement
#     root.after(speed[3], move_ball_4)

# # Start the individual ball movements
# move_ball_1()
# move_ball_2()
# move_ball_3()
# move_ball_4()

# root.mainloop()
