import sys
from time import sleep, time
from pynput.keyboard import Key, Listener
import pathlib
import window   

from ahk import AHK
sys.dont_write_bytecode = True

last_event = 0
running = False

file = open(f"{str(pathlib.Path(__file__).parent.resolve())}/path.py", "a")
key_press_dict = {
    "'w'": False,
    "'a'": False,
    "'s'": False,
    "'d'": False,
    "'e'": False,
    "'f'": False,
    "Key.space": False,
}

ahk = AHK()


def align_camera():
    window.focus_roblox()
    window.get_roblox_window_pos(rx:=[], ry:=[], rw:=[], rh:=[])
    click_menu_button(2)
    sleep(0.1)
    ahk.mouse_move(381 * (rw[0]/1920), 129 * (rh[0]/1080))
    ahk.click()
    sleep(0.1)
    ahk.mouse_drag(button="R", from_position=[rx[0] + rw[0]*0.2, ry[0] + 44 + rh[0]*0.05], x=rx[0] + rw[0]*0.2, y=ry[0] + 400 + rh[0]*0.05, send_mode="Input", speed=1)
    sleep(0.1)
    for i in range(50):
        ahk.click(button="WU")
        sleep(0.01)
    for i in range(15):
        ahk.click(button="WD")
        sleep(0.01)

ahk.add_hotkey("F5", align_camera)

def on_press(key):
    global last_event
    global file
    global running
    global key_press_dict

    try:
        if key == Key.f2:
            return False
        if key == Key.f1 and running == False:
            running = True
            last_event = time()
            file.write(f"\n# New Recording\n")
            print("Started Recording")

        elif running == True and key_press_dict[str(key)] == False:
            print(key)
            file.write(f"walk_sleep('{round(time()-last_event, 3)}')\n")
            last_event = time()
            key_press_dict[str(key)] = True
            file.write(f'walk_send({str(key).replace("Key.space", "space")}, "Down")\n')
    except:
        pass

def on_release(key):
    global key_press_dict
    global last_event
    global file
    try:
        if running == True and not key == Key.f1:
            key_press_dict[str(key)] = False
            file.write(f"walk_sleep('{round(time()-last_event, 3)}')\n")
            last_event = time()
            file.write(f'walk_send("{str(key).replace("Key.space", "space")}", "Up")\n')
    except:
        pass

        
def main():
    print("F1 Start, F2 Stop")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    global file
    file.close()

def click_menu_button(button_num):
    window.get_roblox_window_pos(rx:=[], ry:=[], w:=[], h:=[])
    menu_button_spacing = 54 * (h[0]/1080)
    menu_button_width = 64 * (w[0]/1920)

    start_x = 354 * (h[0]/1080)
    start_y = 11 * (w[0]/1920)

    ahk.mouse_move(x = start_y + (int(menu_button_width/2)), y = start_x + (menu_button_spacing * button_num))
    ahk.click()

ahk.start_hotkeys()

if __name__ == "__main__":
    main()

