from tkinter import *
import random

SNAKES_LADDERS = ([1,30],[2,50],[3,55],[4,30],[5,40],[9,31], [24,66], [55,97], [25,3], [98,7])


class StartApp:

    def __init__(self, master=None):
        self.master = master
        self.pos_text = StringVar()
        self.current_pos = 1 #Position which the user sees
        self.new_pos = None
        self.dice_frame = None
        self.dice_val = StringVar()
        self.LadderStartIndex = []
        self.SnakesStartIndex = []

        for x in SNAKES_LADDERS:
            if x[0] < x[1]:
                self.LadderStartIndex.append(x[0])
            else:
                self.SnakesStartIndex.append(x[0])

        print(self.LadderStartIndex)
        print(self.SnakesStartIndex)

        self.create_dice_layout()
        
        self.frame = Frame(self.master, bg='gray50', height=600,
                           relief=RAISED)

        
        self.frame.pack(side=TOP, anchor=N, expand=NO, fill=None, padx=1, pady=1)

        self.frame.columnconfigure(10,weight=1, minsize=0)
        self.frame.rowconfigure(10,weight=1, minsize=0)

        for r in range(10,0,-1):
            for c in range(10,0,-1):
                self.pos_text = str((r-1)*10+c)
                lbl = Label(self.frame, text=self.pos_text, bd=10,fg='blue',
                            bg='yellow' if self.pos_text==str(self.current_pos) else 'gray90')
                lbl.grid(row=10-r, column= c-1 if r%2 else 10-c, rowspan=1,
                         columnspan=1, sticky=NSEW, padx=2, pady=2)

        # use self.LadderStartIndex and self.SnakesStartIndex and change the label color

    def create_dice_layout(self):
        self.dice_frame = Frame(self.master, bg='blue', height=30)
        self.dice_frame.pack(side=TOP, anchor=N,fill=X, expand=YES)
        
        btn = Button(self.dice_frame, text='Throw Dice', command=self.diceBtnAction)
        btn.pack(side=LEFT, anchor=W, padx=2, pady=2)
        self.dice_val = '0'
        self.dice_lbl = Label(self.dice_frame, text=self.dice_val, width=10, fg='red')
        self.dice_lbl.pack(side=LEFT, anchor=W, padx=2, pady=2)
        btn = Button(self.dice_frame, text='Restart Game', command=self.restart_game)
        btn.pack(side=RIGHT, anchor=E, padx=2, pady=2)

    def move_player_to(self, pos):
        print(self.current_pos)
        color = 'yellow'
        lbl = self.frame.grid_slaves()[self.current_pos-1]
        
        if not self.player_won(pos):
            if pos > 100:
                return
        else:
            color = 'green'    
        lbl.configure(bg = 'gray90')
        lbl = self.frame.grid_slaves()[pos-1]
        lbl.configure(bg = color)
        self.current_pos = pos
        

    def diceBtnAction(self):
        new_val = random.randrange(1,7)
        #Update Dice Label
        self.dice_lbl.configure(text=str(new_val))
        
        if self.current_pos == 100:
            return

        self.new_pos = self.current_pos + new_val
        ret = self.search_snakes_ladders(self.new_pos)
        print("ret is:"+str(ret))
        if ret != -1:
            self.new_pos = ret

        self.move_player_to(self.new_pos)

    def restart_game(self):
        self.move_player_to(1)


    def player_won(self, new_pos):
        return True if new_pos == 100 else False

    def search_snakes_ladders(self, key):
        try:
            l_pos = self.LadderStartIndex.index(key)
            key_present = True
        except:
            try:
                l_pos = self.SnakesStartIndex.index(key)
                key_present = True
            except:
                key_present = False

        if key_present:
            return SNAKES_LADDERS[l_pos][1]
        else:
            return -1


if __name__ == '__main__':
    root = Tk()
    root.resizable(0,0)
    root.title('Snakes and Ladder by Avdesh')
    start = StartApp(root)
    root.mainloop()
