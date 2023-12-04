import tkinter as tk


def create_grid(root, rows, columns):
    for i in range(rows):
        for j in range(columns):
            label = tk.Label(root, text=f'Row {i+1}\nCol {j+1}', borderwidth=1, relief="solid", width=15, height=5)
            label.grid(row=i, column=j, sticky="nsew")
            label.bind('<Button-1>', lambda event, row=i, col=j: on_label_click(event, row, col))


def on_label_click(event, row, col):
    label = event.widget
    current_color = label.cget("bg")

    new_color = 'blue' if current_color != 'blue' else 'gray20'
    label.configure(bg=new_color)

    state[row][col] = 1 - state[row][col]  # Toggle between 0 and 1
    format_output()


def format_output():
    print("\n\n\nPicture Bits:\n")
    for row in range(8):
        print("0b", end="")
        for col in range(5):
            print(state[row][col],  end="")
        print()


root = tk.Tk()
root.title("Resizable Grid")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(8):
    root.grid_columnconfigure(j, weight=1)

state = [[0 for _ in range(5)] for _ in range(8)]

create_grid(root, 8, 5)

root.mainloop()
