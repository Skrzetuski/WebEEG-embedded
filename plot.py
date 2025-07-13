import serial
import matplotlib.pyplot as plt
from collections import deque

# Adjust this to match your ESP32's port
PORT = '/dev/tty.usbserial-57670109311'
BAUD = 115200

# Set up serial connection
ser = serial.Serial(PORT, BAUD, timeout=1)

# Set up live plot
plt.ion()
fig, ax = plt.subplots()
data = deque([0]*100, maxlen=100)
line, = ax.plot(data)
ax.set_ylim(0, 4095)
ax.set_title("Live ADC Readings")
ax.set_ylabel("ADC Value")
ax.set_xlabel("Sample")

try:
    while True:
        line_bytes = ser.readline()
        try:
            line_str = line_bytes.decode('utf-8').strip()
            if line_str.startswith("ADC:"):
                value = int(line_str.split(":")[1].strip())
                data.append(value)
                line.set_ydata(data)
                line.set_xdata(range(len(data)))
                ax.relim()
                ax.autoscale_view()
                plt.pause(0.01)
        except Exception as e:
            print("Parse error:", e)
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    ser.close()
