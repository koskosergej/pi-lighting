from gpiozero import LED
from signal import pause

led = LED(4)  # GPIO pin 4 (physical pin 7)

led.blink(on_time=0.5, off_time=0.5)  # 0.5s on, 0.5s off

pause()  # keep the script running
