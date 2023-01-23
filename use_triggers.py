from triggers import Trigger, KeyboardTrigger
from main import set_work, set_personal
from monitorcontrol import get_monitors

import time


# HINT: Use KeyboardTrigger.get_keyboard_device_id()
KEYBOARD_ID = "USB\\VID_3282&PID_0005\\6&B65A5BC&1&2"
DESIRED_INPUT = set_work

def main_loop(trigger: Trigger, desired_input: callable):
    time_untriggered_ms = 0
    is_here = True
    while True:
        time.sleep(0.01)
        if trigger.is_triggered() and is_here:
            if time_untriggered_ms >= 100:
                print("Triggered, switching inputs")
                for monitor in get_monitors():
                    with monitor:
                        desired_input(monitor)
                is_here = False
        if trigger.is_connected():
            time_untriggered_ms = 0
            is_here = True
        time_untriggered_ms += 10

if __name__ == '__main__':
    trigger = KeyboardTrigger(KEYBOARD_ID)
    main_loop(trigger, DESIRED_INPUT)
    