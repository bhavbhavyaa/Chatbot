from tkinter import *
window = Tk()
def send():
    send = "You -> "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get().lower() in ["hello","hi"]):
        txt.insert(END,"\n"+"Bot -> Hola")
    elif(e.get().lower() in ["whats your name","who are you"]):
        txt.insert(END,"\n"+"Bot -> I am a baby bot! what about you")
    elif(e.get().lower() in ["how are you","how have you been","how are you doing"]):
        txt.insert(END,"\n"+"Bot -> Fine and you")
    elif(e.get().lower() == "Fine"):
        txt.insert(END,"\n"+"Bot -> Nice to hear")
    else:
        txt.insert(END,"\n"+"""Bot -> I am a baby bot still learning,
                   you need to add on things to make me learn new things""")
    e.delete(0,END)
txt = Text(window)
txt.grid(row = 0,column = 0, columnspan = 2)
e = Entry(window,width = 100)
e.grid(row = 1, column = 0)
send = Button(window,text = "Send",command = send)
send.grid(row = 1,column = 1)
window.title("Chatbot")
window.mainloop()

        







