from tkinter import *
import OTP
import win32gui, win32con


def callbackfunc():
    otp = OTP.get_otp()
    otp_value.set(otp)
    root.clipboard_clear()
    root.clipboard_append(otp)
    root.update()


hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

root = Tk()
root.title("eToken Pass")
root.clipboard_clear()
root.resizable(0, 0)

c = Canvas(root, width=309, height=163, bg='white')
c.pack()
eToken_Pass_image = PhotoImage(file=r"img\eToken_pass.png")
image_eToken = c.create_image(155, 80, image=eToken_Pass_image)

otp_value = StringVar()
otp_edit = Entry(root, bd=5, width=14, justify=RIGHT, textvariable=otp_value, state=DISABLED).place(x=70, y=68)

Button_image = PhotoImage(file=r"img\Button.png")
button = Button(root, image=Button_image, command=callbackfunc).place(x=185, y=57)
root.mainloop()

