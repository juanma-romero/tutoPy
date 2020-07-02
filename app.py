import tkinter as tk
import tkinter.messagebox as msgbox


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        self.label_text = tk.StringVar()
        self.label_text.set("My name is:")

        self.name_text = tk.StringVar()

        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)

        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        hello_boton = tk.Button(self, text="Say Hello",
                                command=self.say_hello)
        hello_boton.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

        good_boton = tk.Button(self, text="Say Goodby",
                               command=self.say_goodby)
        good_boton.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        message = "Hello there " + self.name_entry.get()
        msgbox.showinfo("Hello", message)

    def say_goodby(self):
        if msgbox.askyesno("Close Window?", "wuold you like to close this window"):
            message = "Windows will close in 2 sec - goodby " + self.name_text.get()
            self.label_text.set(message)
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo("Not Closing", "Great! this window will stay open.")


if __name__ == "__main__":
    window = Window()
    window.mainloop()
