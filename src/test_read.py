from monitorcontrol import get_monitors
from tkinter.messagebox import showinfo, askyesno

def main():
    vcp_codes_test = {    
        "0x03": "Soft Control",
        "0x07": "unmarked",
        "0x09": "unmarked",
        "0x0c": "User Color",
        "0x0d": "unmarked",
        "0x0f": "unmarked",
        "0x10": "Brightness",
        "0x12": "Contrast",
        "0x14": "Color Preset",
        "0x15": "unmarked",
        "0x16": "Red Gain",
        "0x18": "Green Gain",
        "0x19": "unmarked",
        "0x1a": "Blue Gain",
        "0x1b": "unmarked",
        "0x1c": "Focus",
        "0x1d": "unmarked",
        "0x20": "H Phase",
        "0x21": "unmarked",
        "0x22": "H Size",
        "0x23": "unmarked",
        "0x24": "H Pin",
        "0x25": "unmarked",
        "0x26": "H Pin Balance",
        "0x27": "unmarked",
        "0x28": "H Stat conv",
        "0x29": "H RB/G conv",
        "0x2a": "H Lin",
        "0x2b": "unmarked",
        "0x2c": "H Lin Balance",
        "0x2d": "unmarked",
        "0x30": "V Phase",
        "0x31": "unmarked",
        "0x32": "V Size",
        "0x33": "unmarked",
        "0x34": "V Pin",
        "0x35": "unmarked",
        "0x36": "V Pin balance",
        "0x37": "unmarked",
        "0x38": "V Stat conv",
        "0x39": "V RB/G conv",
        "0x3a": "V Lin",
        "0x3b": "unmarked",
        "0x3c": "V Lin balance",
        "0x3d": "unmarked",
        "0x3f": "unmarked",
        "0x40": "H Key Balance",
        "0x41": "V Key Balance",
        "0x42": "H Keystone",
        "0x43": "V Keystone",
        "0x44": "Rotation",
        "0x45": "unmarked",
        "0x46": "Top Corner Flare",
        "0x47": "unmarked",
        "0x48": "Top Corner Hook",
        "0x49": "unmarked",
        "0x4a": "Bottom Corner Flare",
        "0x4b": "unmarked",
        "0x4c": "Bottom Corner Hook",
        "0x4d": "unmarked",
        "0x4e": "unmarked",
        "0x4f": "unmarked",
        "0x50": "unmarked",
        "0x51": "unmarked",
        "0x53": "unmarked",
        "0x55": "unmarked",
        "0x56": "H Moire",
        "0x58": "V Moire",
        "0x5f": "unmarked",
        "0x60": "Input Select",
        "0x61": "unmarked",
        "0x67": "unmarked",
        "0x68": "unmarked",
        "0x69": "unmarked",
        "0x6a": "unmarked",
        "0x6c": "Red Bias",
        "0x6e": "Green Bias",
        "0x70": "Blue Bias",
        "0x77": "unmarked",
        "0x79": "unmarked",
        "0x7a": "unmarked",
        "0x7b": "unmarked",
        "0x7d": "unmarked",
        "0x7e": "unmarked",
        "0x7f": "unmarked",
        "0x80": "unmarked",
        "0x81": "unmarked",
        "0x83": "unmarked",
        "0x85": "unmarked",
        "0x89": "unmarked",
        "0x99": "unmarked",
        "0xa1": "unmarked",
        "0xa3": "unmarked",
        "0xa8": "unmarked",
        "0xa9": "unmarked",
        "0xab": "unmarked",
        "0xac": "hsync",
        "0xad": "unmarked",
        "0xae": "vsync",
        "0xaf": "unmarked",
        "0xb1": "unmarked",
        "0xb3": "unmarked",
        "0xb6": "Display Type",
        "0xbf": "unmarked",
        "0xc1": "unmarked",
        "0xc0": "Usage Time",
        "0xc5": "unmarked",
        "0xc7": "Reserved",
        "0xc8": "Controller ID",
        "0xca": "OSD",
        "0xcb": "unmarked",
        "0xcc": "OSD Language",
        "0xcd": "Status",
        "0xd1": "unmarked",
        "0xd3": "unmarked",
        "0xd5": "unmarked",
        "0xd6": "Power Mode",
        "0xd8": "unmarked",
        "0xd9": "unmarked",
        "0xdd": "unmarked",
        "0xdf": "VCP Version",
        "0xe0": "manu-specific",
        "0xe1": "manu-specific",
        "0xe2": "manu-specific",
        "0xe3": "manu-specific",
        "0xe4": "manu-specific",
        "0xe5": "manu-specific",
        "0xe6": "manu-specific",
        "0xe7": "manu-specific",
        "0xe8": "manu-specific",
        "0xe9": "manu-specific",
        "0xea": "manu-specific",
        "0xeb": "manu-specific",
        "0xec": "manu-specific",
        "0xed": "manu-specific",
        "0xee": "manu-specific",
        "0xef": "manu-specific",
        "0xf0": "manu-specific",
        "0xf1": "manu-specific",
        "0xf2": "manu-specific",
        "0xf3": "manu-specific",
        "0xf4": "manu-specific",
        "0xf5": "manu-specific",
        "0xf6": "manu-specific",
        "0xf7": "manu-specific",
        "0xf8": "manu-specific",
        "0xf9": "manu-specific",
        "0xfa": "manu-specific",
        "0xfb": "manu-specific",
        "0xfc": "manu-specific",
        "0xfd": "manu-specific",
        "0xfe": "manu-specific",
        "0xff": "manu-specific",
    }
    print("This is a test program to query as much info as possible from the VCP (virtual control panel)")
    for i, monitor in enumerate(get_monitors()):
        with monitor:
            def probe_sequence():
                for code in vcp_codes_test:
                    try:
                        codeoutput = monitor.vcp.get_vcp_feature(code=int(code, 16))
                    except:
                        pass
                    else:
                        if vcp_codes_test[code] != "unmarked":
                            print(" ",str(codeoutput)," - ",vcp_codes_test[code])
                        else:
                            print(" ",str(codeoutput)," - ",vcp_codes_test[code], "-", code)

            print("\nNow reading monitor ",str(i))
            try:
                print("\nProbing capabilities")
                cap = monitor.get_vcp_capabilities()
            except:
                print("\nCapabilities query not supported... querying user on force probe...")
                if askyesno(title="Force probe?", message="The monitor likely does not support DDC... will you probe the VCP anyway?"):
                    probe_sequence()
            else:
                print("\nRAW:\n",str(cap),"\n\nCapabilities dict breakdown: ")
                for thing in cap:                
                    print(" ",str(thing)+": "+str(cap[thing]).replace(" ",""))
                    
                if cap["type"] == "crt":
                    print("\nMonitor identifies as a CRT... probing vcp normally")
                    probe_sequence()

                elif cap["type"] != "crt":
                    print("\nMonitor identifies as a DDC-compliant non-CRT display...")

    print("\nProgram has finished... now exiting...")
    showinfo(title="Debug", message="all done")