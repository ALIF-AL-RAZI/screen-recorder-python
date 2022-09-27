from tkinter import *
import pyscreenrec

import time



mainScrn = Tk()
mainScrn.geometry("400x600")
mainScrn.configure(bg="#fff")
mainScrn.resizable(False,False)
mainScrn.title("Screen Recorder")



def strt_rec():
    cur_time = time.localtime()
    get_file_name = time.strftime("%H-%M-%S-(%d-%m-%Y)",cur_time)
    rec.start_recording(get_file_name+".mp4",20)

def pause_rec():
    rec.pause_recording()


def resume_rec():
    rec.resume_recording()


def stop_rec():
    rec.stop_recording()


rec = pyscreenrec.ScreenRecorder()



icon = PhotoImage(file="screen-recording.png")
mainScrn.iconphoto(False, icon)

Label(mainScrn, text="Record Your Screen", bg="#fff", font="arial 15 bold").pack(pady=20)

image1 = PhotoImage(file="video.png")
Label(mainScrn, image=image1, bg="#fff").pack(pady=10)


# Filename = StringVar()
# entry= Entry(mainScrn, textvariable="Filename", width=18, font="arial 15")
# entry.pack(pady=10)
# Filename.set("recording25")


strt_img = PhotoImage(file="screen-recording.png")
Button(mainScrn, image=strt_img, bd=0, bg="#fff", command=strt_rec).place(relx=.5, rely=.5, anchor="center")

Label(mainScrn, text="Start Recording", bg="#fff", font="arial 15 bold").place(y=350, x=100)


pause_img = PhotoImage(file="pause (1).png")
pause_btn = Button(mainScrn, image=pause_img, bd=0, bg="#fff", command=pause_rec)
pause_btn.place(x=50, y=450)


resume_img = PhotoImage(file="play.png")
resume_btn = Button(mainScrn, image=resume_img, bd=0, bg="#fff", command=resume_rec)
resume_btn.place(x=150, y=450)


stop_img = PhotoImage(file="stop (1).png")
stop_btn = Button(mainScrn, image=stop_img, bd=0, bg="#fff", command=stop_rec)
stop_btn.place(x=250, y=450)


mainScrn.mainloop()