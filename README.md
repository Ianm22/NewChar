# NewChar
## Description
This program will allow you to write an UTF-8 character holding down a key. 

If someone wants to improve this program, it's free to push a pull request or fork the repository!

## Configuration
### Characters configuration
In "chars.json" you can add the char that you want to press and the options that you will output.

- Here is an example:
```
  {
    "a": {
      "1":"á",
      "2":"à"
    },
    "e": {
      "1":"é",
      "2":"è"
    },
  }
```
when the user holds down "a" key, it will show the options " '1'= 'á', '2'= 'à' ".

### Program configuration
In "main.py" there are a few options that you can modify:

```
  #  default 0.2
  SECONDS_TO_WAIT_PRESSING = 0.2

  # 'dvorak' or 'qwerty'.
  SELECTED_KEYBOARD = "qwerty"

  # Select the shortcut that you want to use for pause/resume the program.
  PAUSE_PROGRAM_HOTKEY = 'ctrl+shift+_'

  # Stop program.
  STOP_PROGRAM_HOTKEY = 'ctrl+shift+{'

  # Delay when the new char is write.
  DELAY_IN_WRITE = 0.5
```

## Run
- NOTE: Currently, some programs don't work correctly with this script and can sometimes cause errors on the keyboard. In that case I suggest to use the STOP_PROGRAM_HOTKEY or stop the python process.
- NOTE 2: It's necessary the use of root permisions because the program uses ```/dev/input/input*``` instead X. More info: https://pypi.org/project/keyboard/
```
  $ git clone https://github.com/Ianm22/NewChar.git
  $ cd NewChar
  $ sudo python main.py
```

## Thanks to:
- Thanks to [boppreh](https://github.com/boppreh) for the keyboard library: https://github.com/boppreh/keyboard
