from tkinter import *
import tkinter as tk
from time import strftime
import time
import random
from subprocess import call
import PWM
import globalVar

def init_GUI():
    ## GUI creation
    GUI = tk.Tk()
    screen = True
    GUI.title("Electrospinner")
    # set GUI to fullscreen
    GUI.attributes('-fullscreen', screen)
    
    ## define create_widget
    def create_widget(parent, widget_type, **options):
        return widget_type(parent, **options)
    
    ## exit button ##
    # exit button logic
    def exit_button_pressed():
        call("sudo shutdown -h now", shell = True)
#         exit(1)
        
    #exit button creation
    exit_button = create_widget(GUI,
                         tk.Button,
                         text = 'Exit',
                         command = exit_button_pressed,
                         activebackground = 'red',
                         activeforeground = 'white',
                         anchor = CENTER,
                         bd = 3,
                         bg = 'lightgray',
                         cursor = 'hand2',
                         disabledforeground = 'gray',
                         fg = 'black',
                         font = ('Arial', 12),
                         height = 2,
                         highlightbackground = 'black',
                         highlightcolor = 'green',
                         highlightthickness = 2,
                         justify = CENTER,
                         overrelief = RAISED,
                         padx = 10,
                         pady =5,
                         width = 10,
                         wraplength = 100)
    
    # exit button placement
    exit_button.pack(side = TOP, anchor = NE, padx = 25, pady = 15)
    ## end exit button ##
    
    ## world clock ##
    def time():
        time_string = strftime('%H:%M:%S %p')
        clock.config(text = time_string)
        clock.after(1000, time)
    clock = create_widget(GUI,
                          tk.Label,
                          font = ("Arial", 16, 'bold'),
                          foreground = 'black')
    clock.pack(side = TOP, anchor = CENTER)
    time()
    ## end world clock #
    
    ## humidity ##
    hum_list = range(0, 100)
    humidity_text = tk.StringVar()
    def humidity():
        num = random.choice(hum_list)
        hum_text = f'Humidity: {num}%'
        humidity_text.set(hum_text)
        GUI.update()
        sensor_hum.after(2000, humidity)
    sensor_hum = create_widget(GUI,
                               tk.Label,
                               textvariable = humidity_text,
                               font = ('Arial', 16, 'bold'),
                               fg = 'black',
                               bg = 'lightblue',
                               bd = 3,
                               height = 2,
                               width = 17,
                               highlightthickness = 2,
                               highlightbackground = 'black',
                               anchor = W,
                               padx = 15)
    sensor_hum.pack(anchor = E, padx = 25, pady = 15)
    humidity()
    ## end humidity ##
    
    ## temperature ##
    temp_list = range(32, 120)
    temperature_text = tk.StringVar()
    degree = u'\u2109'
    def temperature():
        num2 = random.choice(temp_list)
        temp_text = f'Temperature: {num2}{degree}'
        temperature_text.set(temp_text)
        if num2 > 94:
            if globalVar.duty_exhaust < 50:
                new_duty = globalVar.duty_exhaust + 5
                on_duty_change(new_duty)
        elif num2 < 52:
            if globalVar.duty_exhaust > 20:
                new_duty = globalVar.duty_exhaust -5
                on_duty_change(new_duty)
        GUI.update()
        sensor_hum.after(2000, temperature)
    sensor_temp = create_widget(GUI,
                                tk.Label,
                                textvariable = temperature_text,
                                font = ('Arial', 16, 'bold'),
                                fg = 'black',
                                bg = 'lightblue',
                                bd = 3,
                                height = 2,
                                width = 17,
                                highlightthickness = 2,
                                highlightbackground = 'black',
                                anchor = W,
                                padx = 15)
    sensor_temp.pack(anchor = E, padx = 25, pady = 15)
    temperature()
    ## end temperature ##
    
    ## duty ##
    def on_duty_change(duty_new):
        #duty_change = range
        globalVar.duty_exhaust = duty_new
        
        print(f"{duty_new}")
    ## end duty ##
    
    
    GUI.mainloop()
    
init_GUI()
PWM.initPWM()
#while True:
#    try:
#        init_GUI()
#    except Exception as e:
#       print(f"Waiting for GUI to become available: {e}")
#        time.sleep(0.5)
