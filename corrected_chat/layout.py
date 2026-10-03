import tkinter as tk
from tkinter import messagebox


class Layout:
    """Tkinter chat interface shared by the client and server."""

    def __init__(self, connection, title):
        self.connection = connection

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("500x500")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.listbox = tk.Listbox(self.root, font=("Arial", 12))
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        bottom = tk.Frame(self.root)
        bottom.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.entry = tk.Entry(bottom, font=("Arial", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self.send)

        self.button = tk.Button(bottom, text="Send", command=self.send)
        self.button.pack(side=tk.RIGHT, padx=(10, 0))

        self.connection.on_message = self.receive_message

    def send(self, event=None):
        message = self.entry.get().strip()
        if not message:
            return

        try:
            self.connection.send_message(message)
            self.listbox.insert(tk.END, f"You: {message}")
            self.entry.delete(0, tk.END)
        except OSError as error:
            messagebox.showerror("Connection Error", str(error))

    def receive_message(self, message):
        self.root.after(0, lambda: self._add_message(message))

    def _add_message(self, message):
        self.listbox.insert(tk.END, f"Other: {message}")
        self.listbox.see(tk.END)

    def start(self):
        self.root.mainloop()

    def close(self):
        self.connection.close()
        self.root.destroy()
