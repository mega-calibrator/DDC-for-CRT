from monitorcontrol import get_monitors
from tkinter.messagebox import showinfo

def main():
    vcp_codes_test = {
    "0x03": "Soft Control",
    "0x0c": "User Color",
    "0x10": "Brightness",
    "0x12": "Contrast",
    "0x14": "Color Preset",
    "0x16": "Red Gain",
    "0x18": "Green Gain",
    "0x1a": "Blue Gain",
    "0x1c": "Focus",
    "0x20": "H Phase",
    "0x22": "H Size",
    "0x24": "H Pin",
    "0x26": "H Pin Balance",
    "0x28": "H Stat conv",
    "0x29": "H RB/G conv",
    "0x2a": "H Lin",
    "0x2c": "H Lin Balance",
    "0x30": "V Phase",
    "0x32": "V Size",
    "0x34": "V Pin",
    "0x36": "V Pin balance",
    "0x38": "V Stat conv",
    "0x39": "V RB/G conv",
    "0x3a": "V Lin",
    "0x3c": "V Lin balance",
    "0x40": "H Key Balance",
    "0x41": "V Key Balance",
    "0x42": "H Keystone",
    "0x43": "V Keystone",
    "0x44": "Rotation",
    "0x46": "Top Corner Flare",
    "0x48": "Top Corner Hook",
    "0x4a": "Bottom Corner Flare",
    "0x4c": "Bottom Corner Hook",
    "0x56": "H Moire",
    "0x58": "V Moire",
    "0x60": "Input Select",
    "0x6c": "Red Bias",
    "0x6e": "Green Bias",
    "0x70": "Blue Bias",
    "0xac": "hsync",
    "0xae": "vsync",
    "0xb6": "Display Type",
    "0xc0": "Usage Time",
    "0xc7": "Reserved",
    "0xc8": "Controller ID",
    "0xca": "OSD",
    "0xcc": "OSD Language",
    "0xcd": "Status",
    "0xd6": "Power Mode",
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

    print("This is a test program to query as many codes as possible from the VCP (virtual control panel)")
    for i, monitor in enumerate(get_monitors()):
        force = False
        normal = False
        with monitor:
            print("\nNow reading monitor ",str(i))
            try:
                print("\nProbing capabilities")
                cape = monitor.get_vcp_capabilities()
            except:
                print("\nCapabilities query not supported")
                force = True
            else:
                print("\nRAW:\n",str(cape),"\n\nCapabilities dict breakdown: ")
                for thing in cape:                
                    print(" ",str(thing)+": "+str(cape[thing]).replace(" ",""))
                    if thing == "type" and cape[thing] == "crt":
                        normal = True

            if force:
                print("\nForce probing vcp (monitor is a CRT or does not support the cap. query)")
                for code in vcp_codes_test:
                    try:
                        codeoutput = monitor.vcp.get_vcp_feature(code=int(code, 16))
                    except:
                        pass
                    else:
                        print(" ",str(codeoutput)," - ",vcp_codes_test[code])
            elif normal:
                print("\Probing vcp normally")
                for code in vcp_codes_test:
                    try:
                        codeoutput = monitor.vcp.get_vcp_feature(code=int(code, 16))
                    except:
                        pass
                    else:
                        print(" ",str(codeoutput)," - ",vcp_codes_test[code])
                
    showinfo(title="Debug", message="all done")