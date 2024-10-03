from monitorcontrol import get_monitors
from tkinter.messagebox import showinfo

def main():
    monitors = []
    for i, monitor in enumerate(get_monitors()):
        with monitor:
            print(i)
            try:
                dict = monitor.get_vcp_capabilities()
                string = ""
                for thing in dict:
                    string = string+"_"+str(thing)+"-"+str(dict[thing])
                monitors.append(string.replace(" ","")+"\n")
            except:
                pass
    showinfo(title="Debug", message=monitors)