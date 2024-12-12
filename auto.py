from ahk import AHK
import win32gui
from time import sleep
from pynput.keyboard import Key
from pynput import keyboard

exit_flag = False

azerty_replace_dict = {"w":"z", "a":"q"}
ahk = AHK()

kc = keyboard.Controller()
def walk_time_conversion(d):
    final_walk_time = float(d)
    return final_walk_time

def walk_sleep(d):
    if exit_flag == True:
        exit()
    sleep(walk_time_conversion(d))

def walk_send(k, t):
    if exit_flag == True:
        exit()
    if t == True:
        kc.press(k)
    else:
        kc.release(k)

def exit_program():
    global exit_flag
    exit_flag = True

ahk.add_hotkey("F1", exit_program)
ahk.start_hotkeys()

def align_camera():
    r_pos = window.get_roblox_window_pos()

    pathlib.reset()
    sleep(0.1)
    click_menu_button(2)
    sleep(0.1)
    
    kc.tap("\\")
    sleep(0.1)
    kc.tap(Key.enter)
    sleep(0.1)
    ahk.mouse_drag(button="R", from_position=[r_pos.x + r_pos.width*0.2, r_pos.y + 44 + r_pos.height*0.05], x=r_pos.x + r_pos.width*0.2, y=r_pos.y + 400 + r_pos.height*0.05, send_mode="Input", speed=1)
    sleep(0.1)
    for i in range(50):
        ahk.click(button="WU")
        sleep(0.01)
    for i in range(15):
        ahk.click(button="WD")
        sleep(0.01)
    kc.tap("\\")


def click_menu_button(button_num):
    # rel_pos = window.get_roblox_window_pos()
    # menu_button_spacing = 54 * (rel_pos.height/1080)
    # menu_button_width = 64 * (rel_pos.width/1920)

    # start_y = 367 * (rel_pos.height/1080)
    # start_x = 11 * (rel_pos.width/1920)

    # ahk.mouse_move(x = start_x + (int(menu_button_width/2)), y = start_y + (menu_button_spacing * button_num))
    # ahk.click()

    kc.tap('\\')
    for i in range(4):
        sleep(0.1)
        kc.tap(Key.left) 
    for i in range(5 - button_num):
        sleep(0.1)
        kc.tap(Key.up)
    sleep(0.1)
    kc.tap(Key.enter)
    kc.tap('\\')
    
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_roblox_HWND():
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "roblox" in i[1].lower():
            return i[0]
    return -1

def focus_roblox():
    roblox_hwnd = get_roblox_HWND()
    if roblox_hwnd == -1:
        return -1
    win32gui.ShowWindow(roblox_hwnd, 5)
    win32gui.SetForegroundWindow(roblox_hwnd)

def get_roblox_window_pos():
    position = ahk.win_get_position(title=win32gui.GetWindowText(get_roblox_HWND()))
    if position.x == -8 and position.y == -8:
        position1 = Position()
        position1.x = 0
        position1.y = 23
        position1.width = position.width - 16
        position1.height = position.height - 24
        return position1
    return position

