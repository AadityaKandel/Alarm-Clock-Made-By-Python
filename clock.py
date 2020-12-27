from tkinter import *
import time
import os
from winsound import *
import pygame
import keyboard
import tkinter.messagebox as tmsg
try:
	os.system('del sta.bat')
	os.system("cls")
	# Import Success
	root = Tk()
	root.title("Alarm [ Not Set ]")
	Label(text = "Alarm Made By Aaditya Kandel",fg = "white",bg = "black",font = "comicsansms 20",justify = "center").pack()
	def save():
		os.system(f'echo {(dirr.get())}>dre.clock')
		os.system('cls')
		sve.set('Saved')
	def empty():
		Label(text = "",bg = "black").pack()
	def act():
		if (dirr.get()) == "":
			tmsg.showinfo('Sorry','Please Fill Out The Directory Box')
		else:
			a = (hour.get()*60*60)
			b = (minute.get()*60)
			c = (second.get())
			d = a+b+c
			root.title(f"Alarm Set Of {d} seconds")
			timee.set(d)
			nott.set('sec')
			for i in range(0,999999999):
				root.update()
				time.sleep(1)
				timee.set((timee.get())-1)
				if (hour.get()) == 0 and (minute.get()) == 0 and (second.get()) == 0:
					tmsg.showinfo('Sorry','Please Fill Out The Hour, Minute And Second')
					timee.set(0)
					nott.set("")
					timee.set("NOT SET")
					root.title("Alarm [ Not Set ]")
				else:
					if (timee.get()) == 0:
						try:
							pygame.init()
							pygame.mixer.music.load(f"{(dirr.get())}")
							pygame.mixer.music.play(loops = 0)
							star.set('Press Ctrl+Q To Stop The Music')
							for i in range(0,999999999):
								root.update()
								if keyboard.is_pressed('ctrl+q'):
									pygame.mixer.music.stop()
									star.set("Start")
									root.title("Alarm [ Not Set ]")
									timee.set("NOT SET")
									nott.set('')
									break
						except:
							tmsg.showinfo('Sorry','Directory Is Wrong')
							break
						break

	empty()

	f1 = Frame(borderwidth = 10, bg = "black")
	f2 = Frame(borderwidth = 10, bg = "black")
	f3 = Frame(borderwidth = 10, bg = "black")

	Label(f1,text = "Music Directory ",fg = "white",bg = "black",font = "comicsansms 14").pack(side=LEFT)
	dirr = StringVar()
	try:
		a = open('dre.clock','r+')
		for words in a:
			pass
		dirr.set(f"{words[0:-1]}")
		a.close()
	except:
		pass
	Entry(f1,textvariable = dirr,fg = "white",bg = "black",font = "comicsansms 14",justify = "left",width = 30).pack(side = LEFT)
	sve = StringVar()
	sve.set('Save')
	Label(f1,text = "",bg = "black").pack(side = LEFT)
	Button(f1,textvariable = sve,fg = "white",bg = "black",font = "comicsansms 14",borderwidth = 1,relief = SUNKEN,command = save).pack(side = LEFT)

	Label(f2,text = "After Time ",fg = "white",bg = "black",font = "comicsansms 14").pack(side=LEFT)
	hour = IntVar()
	hour.set(24)
	minute = IntVar()
	minute.set(24)
	second = IntVar()
	second.set(24)
	Entry(f2,textvariable = hour,fg = "white",bg = "black",font = "comicsansms 14",justify = "left",width = 4).pack(side = LEFT)
	Label(f2,text = "hrs",fg = "white",bg = "black",font = "comicsansms 14").pack(side=LEFT)
	Label(f2,text = "",fg = "white",bg = "black",font = "comicsansms 14").pack(side=LEFT)
	Entry(f2,textvariable = minute,fg = "white",bg = "black",font = "comicsansms 14",justify = "left",width = 4).pack(side = LEFT)
	Label(f2,text = "min",fg = "white",bg = "black",font = "comicsansms 14").pack(side=LEFT)
	Label(f2,text = "",fg = "white",bg = "black",font = "comicsansms 14").pack(side=LEFT)
	Entry(f2,textvariable = second,fg = "white",bg = "black",font = "comicsansms 14",justify = "left",width = 4).pack(side = LEFT)
	Label(f2,text = "sec",fg = "white",bg = "black",font = "comicsansms 14").pack(side=LEFT)

	timee = IntVar()
	timee.set("NOT SET")
	empty()
	nott = StringVar()

	Label(f3,textvariable = timee,fg = "white",bg = "black",font = "comicsansms 30").pack(side = LEFT)
	Label(f3,textvariable = nott,fg = "white",bg = "black",font = "comicsansms 30").pack(side = LEFT)

	f1.pack(anchor = W)
	f2.pack(anchor = W)
	f3.pack()
	empty()
	star = StringVar()
	star.set('Start')
	Button(textvariable = star,fg = "white",bg = "black",font = "comicsansms 20",borderwidth = 1,relief = SUNKEN,command = act).pack()
	empty()

	root.config(bg = "black")
	root.mainloop()
except:
	quit()