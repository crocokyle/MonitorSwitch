from main import set_work
from monitorcontrol import get_monitors

if __name__ == '__main__':
    for monitor in get_monitors():
        with monitor:
            set_work(monitor)