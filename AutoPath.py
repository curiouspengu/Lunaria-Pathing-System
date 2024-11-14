import sys
import multiprocessing
from time import sleep, time
from pynput.keyboard import Key, Listener

sys.dont_write_bytecode = True

last_event = 0
running = False

file = open("path.py", "a")
key_press_dict = {
    "'w'": False,
    "'a'": False,
    "'s'": False,
    "'d'": False,
    "'e'": False,
    "'f'": False,
    "Key.space": False,
}

def on_press(key):
    global last_event
    global file
    global running

    if key == Key.f2:
        return False
    if key == Key.f1 and running == False:
        running = True
        file.write(f"\n# New Recording\n")
        print("Started Recording")
    elif running == True and key_press_dict[str(key)] == False:
        print(key)
        file.write(f"walk_sleep('{time()-last_event}')\n")
        last_event = time()
        key_press_dict[str(key)] = True
        file.write(f"walk_send({str(key).replace("Key.space", "'space'")}, 'Down')\n")

def on_release(key):
    global last_event
    global file
    if running == True and not key == Key.f1:
        file.write(f"walk_sleep('{time()-last_event}')\n")
        last_event = time()
        file.write(f"walk_send({str(key).replace("Key.space", "'space'")}, 'Up')\n")
    
        
def main():
    print("F1 Start, F2 Stop")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    global file
    file.close()

if __name__ == "__main__":
    main()