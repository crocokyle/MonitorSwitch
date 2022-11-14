from pprint import pprint
from monitorcontrol import get_monitors, InputSource

import time

class Monitors:
    LG = "UMx57"
    ASUS = "VG27AQ"

def set_work(monitor):
    if (monitor_data := monitor.get_vcp_capabilities()).get('model') == Monitors.LG:
        monitor.set_input_source("COMPOSITE1")
    elif monitor_data.get('model') == Monitors.ASUS:
        monitor.set_input_source("HDMI1")

def set_work(monitor):
    if (monitor_data := monitor.get_vcp_capabilities()).get('model') == Monitors.LG:
        monitor.set_input_source("DVI1")
    elif monitor_data.get('model') == Monitors.ASUS:
        monitor.set_input_source("DP1")

def brute_force_inputs(monitor):
    for monitor in get_monitors():
        with monitor:
            if monitor.get_vcp_capabilities().get('model') == Monitors.LG:
                for source in InputSource:
                    if source != InputSource.OFF:
                        monitor.set_input_source(source)
                        print(source)
                        time.sleep(10)

if __name__ == '__main__':
    for monitor in get_monitors():
        with monitor:
            set_work(monitor)
            set_work(monitor)