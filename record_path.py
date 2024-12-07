filename = "path.py"








import time
from auto import *
from threading import Thread
from pynput import mouse, keyboard
from ahk import AHK

ahk = AHK()
class Path():
    def __init__(self, filename=filename):
        self.azerty_keyboard = False
        self.filename = filename
        
        self.start_time = None
        self.last_action = None

        self.stop_recording_flag = False
        self.stop_replay_flag = False

        self.actions = []

        self.mouse_controller = mouse.Controller()
        self.keyboard_controller = keyboard.Controller()
    
    def start_recording(self):
        self.recording = True
        self.start_time = None
        self.actions = []
        self.stop_recording_flag = False

        self.actions.append("\n\n# New Recording\n")

        with mouse.Listener(on_click=self.on_click) as mouse_listener, \
            keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as keyboard_listener:
            
            while not self.stop_recording_flag: time.sleep(0.1)

            mouse_listener.stop()
            keyboard_listener.stop()
        
        self.recording = False
        self.actions[1] == ""
        self.save_recording()

    def on_click(self, x, y, button, pressed):
        self.record_mouse(x, y, button, pressed)

    def on_press(self, key):
        if key == keyboard.Key.f2:
            self.stop_recording_flag = True
        self.record_keyboard(key, True)

    def on_release(self, key):
        self.record_keyboard(key, False)
    
    def record_mouse(self, x, y, button, pressed):
        if not self.stop_recording_flag:
            if not self.start_time:
                self.start_time = time.time()
            if not self.last_action:
                self.last_action = self.start_time
            
            timestamp = time.time() - self.last_action
            self.last_action = time.time()
            self.actions.append(f"sleep({timestamp})\nahk.click()\n")
    
    def record_keyboard(self, key, pressed):
        if not self.stop_recording_flag:
            if not self.start_time:
                self.start_time = time.time()
            if not self.last_action:
                self.last_action = self.start_time
            
            key = self.convert_key_layout(str(key).replace("'", ""))
            timestamp = time.time() - self.last_action
            self.last_action = time.time()
            key = f'\"{key}\"' if "Key" not in key else key
            self.actions.append(f"walk_sleep({timestamp})\nwalk_send({key}, {pressed})\n")
    
    def convert_key_layout(self, key):
        if self.azerty_keyboard:
            azerty_map = {
                'a': 'q', 'q': 'a',
                'w': 'z', 'z': 'w',
                's': 's', 'd': 'd'
            }
            return azerty_map.get(key, key)
        return key

    def save_recording(self):
        with open(self.filename, "a") as f:
            for action in self.actions:
                f.write(action)
        print(f"Actions saved to {self.filename}")
    
    def stop_recording(self):
        self.stop_recording_flag = True

def main():
    print("F1 Start Recording | F2 Stop Recording | F3 Align Roblox Character | Ctrl C exit this window")
    print("Run path.py to test | F1 Exit Path")
    record_path = Path()
    def on_record_hotkey():
        print("Recording with hotkey")
        Thread(target=record_path.start_recording).start()

    with keyboard.GlobalHotKeys({
        '<F1>': on_record_hotkey,
        '<F2>': record_path.stop_recording,
        '<F3>': align_camera,
        '<ctrl>+c': exit
    }) as h:
        h.join()

if __name__ == "__main__":
    main()