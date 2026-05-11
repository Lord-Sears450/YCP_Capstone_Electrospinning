## Program Start
global startTime
startTime = 0

## PWM vals
global duty_intake
global intake
duty_intake = 20
intake = 1800 * (duty_intake/100)   # converts PWM to RPM
global duty_exhaust
global exhaust
duty_exhaust = 30
exhaust = 1800 * (duty_exhaust/100) # converts PWM to RPM

## sensor vals
global temp_max
global temp_min
global temp
temp_max = 100
temp_min = 0
temp = 0

global hum_max
global hum_min
global hum
hum_max = 100
hum_min = 0
hum = 0

global press_max
global press_min
global press
press_max = 100
press_min = 0
press = 0

global wind_max
global wind_min
global wind
wind_max = 100
wind_min = 0
wind = 0
