from tkinter import *

class TextDisappearingApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dangerous Writing App")
        self.window.minsize(height=500, width=700)
        self.window.maxsize(height=500, width=700)
        self.window.config(padx=35, pady=20)
        self.ui_setup()
        self.window.mainloop()

    def ui_setup(self):
        self.title = Label(text='Dangerous Writing App', justify='center',  font=('Arial', 29, 'bold')) 
        self.title.grid(row=1, column=0, columnspan=3)
        self.timer = Label(text='TIME: 0', font=('Arial', 10, 'bold'), fg='#2d6da7')
        self.timer.grid(row=0, column=2)
        self.entry_text = Text(font=('Arial', 20, 'normal'), padx=7, pady=7, width=40, height=10, state='disabled')
        self.entry_text.grid(row=2, column=0, pady=10, columnspan=3)
        self.restart_btn = Button(text='Restart',bg="#c14134", font=('Arial', 15, 'bold'), fg='white', activebackground="#4ac78b", command=self.restart)
        self.restart_btn.grid(row=3, column=0, columnspan=3)
        self.timer_countdown(65)
        self.entry_text.bind("<Key>", self.on_typing)
        self.typing_timer = None  
        self.typing_threshold = 5000
    

    def timer_countdown(self, count):
        if count<=60:
            self.timer.config(text=f"TIME: {count}", fg='#2d6da7')
            self.entry_text.config(state='normal')
            self.entry_text.focus_set()  
           
            if count < 10:
                self.timer.config(fg='red')
            if count == 0:
                self.timer.config(text='Time up')
                self.window.after_cancel(self.timer_after)
                self.window.after_cancel(self.typing_timer)
                self.entry_text.config(state='disabled')
        if count > 0:
            self.timer_after = self.window.after(1000, self.timer_countdown, count-1)
        if count >60:
            self.timer.config(text=f"Starts in {count-60}", fg="#4ac78b")
        

    def on_typing(self, event):
        if self.typing_timer:
            self.window.after_cancel(self.typing_timer)
        self.typing_timer = self.window.after(self.typing_threshold, self.check_typing)


    def check_typing(self):
        print('user stopped typing')
        self.entry_text.delete('1.0','end')
        self.entry_text.config(bg='red')
        self.window.after_cancel(self.timer_after)

    def restart(self):
        self.window.after_cancel(self.timer_after)
        self.window.after_cancel(self.typing_timer)
        self.entry_text.delete('1.0','end')
        self.entry_text.config(bg='red')
        self.ui_setup()



app = TextDisappearingApp()