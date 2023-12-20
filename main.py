import tkinter

window = tkinter.Tk()
window.title("gui test")
window.minsize(width=600, height=300)
sample_label = tkinter.Label(text="sample label", font=("Aril", 24, "bold"))
sample_label.pack()


def button_clicked():
    print("I got clicked")
    new_text = input_one.get()
    sample_label.config(text=new_text)


button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

input_one = tkinter.Entry()
input_one.pack()


window.mainloop()
