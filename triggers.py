import win32com.client
import time
from abc import ABC

class Trigger(ABC):
    def is_triggered(self) -> bool:
        pass

class KeyboardTrigger(Trigger):
    def __init__(self, keyboard_device_id=None) -> None:
        self.keyboard_device_id = keyboard_device_id
        self.device_ids = []

    @staticmethod
    def get_keyboard_device_id() -> str:
        print('Leave your keyboard connected for this step.')
        time.sleep(3)
        print('Detecting connected USB devices, please wait...')
        wmi = win32com.client.GetObject("winmgmts:")
        all_dev_ids = [usb.DeviceID for usb in wmi.InstancesOf("Win32_USBHub")]
        print("Now disconnect the keyboard you'd like to use as a trigger. You have 10 seconds to unplug your device.")
        time.sleep(10)
        wmi = win32com.client.GetObject("winmgmts:")
        keyboardless_dev_ids = [usb.DeviceID for usb in wmi.InstancesOf("Win32_USBHub")]

        if disconnected_device_ids := list(set(all_dev_ids) - set(keyboardless_dev_ids)):
            print(f"Devices disconnected: {disconnected_device_ids}")
            keyboard_device_id = disconnected_device_ids[0]
            if len(disconnected_device_ids) > 1:
                print("Multiple devices were disconnected. Using the first entry: {keyboard_device_id}")

            return keyboard_device_id
        
        raise Exception("No devices were disconnected. Please try again.")

    def _refresh_devices(self):
        wmi = win32com.client.GetObject("winmgmts:")
        self.device_ids = [usb.DeviceID for usb in wmi.InstancesOf("Win32_USBHub")]

    def is_connected(self) -> bool:
        if self.keyboard_device_id is not None:
            self._refresh_devices()
            return self.keyboard_device_id in self.device_ids
        else:
            raise ValueError("No keyboard device ID has been assigned.")

    def is_triggered(self) -> bool:
        return not self.is_connected()

if __name__ == '__main__':
    keyboard_id = KeyboardTrigger.get_keyboard_device_id()
    keyboard_trigger = KeyboardTrigger(keyboard_id)
    KEYBOARD_ID = "USB\\VID_3282&PID_0005\\6&B65A5BC&1&2"

