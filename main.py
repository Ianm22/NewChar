from time import sleep, time
import keyboard
import json

#  default 0.2
SECONDS_TO_WAIT_PRESSING = 0.2
# 'dvorak' or 'qwerty'.
SELECTED_KEYBOARD = "dvorak"
# Select the shortcut that you want to use for pause/resume the program.
PAUSE_PROGRAM_HOTKEY = 'ctrl+shift+_'
# Stop program.
STOP_PROGRAM_HOTKEY = 'ctrl+shift+{'
# Delay when the new char is write.
DELAY_IN_WRITE = 0.5
# Banned keys.
BANNED_KEYS = ["shift", "ctrl", "alt", "windows", "menu", "caps lock", "left",
               "right", "up", "down", "enter", "space", "backspace", "delete", "tab"]

# Initial state when the program is open.
program_status = True


# Key of keyboard codes.
keyboard_QWERTY_code = {
    16: "q",
    17: "w",
    18: "e",
    19: "r",
    20: "t",
    21: "y",
    22: "u",
    23: "i",
    24: "o",
    25: "p",
    30: "a",
    31: "s",
    32: "d",
    33: "f",
    34: "g",
    35: "h",
    36: "j",
    37: "k",
    38: "l",
    44: "z",
    45: "x",
    46: "c",
    47: "v",
    48: "b",
    49: "n",
    50: "m",
}

keyboard_DVORAK_code = {
    45: "q",
    51: "w",
    32: "e",
    24: "r",
    37: "t",
    20: "y",
    33: "u",
    34: "i",
    31: "o",
    19: "p",
    30: "a",
    39: "s",
    35: "d",
    21: "f",
    22: "g",
    36: "h",
    46: "j",
    47: "k",
    25: "l",
    53: "z",
    48: "x",
    23: "c",
    52: "v",
    49: "b",
    38: "n",
    50: "m",
}

with open("chars.json", "r") as read_file:
    data_chars = json.load(read_file)


def selectDiffrentChars(keyboard_layout, code):
    keyboard.press_and_release("backspace")
    string_to_show = "RELEASE"
    keyboard.write(string_to_show, restore_state_after=False)
    sleep(0.1)

    char = keyboard.read_event()
    while(char.name == keyboard_layout[code] and char.event_type != "up"):
        char = keyboard.read_event()

    keyboard.press("shift")
    for x in string_to_show:
        keyboard.press_and_release("left")
    keyboard.release("shift")

    options = str(data_chars[keyboard_layout[code]]).replace("{", "")
    options = options.replace("}", "")
    options = options.replace(":", "=")
    keyboard.write(options, restore_state_after=False)

    while True:
        test_char = False
        sleep(0.1)
        char = keyboard.read_event()

        try:
            test_char = isinstance(int(char.name), (int))
        except:
            print("is not a number")
            for x in range(len(options) + 1):
                keyboard.press_and_release("backspace")
            break

        if (test_char):
            for x in range(len(options) + 1):
                keyboard.press_and_release("backspace")
            if (char.name in data_chars[keyboard_layout[code]]):
                # The sleep(0.2) is necessary because some chars sometimes doesn't appear.
                sleep(0.2)
                keyboard.write(data_chars[keyboard_layout[code]][char.name],
                               delay=DELAY_IN_WRITE, restore_state_after=False)
                break
            else:
                break


def newChar(code, keyboard_layout):
    if (keyboard_layout == 'qwerty'):
        if (code in keyboard_QWERTY_code):
            if (keyboard_QWERTY_code[code] in data_chars):
                if (len(data_chars[keyboard_QWERTY_code[code]]) > 1):
                    selectDiffrentChars(keyboard_QWERTY_code, code)
                else:
                    keyboard.press_and_release('backspace')
                    keyboard.write(
                        data_chars[keyboard_QWERTY_code[code]]["1"], delay=DELAY_IN_WRITE)
    elif (keyboard_layout == 'dvorak'):
        if (code in keyboard_DVORAK_code):
            if (keyboard_DVORAK_code[code] in data_chars):
                if (len(data_chars[keyboard_DVORAK_code[code]]) > 1):
                    selectDiffrentChars(keyboard_DVORAK_code, code)
                else:
                    keyboard.press_and_release('backspace')
                    keyboard.write(
                        data_chars[keyboard_DVORAK_code[code]]["1"], delay=DELAY_IN_WRITE)

    else:
        raise Exception("Keyboard layout bad selected!")


def changeProgramState():
    global program_status
    program_status = not program_status
    print("Program status:", program_status)


def stopProgram():
    print("Program stopped!")
    quit()


def main():
    keyboard.add_hotkey(PAUSE_PROGRAM_HOTKEY, changeProgramState)
    keyboard.add_hotkey(STOP_PROGRAM_HOTKEY, stopProgram)

    while True:
        sleep(1)

        while program_status:
            key_pressed = keyboard.read_event()

            if (key_pressed.name in BANNED_KEYS):
                continue

            if (key_pressed.event_type != "up"):
                start = time()

                while True:
                    key_pressed = keyboard.read_event()
                    if (key_pressed.name in BANNED_KEYS):
                        break
                    if (key_pressed.event_type != "up"):
                        last_time = time()
                        if (last_time - start > SECONDS_TO_WAIT_PRESSING):
                            newChar(key_pressed.scan_code, SELECTED_KEYBOARD)
                            print("success")
                            break
                    else:
                        break


if __name__ == "__main__":
    main()
