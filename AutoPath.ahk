#SingleInstance, Force
Gui, New
Gui, Font, s20 , Segoe UI ; Set a larger font size with a blue color
Gui, Add, Text, x10 y10 w280 Center, AutoPath by Allan ; Centered title text
Gui, Font, s10, Segoe UI ; Set a clean font for better readability
Gui, Add, Button, x0 y70 w80 h30 gStart, Start (F1) ; Start button positioned at bottom left
Gui, Add, Button, x80 y70 w80 h30 , Pause (F2)
Gui, Add, Button, x160 y70 w80 h30 , Stop (F3) 
Gui, Add, Button, x270 y70 w30 h30 gInfo, Info ; Info button to the right of Stop
Gui, Show, w300 h100, AutoPath by Allan ; Adjust window size to fit all elements
Return

F1::
    Gosub, Start
Return

Start:
    Run, Status.ahk
Return

Info:
    MsgBox, AutoPath is a keylogger application that records all inputs in a structured format. This format is compatible with path code, allowing for easy copy-pasting directly into the code environment. Please ensure responsible usage of this tool.
Return

F9::Reload
GuiClose:
ExitApp