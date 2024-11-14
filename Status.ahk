#Persistent
#SingleInstance, Force
Gui, +AlwaysOnTop +ToolWindow
Gui, Font, s10
Gui, Add, Text, vKeyText, Press any key...

; Initialize variables
LastKey := ""
LastTime := 0
LogFile := A_ScriptDir "\path.ahk"
IdleTimeThreshold := 300
InSleep := false
LastLiftTime := 0
Paused := false

; Write starting path at the beginning of the log
FileAppend, % "; Starting Path...`n`n", % LogFile

; Get the screen width and set the window position
ScreenWidth := A_ScreenWidth
GuiWidth := 150
GuiHeight := 50
xPos := ScreenWidth - GuiWidth
Gui, Show, x%xPos% y0 w%GuiWidth% h%GuiHeight%, Keypress Display

SetTimer, CheckKeyPress, 10
Return

; Define F3 hotkey to exit the script
F3::
    FileAppend, % "Collect()`n`n", % LogFile
    Run autopath.ahk
    ExitApp

; Define F2 hotkey to pause/resume the script
F2::
    Paused := !Paused
    if (Paused) {
        FileAppend, % "; Paused...`n`n", % LogFile
        GuiControl,, KeyText, % "Paused"
    } else {
        GuiControl,, KeyText, % "Press any key..."
    }
Return

CheckKeyPress:
    if (Paused)
        return

    ; Check for A-Z keys and the spacebar
    Loop, 26
    {
        Key := Chr(Asc("A") + A_Index - 1)
        if (GetKeyState(Key, "P"))
        {
            If (LastKey != Key)
            {
                if (LastKey != "")
                {
                    Duration := Ceil(A_TickCount - LastTime, 10)
                    FileAppend, % "walkSleep(" Duration ")`n", % LogFile
                }

                FileAppend, % "walkSend(""" Key """,""Down"")`n", % LogFile
                LastKey := Key
                LastTime := A_TickCount
                InSleep := false
                GuiControl,, KeyText, % "Key: " LastKey
            }
            return
        }
    }

; Check for spacebar
if (GetKeyState("Space", "P"))
    {
        If (LastKey != "Space")
        {
            if (LastKey != "" && LastKey != "Space")
            {
                Duration := Ceil(A_TickCount - LastTime, 10)
                FileAppend, % "walkSleep(" Duration ")`n", % LogFile
            }

            FileAppend, % "Jump()`n", % LogFile
            LastKey := "Space"
            LastTime := A_TickCount
            InSleep := false
            GuiControl,, KeyText, % "Key: Space"
        }
        return
    }
    
    ; Check for released keys (including spacebar reset)
    if (LastKey != "")
    {
        if !GetKeyState(LastKey, "P")
        {
            if (LastKey != "Space")
            {
                Duration := Ceil(A_TickCount - LastTime, 10)
                FileAppend, % "walkSleep(" Duration ")`n", % LogFile
                FileAppend, % "walkSend(""" LastKey """,""Up"")`n", % LogFile
            }

            LastLiftTime := A_TickCount
            LastKey := ""
            GuiControl,, KeyText, % "Press any key..."
        }
    }
    
    ; Check for idle time to log Sleep if no keys are pressed
    if (A_TickCount - LastLiftTime > IdleTimeThreshold && !InSleep && LastLiftTime > 0)
    {
        InSleep := true
        SleepDuration := Ceil(A_TickCount - LastLiftTime, 10)
        FileAppend, % "Sleep, " SleepDuration "`n`n", % LogFile
        LastLiftTime := A_TickCount
    }
Return
F1::Reload
GuiClose:
    FileAppend, % "Collect()`n`n", % LogFile
    ExitApp

; Function to round up to the nearest multiple of 10
Ceil(value, factor) {
    return (value + (factor - 1)) - Mod(value + (factor - 1), factor)
}
