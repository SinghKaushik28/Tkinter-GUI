import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Canvas Shapes")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Draw different shapes
canvas.create_line(50, 50, 200, 50, fill="blue", width=3)
canvas.create_rectangle(50, 80, 200, 150, outline="red", width=3, fill="yellow")
canvas.create_oval(50, 180, 200, 300, fill="green")
canvas.create_polygon(300, 100, 350, 50, 400, 100, 375, 150, 325, 150, fill="orange")
canvas.create_arc(220, 200, 350, 350, start=0, extent=180, fill="purple")
canvas.create_text(200, 20, text="Canvas Drawing", font=("Arial", 14, "bold"), fill="black")

root.mainloop()
