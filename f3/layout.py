from tkinter import *


class Layout:

    def __init__(self, connection, title):
        self.connection = connection

        self.root = Tk()
        self.root.title(title)

        self.listbox = Listbox(self.root)
        self.listbox.pack()

        self.entry = Entry(self.root)
        self.entry.pack(side=BOTTOM)

        self.button = Button(
            self.root,
            text="Send",
            command=self.send_message
        )
        self.button.pack(side=BOTTOM)

        self.rbutton = Button(
            self.root,
            text="Receive",
            command=self.receive_message
        )
        self.rbutton.pack(side=BOTTOM)

    def send_message(self):
        message = self.entry.get()

        if message:
            self.listbox.insert(END, "You: " + message)
            self.connection.send(message)
            self.entry.delete(0, END)

    def receive_message(self):
        message = self.connection.receive()
        self.listbox.insert(END, "Receiver: " + message)

    def start(self):
        self.root.mainloop()