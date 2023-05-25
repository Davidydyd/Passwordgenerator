from tkinter import * 
import random


commonWords = ['mouse','dog','jump','train','soccer','Bayern','show','movie','series','phone']
specialChars =['!','+','#','@','=']


def create_password():
  password = random.choice(commonWords) + random.choice(specialChars) + random.choice(commonWords) + str(random.randint(0,100)) + random.choice(specialChars)
  print("\n\n",password)

window = Tk()
window.title('Password')

button1 = Button(window, text = "Click me", command = create_password)
button1.pack()

#img = PhotoImage(file = "lock.png")
#lock =Canvas.create_image(100,100, image = img)

window.mainloop()
