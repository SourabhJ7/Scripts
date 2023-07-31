import tkinter as tk

def on_button_click():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

app = tk.Tk()
app.title("Simple GUI")
app.geometry("300x150")

label = tk.Label(app, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=5)

button = tk.Button(app, text="Greet", command=on_button_click)
button.pack(pady=10)

app.mainloop()
