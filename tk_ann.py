import tkinter as tk
import json

d = 110
BIAS = 7
maincolor = 'lightblue'


class MyRoot:

    def __init__(self, root):
        self.root = root
        self.root.title('ANN')
        self.root.configure(bg=maincolor)
        self.frame_figure = tk.Frame(self.root, bg=maincolor, padx=2, pady=2)
        self.frame_figure.grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame_figure, text='Create picture', font='Sens 18 bold', bg=maincolor).pack(pady=5)
        self.frame_number = tk.Frame(self.root, bg=maincolor)
        self.frame_number.grid(row=0, column=1, padx=10, pady=10)

        self.labels_number = []
        for i in range(10):
            self.labels_number.append(tk.Label(self.frame_number, text=i, bd=2, relief="groove", font='Arial 18',
                                               width=2, bg='grey', fg="white"))
            self.labels_number[-1].pack(padx=5, pady=5)

        self.canvas = tk.Canvas(self.frame_figure, height=d*5, width=d*3, bg='black')
        self.canvas.pack()
        self.inputs = [0] * 15
        self.draw()
        self.canvas.bind('<Button-1>', self.click_canvas)
        self.weights = self.get_weights()
        self.label = tk.Label(self.root, text='', width=30, bg=maincolor, font='Arial 14')
        self.label.grid(row=1, column=0, columnspan=2, pady=15)

    def number_recognize(self):
        string = ''
        numbers = []
        for k, v in self.weights.items():
            s = sum([i1 * i2 for i1, i2 in zip(self.inputs, v)])
            if s >= BIAS:
                string += f'Цифра {k} распознанна\n'
                numbers.append(int(k))
        self.show_recognize_number(numbers)
        if string:
            self.label['text'] = string
        else:
            self.label['text'] = "Ничего не распознанно"

    def show_recognize_number(self, numbers):
        for i in range(len(self.labels_number)):
            if i in numbers:
                self.labels_number[int(i)].configure(bg='DarkBlue', fg="white")
            else:
                self.labels_number[int(i)].configure(bg='grey', fg="white")

    def get_weights(self):
        with open('weights.json', 'r') as f:
            weights = json.load(f)
            return weights

    def click_canvas(self, event):
        row = event.y // d
        col = event.x // d

        ind = row * 3 + col
        if self.inputs[ind] == 0:
            self.inputs[ind] = 0.5
        elif self.inputs[ind] == 0.5:
            self.inputs[ind] = 1
        else:
            self.inputs[ind] = 0
        self.draw()
        self.number_recognize()

    def draw(self):
        for i in range(len(self.inputs)):
            row = i // 3
            col = i % 3
            self.draw_square(row, col, self.inputs[i])

    def draw_square(self, row, col, color):
        colors = {0: 'white',
                  0.5: 'grey',
                  1: 'black'}
        x, y = col * d, row * d
        self.canvas.create_rectangle(x+2, y+2, x+d+1, y+d+1, fill=colors[color])


if __name__ == '__main__':
    root = tk.Tk()
    myroot = MyRoot(root)
    root.mainloop()


