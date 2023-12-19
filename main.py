import tkinter

window = tkinter.Tk()
window.title("gui test")
window.minsize(width=600, height=300)
sample_label = tkinter.Label(text="sample label", font=("Aril", 24, "bold"))
sample_label.pack()


def button_clicked():
    print("I got clicked")
    sample_label.config(text="I got clicked")


button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

window.mainloop()
