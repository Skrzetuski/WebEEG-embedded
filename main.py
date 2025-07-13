from machine import ADC, Pin, Timer
import time

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

def read_adc(timer):
    value = adc.read()
    print("ADC:", value)

# Create a timer that triggers every 100 ms (10 Hz)
tim = Timer(0)
tim.init(period=100, mode=Timer.PERIODIC, callback=read_adc)

# Keep the main thread alive
while True:
    time.sleep(1)
