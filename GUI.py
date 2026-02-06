from tkinter import *
from tkinter import ttk
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
    
    GUI.columnconfigure(0, weight = 1)
    GUI.columnconfigure(1, weight = 1)
    GUI.columnconfigure(2, weight = 1)
    GUI.columnconfigure(3, weight = 1)
    GUI.columnconfigure(4, weight = 1)
    GUI.rowconfigure(0, weight = 1)
    GUI.rowconfigure(1, weight = 1)
    GUI.rowconfigure(2, weight = 1)
    GUI.rowconfigure(3, weight = 1)
    GUI.rowconfigure(4, weight = 1)
    
    ## define create_widget
    def create_widget(parent, widget_type, **options):
        return widget_type(parent, **options)
    
    ## exit button ##
    # exit button logic
    def exit_button_pressed():
        # call("sudo shutdown -h now", shell = True)
        exit(1)
        
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
    
    exit_button.grid(row = 0, column = 4)
    ## end exit button ##
    
    def center(win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()
    
    ## Set Range ##
    # set popup size
    popup_width = int(GUI.winfo_screenwidth() * 0.75)
    popup_height = int(GUI.winfo_screenheight() * 0.75)
    # define popup
    def set_range_popup():
        set_range_popup = tk.Tk() 
        set_range_popup.geometry(f"{popup_width}x{popup_height}")
        set_range_popup.overrideredirect(True)
        set_range_popup.wm_sizefrom()
        center(set_range_popup)
        set_range_popup.title("Set Value Ranges")
        set_range_popup.columnconfigure(0, weight = 1)
        set_range_popup.columnconfigure(1, weight = 1)
        set_range_popup.columnconfigure(2, weight = 1)
        set_range_popup.columnconfigure(3, weight = 1)
        set_range_popup.rowconfigure(0, weight = 1)
        set_range_popup.rowconfigure(1, weight = 2) ## temperature
        set_range_popup.rowconfigure(2, weight = 1)
        set_range_popup.rowconfigure(3, weight = 2) ## humidity
        set_range_popup.rowconfigure(4, weight = 1)
        set_range_popup.rowconfigure(5, weight = 2) ## pressure
        set_range_popup.rowconfigure(6, weight = 1)
        set_range_popup.rowconfigure(7, weight = 2) ## air speed/wind
        set_range_popup.rowconfigure(8, weight = 1)
        
        ## Temperature ##
        temp = create_widget(set_range_popup,
                            tk.Frame,
                            bg="lightgrey", 
                            width = 50,
                            height = 10,
                            bd = 3)
        temp.grid(row = 1, column = 0)
        temp_max_label = create_widget(temp,
                                tk.Label,
                                text = "Set Max Temperature:",
                                font=("Arial", 12),
                                bg="lightgrey", 
                                width = 20,
                                justify = "center",
                                padx = 5,
                                pady = 5,
                                wrap = False)
        temp_max_label.grid(row = 0, column = 0)
        temp_min_label = create_widget(temp,
                                tk.Label,
                                text = "Set Min Temperature:",
                                font=("Arial", 12),
                                bg="lightgrey", 
                                width = 20,
                                justify = "center",
                                padx = 5,
                                pady = 5,
                                wrap = False)
        temp_min_label.grid(row = 0, column = 2)
        ## Temp Set
        temp_max = IntVar(temp)
        temp_min = IntVar(temp)
        temp_max.set(75)
        temp_min.set(10)
        def update_temp():
            temp_min_upper = int(temp_max_box.get()) - 1
            temp_min_box.config(to = temp_min_upper)
            temp_max_lower = int(temp_min_box.get()) + 1
            temp_max_box.config(from_ = temp_max_lower)
        temp_max_box = create_widget(temp,
                            tk.Spinbox,
                            from_ = 50,
                            to = 100,
                            textvariable = temp_max,
                            command = update_temp,
                            width = 10,
                            relief = "sunken",
                            font=("Arial", 24), 
                            bg="lightgrey", 
                            fg="blue",
                            state="normal",
                            repeatdelay = 500,
                            repeatinterval = 100, 
                            cursor="hand2", 
                            bd=3, 
                            justify="center", 
                            wrap=True)
        temp_max_box.grid(row = 0, column = 1)
        temp_min_box = create_widget(temp,
                            tk.Spinbox,
                            from_ = 0,
                            to = 50,
                            textvariable = temp_min,
                            command = update_temp,
                            width = 10,
                            relief = "sunken",
                            font=("Arial", 24), 
                            bg="lightgrey", 
                            fg="blue",
                            state="normal", 
                            cursor="hand2", 
                            bd=3, 
                            justify="center", 
                            wrap=True)
        temp_min_box.grid(row = 0, column = 3)
        ## End Temperature ##
        
        ## Humidity ##
        hum = create_widget(set_range_popup,
                            tk.Frame,
                            bg="lightgrey", 
                            width = 50,
                            height = 10,
                            bd = 3)
        hum.grid(row = 3, column = 0)
        hum_max_label = create_widget(hum,
                                tk.Label,
                                text = "Set Max Humidity:",
                                font=("Arial", 12),
                                bg="lightgrey", 
                                width = 20,
                                justify = "center",
                                padx = 5,
                                pady = 5,
                                wrap = False)
        hum_max_label.grid(row = 0, column = 0)
        hum_min_label = create_widget(hum,
                                tk.Label,
                                text = "Set Min Humidity:",
                                font=("Arial", 12),
                                bg="lightgrey", 
                                width = 20,
                                justify = "center",
                                padx = 5,
                                pady = 5,
                                wrap = False)
        hum_min_label.grid(row = 0, column = 2)
        ## Hum Set
        hum_max = IntVar(temp)
        hum_min = IntVar(temp)
        hum_max.set(75)
        hum_min.set(10)
        def update_hum():
            hum_min_upper = int(hum_max_box.get()) - 1
            hum_min_box.config(to = hum_min_upper)
            hum_max_lower = int(hum_min_box.get()) + 1
            hum_max_box.config(from_ = hum_max_lower)
        hum_max_box = create_widget(hum,
                            tk.Spinbox,
                            from_ = 0,
                            to = 100,
                            textvariable = hum_max,
                            command = update_hum,
                            width = 10,
                            relief = "sunken",
                            font=("Arial", 24), 
                            bg="lightgrey", 
                            fg="blue",
                            state="normal",
                            repeatdelay = 500,
                            repeatinterval = 100, 
                            cursor="hand2", 
                            bd=3, 
                            justify="center", 
                            wrap=True)
        hum_max_box.grid(row = 0, column = 1)
        hum_min_box = create_widget(hum,
                            tk.Spinbox,
                            from_ = 0,
                            to = 50,
                            textvariable = hum_min,
                            command = update_hum,
                            width = 10,
                            relief = "sunken",
                            font=("Arial", 24), 
                            bg="lightgrey", 
                            fg="blue",
                            state="normal", 
                            cursor="hand2", 
                            bd=3, 
                            justify="center", 
                            wrap=True)
        hum_min_box.grid(row = 0, column = 3)
        ## End Humidity ##
        
        ## Pressure ##
        press = create_widget(set_range_popup,
                            tk.Frame,
                            bg="lightgrey", 
                            width = 50,
                            height = 10,
                            bd = 3)
        press.grid(row = 5, column = 0)
        press_max_label = create_widget(press,
                                tk.Label,
                                text = "Set Max Pressure:",
                                font=("Arial", 12),
                                bg="lightgrey", 
                                width = 20,
                                justify = "center",
                                padx = 5,
                                pady = 5,
                                wrap = False)
        press_max_label.grid(row = 0, column = 0)
        press_min_label = create_widget(press,
                                tk.Label,
                                text = "Set Min Pressure:",
                                font=("Arial", 12),
                                bg="lightgrey", 
                                width = 20,
                                justify = "center",
                                padx = 5,
                                pady = 5,
                                wrap = False)
        press_min_label.grid(row = 0, column = 2)
        ## Press Set
        press_max = IntVar(press)
        press_min = IntVar(press)
        press_max.set(75)
        press_min.set(10)
        def update_press():
            press_min_upper = int(press_max_box.get()) - 1
            press_min_box.config(to = press_min_upper)
            press_max_lower = int(press_min_box.get()) + 1
            press_max_box.config(from_ = press_max_lower)
        press_max_box = create_widget(press,
                            tk.Spinbox,
                            from_ = 50,
                            to = 100,
                            textvariable = press_max,
                            command = update_press,
                            width = 10,
                            relief = "sunken",
                            font=("Arial", 24), 
                            bg="lightgrey", 
                            fg="blue",
                            state="normal",
                            repeatdelay = 500,
                            repeatinterval = 100, 
                            cursor="hand2", 
                            bd=3, 
                            justify="center", 
                            wrap=True)
        press_max_box.grid(row = 0, column = 1)
        press_min_box = create_widget(press,
                            tk.Spinbox,
                            from_ = 0,
                            to = 50,
                            textvariable = press_min,
                            command = update_press,
                            width = 10,
                            relief = "sunken",
                            font=("Arial", 24), 
                            bg="lightgrey", 
                            fg="blue",
                            state="normal", 
                            cursor="hand2", 
                            bd=3, 
                            justify="center", 
                            wrap=True)
        press_min_box.grid(row = 0, column = 3)
        ## End Pressure ##
        
        ## Air Speed / Wind ##
        wind = create_widget(set_range_popup,
                            tk.Frame,
                            bg="lightgrey", 
                            width = 50,
                            height = 10,
                            bd = 3)
        wind.grid(row = 7, column = 0)
        wind_max_label = create_widget(wind,
                                tk.Label,
                                text = "Set Max Air Speed:",
                                font=("Arial", 12),
                                bg="lightgrey", 
                                width = 20,
                                justify = "center",
                                padx = 5,
                                pady = 5,
                                wrap = False)
        wind_max_label.grid(row = 0, column = 0)
        wind_min_label = create_widget(wind,
                                tk.Label,
                                text = "Set Min Air Speed:",
                                font=("Arial", 12),
                                bg="lightgrey", 
                                width = 20,
                                justify = "center",
                                padx = 5,
                                pady = 5,
                                wrap = False)
        wind_min_label.grid(row = 0, column = 2)
        ## Air Speed Set
        wind_max = IntVar(wind)
        wind_min = IntVar(wind)
        wind_max.set(75)
        wind_min.set(10)
        def update_wind():
            wind_min_upper = int(wind_max_box.get()) - 1
            wind_min_box.config(to = wind_min_upper)
            wind_max_lower = int(wind_min_box.get()) + 1
            wind_max_box.config(from_ = wind_max_lower)
        wind_max_box = create_widget(wind,
                            tk.Spinbox,
                            from_ = 50,
                            to = 100,
                            textvariable = wind_max,
                            command = update_wind,
                            width = 10,
                            relief = "sunken",
                            font=("Arial", 24), 
                            bg="lightgrey", 
                            fg="blue",
                            state="normal",
                            repeatdelay = 500,
                            repeatinterval = 100, 
                            cursor="hand2", 
                            bd=3, 
                            justify="center", 
                            wrap=True)
        wind_max_box.grid(row = 0, column = 1)
        wind_min_box = create_widget(wind,
                            tk.Spinbox,
                            from_ = 0,
                            to = 50,
                            textvariable = wind_min,
                            command = update_wind,
                            width = 10,
                            relief = "sunken",
                            font=("Arial", 24), 
                            bg="lightgrey", 
                            fg="blue",
                            state="normal", 
                            cursor="hand2", 
                            bd=3, 
                            justify="center", 
                            wrap=True)
        wind_min_box.grid(row = 0, column = 3)
        ## End Air Speed / Wind ##
        
        def set_range():
            globalVar.temp_max = temp_max_box.get()
            globalVar.temp_min = temp_min_box.get()
            globalVar.hum_max = hum_max_box.get()
            globalVar.hum_min = hum_min_box.get()
            globalVar.press_max = press_max_box.get()
            globalVar.press_min = press_min_box.get()
            set_range_popup.destroy()
        #set button creation
        set_button = create_widget(set_range_popup,
            tk.Button,
            text = 'Set Values',
            command = set_range,
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
        # set button placement
        set_button.grid(row = 1, column = 3)
    set_range_button = create_widget(GUI,
                        tk.Button,
                        text = 'Set Value Ranges',
                        command = set_range_popup,
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
    # set range button placement
    set_range_button.grid(row = 0, column = 0)
    ## end set range ##
    
    ## world clock ##
    def time():
        time_string = strftime('%H:%M:%S %p')
        clock.config(text = time_string)
        clock.after(1000, time)
    clock = create_widget(GUI,
                          tk.Label,
                          font = ("Arial", 16, 'bold'),
                          foreground = 'black')
    clock.grid(row = 0, column = 2)
    time()
    ## end world clock #
    
    ## humidity ##
    # hum_list = range(0, 100)
    humidity_text = tk.StringVar()
    def humidity():
        # num = random.choice(hum_list)
        num = "Null"
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
    sensor_hum.grid(row = 1, column = 4)
    humidity()
    ## end humidity ##
    
    ## temperature ##
    # temp_list = range(32, 120)
    temperature_text = tk.StringVar()
    degree = u'\u2109'
    def temperature():
        # num2 = random.choice(temp_list)
        num2 = "Null"
        temp_text = f'Temperature: {num2}{degree}'
        temperature_text.set(temp_text)
        # if num2 > 94:
        #     if globalVar.duty_exhaust < 50:
        #         new_duty = globalVar.duty_exhaust + 5
        #         # on_duty_change(new_duty)
        # elif num2 < 52:
        #     if globalVar.duty_exhaust > 20:
        #         new_duty = globalVar.duty_exhaust -5
        #         # on_duty_change(new_duty)
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
    sensor_temp.grid(row = 2, column = 4)
    temperature()
    ## end temperature ##
    
    GUI.mainloop()
    
init_GUI()
PWM.initPWM()
#while True:
#    try:
#        init_GUI()
#    except Exception as e:
#       print(f"Waiting for GUI to become available: {e}")
#        time.sleep(0.5)
