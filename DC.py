import time

def digital_clock():
    while True:
        current_time = time.strftime("%H:%M:%S")  
        print("Time:", current_time, end="\r")
        time.sleep(1)

digital_clock()
