# Import Module
from tkinter import *
import tkinter as tk
from time import strftime
import time
import random
from subprocess import call
# import PWM
import globalVar

# create GUI window
def init_GUI():
    GUI = tk.Tk()
    screen = True

    # GUI window title and dimension
    GUI.title("Electrospinner")
    # Set geometry (widthxheight)
    # width = GUI.winfo_screenwidth()
    # height = GUI.winfo_screenheight()
    # GUI.geometry('%dx%d' % (width, height))
    GUI.attributes('-fullscreen', screen)

    # all widgets will be here
    def create_widget(parent, widget_type, **options):
        return widget_type(parent, **options)

    # exit button
    #   exits program and shuts off pi
    def exit_button_clicked():
        # GUI.attributes('-fullscreen', False)
        # call("sudo shutdown -h now", shell = True)
        exit(1)
    exit_button = tk.Button(GUI, 
                            text = "Exit", 
                            command = exit_button_clicked,
                            activebackground = "red", 
                            activeforeground = "white",
                            anchor = CENTER,
                            bd = 3,
                            bg = "lightgray",
                            cursor = "hand2",
                            disabledforeground = "gray",
                            fg = "black",
                            font = ("Arial", 12),
                            height = 2,
                            highlightbackground = "black",
                            highlightcolor = "green",
                            highlightthickness = 2,
                            justify = CENTER,
                            overrelief = RAISED,
                            padx = 10,
                            pady = 5,
                            width = 10,
                            wraplength = 100)
    exit_button.pack( side = TOP, anchor = NE, padx = 25, pady = 15)

    def clock():
        string = strftime('%H:%M:%S %p') 
        dsply.config(text = string) 
        dsply.after(1000, clock) 
    dsply = Label(GUI,
                font = ('Arial', 16, 'bold'),  
                foreground = 'black') 
    dsply.pack(anchor = CENTER)
    clock()

    hum_list = range(0, 100)
    humidity_text = tk.StringVar()
    def humidity():
        num = random.choice(hum_list)
        hum_text = f"Humidity: {num}%"
        humidity_text.set(hum_text)
        GUI.update()
        sensor_hum.after(2000, humidity)
    sensor_hum = Label(GUI,
                        textvariable = humidity_text,
                        font = ('Arial', 16, 'bold'),
                        fg = 'black',
                        bg = 'lightblue', 
                        bd = 3,
                        height = 2,
                        highlightthickness = 2, 
                        highlightbackground = 'black', 
                        width = 17,
                        anchor = W,
                        padx = 15)
    sensor_hum.pack(anchor = E, padx = 25, pady = 15)
    humidity()

    def on_duty_change(duty_new):
        globalVar.duty_exhaust = duty_new
        # PWM.update_duty()
        # print(duty_val)

    temp_list = range(120, 32)
    temperature_text = tk.StringVar()
    degree = u'\u2109'
    def temperature():
        num2 = random.choice(temp_list)
        # num2 = duty_val;
        temp_text = f"Temperature: {num2}{degree}"
        temperature_text.set(temp_text)
        if num2 > 50:
            new_duty = globalVar.duty_exhaust + 5
            on_duty_change(new_duty)
        GUI.update()
        sensor_hum.after(2000, temperature)
    sensor_temp = Label(GUI,
                        textvariable = temperature_text,
                        font = ('Arial', 16, 'bold'),
                        fg = 'black',
                        bg = 'lightblue', 
                        bd = 3,
                        height = 2,
                        highlightthickness = 2, 
                        highlightbackground = 'black', 
                        width = 17,
                        anchor = W,
                        padx = 15)
    sensor_temp.pack(anchor = E, padx = 25, pady = 15)
    temperature()

    duty = IntVar()
    duty_frame = create_widget(GUI,
                                tk.Frame,
                                bg='lightblue',
                                bd=3,
                                cursor='hand2',
                                height=100,
                                highlightcolor='red', 
                                highlightthickness=2, 
                                highlightbackground='black',
                                relief=tk.RAISED,
                                width=200)
    duty_frame.pack(padx=20, pady=20)


    duty = create_widget(duty_frame, 
                        tk.Label,
                        text = globalVar.duty_exhaust,
                        # text = "test",
                        width = 10,                
                        font = ('Arial', 16, 'bold'),
                        bg = 'lightblue',
                        fg = 'black')
    # duty.config(state = "readonly",
    #             cursor = "hand2",
    #             readonlybackground = 'lightblue',
    #             bd = 3,
    #             justify = "center",
    #             wrap = True)
    duty.grid(row = 0, column = 1, sticky = E)
    duty_label = create_widget(duty_frame,
                                tk.Label,
                                text = "Duty %:",
                                width = 10,
                                font = ('Arial', 16, 'bold'),
                                bg = 'lightblue',
                                fg = 'black',)
    duty_label.grid(row = 0, column = 0, sticky = W)


    # Execute Tkinter
    GUI.mainloop()

# while True:
#     try:
#         init_GUI()
#     except Exception as e:
#         print(f"Waiting for GUI to become available: {e}")
#         time.sleep(0.2)