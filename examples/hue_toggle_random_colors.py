from tkinter import *
from phue import Bridge
import random


def set_light_xy(obj):
    obj.xy = [random.random(),random.random()]
    

b = Bridge('192.168.1.10')

root = Tk()
root.title("Hue Test App")

horizontal_frame = Frame(root)
horizontal_frame.pack()

if not b.get_light(1, 'on'):
    b.set_light(1, 'on', True)
    b.set_light(1, 'bri', 50)

if not b.get_light(2, 'on'):
    b.set_light(2, 'on', True)
    b.set_light(2, 'bri', 100)

if not b.get_light(3, 'on'):
    b.set_light(3, 'on', True)
    b.set_light(3, 'bri', 150)

for light in b.lights:
    light_id = light.light_id
    light.xy = [random.random(),random.random()]
    channel_frame = Frame(horizontal_frame)
    channel_frame.pack(side = LEFT)

    scale_command = lambda x, light_id=light_id: b.set_light(light_id,{'bri': int(x), 'transitiontime': 1})
    scale = Scale(channel_frame, from_ = 254, to = 0, command = scale_command, length = 200, showvalue = 0)
    scale.set(b.get_light(light_id,'bri'))
    scale.pack()

    button_var = BooleanVar()
    button_var.set(b.get_light(light_id, 'on'))
    button_command = lambda button_var=button_var, light_id=light_id: b.set_light(light_id, 'on', button_var.get())
    button = Checkbutton(channel_frame, variable = button_var, command = button_command)
    button.pack()

    
    button_random_command = lambda  light = light: set_light_xy(light)
    button_random = Button(channel_frame, command = button_random_command)
    button_random.pack()
    

    label = Label(channel_frame)
    label.config(text = b.get_light(light_id,'name'))
    label.pack()

root.mainloop()