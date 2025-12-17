# import RPi.GPIO as GPIO
from time import sleep
import globalVar
import pi.gpio 

pwm_exhaust = 12				
pwm_intake = 13
pi.set_PWM_range(pwm_exhaust, 1000) 
pi.set_PWM_range(pwm_intake, 1000)
# GPIO.setwarnings(False)			#disable warnings
# GPIO.setmode(GPIO.BOARD)		#set pin numbering system
# GPIO.setup(pwm_intake, GPIO.OUT)
# GPIO.setup(pwm_exhaust, GPIO.OUT)
def update_duty():
    # pi_pwm_intake = GPIO.PWM(pwm_intake, 2000)		#create PWM instance with frequency
    # pi_pwm_intake.start(globalVar.duty_intake)				#start PWM of required Duty Cycle 
    # pi_pwm_exhaust = GPIO.PWM(pwm_exhaust, 2000)
    # pi_pwm_exhaust.start(globalVar.duty_exhaust)
    print(f"exhaust: {globalVar.duty_exhaust}")
    print(f"intake: {globalVar.duty_intake}")
# def update_duty():
#     print(f"exhaust: {globalVar.duty_exhaust}")
#     print(f"intake: {globalVar.duty_intake}")
# duty_list = range(0, 20)
# def duty():
#     duty_val = random.choice(duty_list)
#     duty_val = duty_val * 5
#     globalVar.duty_exhaust = duty_val
#     # num2 = duty_val;
#     # temp_text = f"Temperature: {duty}"
#     # temperature_text.set(temp_text)
#     # GUI.update()
#     # sleep(2000)
#     # PWM.duty()
# duty()