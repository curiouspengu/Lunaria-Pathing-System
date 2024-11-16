# Settings
developer_walk_speed = 1.25
player_walk_speed = 1 # vip or not

















































from ahk import AHK
import win32gui
from time import sleep

azerty_replace_dict = {"w":"z", "a":"q"}
ahk = AHK()

def walk_time_conversion(d):
    final_walk_time = float(d) * (1.0 + (developer_walk_speed - 1.0) * (1 - player_walk_speed))
    return final_walk_time

def walk_sleep(d):
    sleep(walk_time_conversion(d))

def walk_send(k, t):
    result = lambda t: " " if not t == "" else ""
    ahk.send("{" + k + result(t) + t + "}")

def reset():
    ahk.press("esc")
    sleep(0.1)
    ahk.press("r")
    sleep(0.1)
    ahk.key_press("enter")

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
