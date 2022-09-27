import pyscreenrec
import  time

rec = pyscreenrec.ScreenRecorder()



rec.start_recording("abc.mp4",5)

time.sleep(10)

rec.pause_recording()

time.sleep(5)

rec.resume_recording()

time.sleep(5)

rec.stop_recording()