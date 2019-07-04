import time, datetime, winsound
print("Welcome to the Pomodoro Effect!!!")

pomodoros= 0
n= "-" *25
def sleep_(time_):
	time.sleep(time_)
	fname = "C:/Users/User/Documents/$+pythonized/projects/media_dump/fit_music.wav"
	winsound.PlaySound(fname, winsound.SND_FILENAME)

def work():
	print(f"\nStart working (30mins):", datetime.datetime.now().strftime("%H:%M:%S"))
	sleep_(60*30)

def short_break():
	print(f"Time to take a short break (10mins): ", datetime.datetime.now().strftime("%H:%M:%S"))
	sleep_(60*10)

def long_break():
	print(f"Time to take a long break (30mins): ", datetime.datetime.now().strftime("%H:%M:%S"))
	sleep_(60*10)



while True:
	for i in range(3): #Three short breaks 
		work()
		short_break()
	work()
	long_break()
	pomodoros+=1
	print(f"\n{n}\n\tPomodoros done: {pomodoros}\n{n}")

