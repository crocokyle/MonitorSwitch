from pprint import pprint
from monitorcontrol import get_monitors

import time

class Monitors:
    LG = "UMx57"
    ASUS = "VG27AQ"

def set_work(monitor):
    if (monitor_data := monitor.get_vcp_capabilities()).get('model') == Monitors.LG:
        monitor.set_input_source("DP2")
    elif monitor_data.get('model') == Monitors.ASUS:
        monitor.set_input_source("HDMI1")

def set_peronal(monitor):
    if (monitor_data := monitor.get_vcp_capabilities()).get('model') == Monitors.LG:
        monitor.set_input_source("HDMI1")
    elif monitor_data.get('model') == Monitors.ASUS:
        monitor.set_input_source("DP1")

for monitor in get_monitors():
    with monitor:
        set_work(monitor)
