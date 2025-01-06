from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, showerror, askokcancel
from monitorcontrol import get_monitors
import sv_ttk
import json

def main():
    window = Tk()
    window.title("DDC/CI for CRT")
    window.tk.call('tk', 'scaling', 1)
    s = ttk.Style()
    if window.winfo_screenheight() < 769 or window.winfo_screenwidth() < 1025:
        lowres = True
        tabfont = 10
        buttonfont = 10
        sliderlength = 256
        entryfont = 10
        padsmall = 0
        padmedium = 0
        padlarge = 0
        padXL = 0
        rightarrowimg = PhotoImage(data=r"iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAYAAADED76LAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAP0lEQVQYlY3PMQ6AIBQE0RePQW0sjOH+jachFMRLUNDykakn2VkGCS8uATca6krK+HalghOOyJzxrCZ+I8ObHahHDJ/5N0/LAAAAAElFTkSuQmCC")
        leftarrowimg = PhotoImage(data=r"iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAYAAADED76LAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAQ0lEQVQYlY3OMQrAIABD0YfHKJ2KYwfvD56mo3gFcRWrYKaQH0L4KyLjXjARHwreHaxIM3x2MAy+LbKzleOTYynjgg72vw2fCIi97QAAAABJRU5ErkJggg==")
    else:
        lowres = False
        tabfont = 18
        buttonfont = 16
        sliderlength = 320
        entryfont = 15
        padsmall = 2
        padmedium = 4
        padlarge = 8
        padXL = 12
        rightarrowimg = PhotoImage(data=r"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAfklEQVQ4jbXTQQrCMBRF0SClCy3ifqSIuAAHIsUV6unAgjEUm6/2TZN74f38pFQEHXpsyrPFYIu7Z44hCRLO3hOWNLjOSEI1GgyF5BCVtLitIen/IdnnkpoJl3ce61f46SU+7MJy3Qm+fAvPrfKpCs4kO6/PFIMzSTcNrAoeAV5STb5AuWlOAAAAAElFTkSuQmCC")
        leftarrowimg = PhotoImage(data=r"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAc0lEQVQ4jb2SQQqAQAgAl4joqRHRNzrE0ksiIqK/dZmOkUjpFnkTnUHFEAwBBCACtaVfgwfOaN/AACOQDE9AkQovHjgKeP0N7r1wJvJd5LnS8zhFJ6bYgNIr0VZxS9KOKSTyF+YvJLZXvpE0dvoqiUAlawf0GU2w8QV3KQAAAABJRU5ErkJggg==")
    window.configure(padx=padlarge, pady=padlarge)

    vcp_codes = {
        "0x12": "Contrast",
        "0x10": "Brightness",
        "0x16": "Red Gain",
        "0x18": "Green Gain",
        "0x1a": "Blue Gain",
        "0x6c": "Red Bias",
        "0x6e": "Green Bias",
        "0x70": "Blue Bias",
        "0x20": "H Phase",
        "0x22": "H Size",
        "0x30": "V Phase",
        "0x32": "V Size",
        "0x24": "H Pin",
        "0x26": "H Pin Balance",
        "0x42": "H Keystone",
        "0x40": "H Key Balance",
        "0x2a": "H Lin",
        "0x2c": "H Lin Balance",
        "0x46": "Top Corner Flare",
        "0x48": "Top Corner Hook",
        "0x4a": "Bottom Corner Flare",
        "0x4c": "Bottom Corner Hook",
        "0x34": "V Pin",
        "0x36": "V Pin balance",
        "0x43": "V Keystone",
        "0x41": "V Key Balance",
        "0x3a": "V Lin",
        "0x3c": "V Lin balance",
        "0x44": "Rotation",
        "0x28": "H Stat conv",
        "0x38": "V Stat conv",
        "0x29": "H RB/G conv",
        "0x39": "V RB/G conv",
        "0x1c": "Focus",
        "0x56": "H Moire",
        "0x58": "V Moire",
        "0x14": "Color Preset",
        "0xe0": "unspecified",
        "0xe1": "unspecified",
        "0xe2": "unspecified",
        "0xe3": "unspecified",
        "0xe4": "unspecified",
        "0xe5": "unspecified",
        "0xe6": "unspecified",
        "0xe7": "unspecified",
        "0xe8": "unspecified",
        "0xe9": "unspecified",
        "0xea": "unspecified",
        "0xeb": "unspecified",
        "0xec": "unspecified",
        "0xed": "unspecified",
        "0xee": "unspecified",
        "0xef": "unspecified",
        "0xf0": "unspecified",
        "0xf1": "unspecified",
        "0xf2": "unspecified",
        "0xf3": "unspecified",
        "0xf4": "unspecified",
        "0xf5": "unspecified",
        "0xf6": "unspecified",
        "0xf7": "unspecified",
        "0xf8": "unspecified",
        "0xf9": "unspecified",
        "0xfa": "unspecified",
        "0xfb": "unspecified",
        "0xfc": "unspecified",
        "0xfd": "unspecified",
        "0xfe": "unspecified",
        "0xff": "unspecified",
    }

    class dong_button():
        def __init__(self, parent, monitor):
            self.parent = parent
            self.monitorobj = monitor

        def make_button(self):
            def dong():
                while True:
                    with self.monitorobj:
                        try:
                            self.monitorobj.vcp.set_vcp_feature(code=1, value=1)
                            showinfo(title='Notice', message='Dong !')
                        except:
                            pass
                        else:
                            break
            self.button = ttk.Button(self.parent, text="Degauss", command=dong, takefocus=False)
            self.button.pack(side=LEFT, expand=YES, padx=padmedium)

    class code_refresher():
        def __init__(self, parent, adjustersdict, displayname):
            self.parent = parent
            self.adjustersdict = adjustersdict
            self.displayname = displayname

        def make_button(self):
            def refresh():
                print("\nNow refreshing values from monitor....")
                for code in self.adjustersdict.keys():
                    with self.adjustersdict[code].monitorobj:
                        new_value = self.adjustersdict[code].monitorobj.vcp.get_vcp_feature(code=int(code, 16))[0]
                    self.adjustersdict[code].slider.set(new_value)
                print("Values refreshed successfully")
                showinfo(title="Notice", message="Values refreshed for "+self.displayname)
            self.button = ttk.Button(self.parent, text="Refresh", command=refresh, takefocus=False)
            self.button.pack(side=LEFT, expand=YES, padx=padmedium)

    class code_saver:
        def __init__(self, parent, adjustersdict, displayname):
            self.parent = parent
            self.adjustersdict = adjustersdict
            self.displayname = displayname

        def make_button(self):    
            def save():
                filename = asksaveasfilename(
                                            initialdir="~",
                                            confirmoverwrite=True, 
                                            initialfile=self.displayname+" profile", 
                                            defaultextension=".json", 
                                            filetypes=[('json files', '*.json'), ('All Files', '**')]
                                            )
                if filename:
                    print("\nSaving values to file.....\n")
                    saved_vcp_codes = {}
                    for code in self.adjustersdict.keys():
                        with self.adjustersdict[code].monitorobj:
                            saved_vcp_codes[code] = self.adjustersdict[code].monitorobj.vcp.get_vcp_feature(code=int(code, 16))[0]
                            print("Saving current value:", saved_vcp_codes[code], "for", vcp_codes[code],)
                    if len(saved_vcp_codes) != 0:
                        with open(filename, "w") as vcp_file:
                            vcp_file.write(json.dumps(saved_vcp_codes, indent=3))
                        print("\nSaving complete for", str(self.displayname)+".....\n")
                        showinfo(title="Notice", message="Values saved to file:\n\n"+filename)
            self.button = ttk.Button(self.parent, text="Save profile", command=save, takefocus=False)
            self.button.pack(side=LEFT, expand=YES, padx=padmedium)

    class code_loader:
        def __init__(self, parent, adjustersdict, displayname):
            self.parent = parent
            self.adjustersdict = adjustersdict
            self.displayname = displayname

        def make_button(self):
            def load():
                filename = askopenfilename(initialdir="~")
                if filename:
                    print("\nNow loading values from file....\n")
                    with open(filename, "r") as vcp_file:
                        saved_vcp_codes = json.loads(vcp_file.read())        
                        for code, saved_value in saved_vcp_codes.items():
                            print("Loading value:", saved_value, "for", vcp_codes[code])
                            self.adjustersdict[code].slider.set(saved_value)
                    print("\nValues loaded for monitor", str(self.displayname)+".....\n")
                    print("\nValues loaded successfully")
                    showinfo(title="Notice", message="Values loaded from file!")
            self.button = ttk.Button(self.parent, text="Load profile", command=load, takefocus=False)
            self.button.pack(side=LEFT, expand=YES, padx=padmedium)

    class code_applier():
        def __init__(self, parent, monitor, displayname):
            self.parent = parent
            self.monitorobj = monitor
            self.displayname = displayname

        def make_button(self):
            def apply():
                with self.monitorobj:
                    while True:
                        try:
                            self.monitorobj.vcp.save_current_settings()
                            showinfo(title='Notice', message='Values applied to '+self.displayname)
                        except:
                            pass
                        else:
                            break
            self.button = ttk.Button(self.parent, text="Apply", command=apply, takefocus=False)
            self.button.pack(side=LEFT, expand=YES, padx=padmedium)

    class adjustment_box:
        def __init__(self, crtcodevalues, parent, monitor, code, index):
            self.parent = parent
            self.code = code
            self.monitorobj = monitor
            self.index = index
            self.codevalues = crtcodevalues
            self.boxvalue = IntVar(value=self.codevalues[0])
            self.label = ttk.Label(self.parent, text=vcp_codes[self.code])
            self.label.grid(row=self.index, column=3, padx=padlarge, sticky=W)

        def new_radiobutton(self):
            self.boxvalue.set(self.boxvalue.get()+1)
            self.radiobox = ttk.Frame(self.parent)
            print("Creating buttons for", vcp_codes[self.code])
            self.radiobox.grid(row=self.index, column=4, sticky=EW, padx=padXL)
            def radio_button_pressed():
                with self.monitorobj:
                    while True:
                        try:
                            self.monitorobj.vcp.set_vcp_feature(code=int(self.code, 16), value=self.boxvalue.get()-1)
                        except:
                            pass
                        else:
                            break

            for option in range(1, self.codevalues[1]+2, 1):  
                self.radio = ttk.Radiobutton(self.radiobox, text=(option), value=option, variable=self.boxvalue, command=radio_button_pressed)
                self.radio.pack(side=LEFT)

        def new_sliderbox(self):
            def field_entered(event):
                newentry = self.boxvalue.get()
                if int(newentry) > 255:
                    self.slider.set(255)
                else:
                    self.slider.set(int(newentry))

            def slider_changed(value):
                self.boxvalue.set(int(float(value)))
                with self.monitorobj:
                    while True:
                        try:
                            self.monitorobj.vcp.set_vcp_feature(code=int(self.code, 16), value=int(self.boxvalue.get()))
                        except:
                            pass
                        else:
                            break
                                
            def buttondown():
                self.downone.state(["disabled"])
                self.slider.set(self.boxvalue.get()-1)
                self.downone.state(["!disabled"])

            def buttonup():
                self.upone.state(["disabled"])
                self.slider.set(self.boxvalue.get()+1)
                self.upone.state(["!disabled"])

            self.slidervalue = ttk.Entry(self.parent, width=4, justify=CENTER, textvariable=self.boxvalue)
            self.slidervalue.bind("<Return>", field_entered)
            self.slidervalue.config(takefocus=0)
            self.downone = ttk.Button(self.parent, image=leftarrowimg, command=buttondown, takefocus=False)
            self.upone = ttk.Button(self.parent,image=rightarrowimg, command=buttonup, takefocus=False)
            print("Creating slider with value", self.boxvalue.get(), "for", vcp_codes[self.code])
            self.slider = ttk.Scale(self.parent, from_=0, to=self.codevalues[1], length=sliderlength, value=self.codevalues[0], command=slider_changed)
            self.slider.grid(row=self.index, column=4, padx=padXL)
            self.downone.grid(row=self.index, column=0, padx=padsmall, pady=padsmall)
            self.slidervalue.grid(row=self.index, column=1, padx=padmedium)
            self.upone.grid(row=self.index, column=2, padx=padsmall, pady=padsmall)

    monitors = get_monitors()
    monitornum = len(monitors)
    loading = Toplevel()
    loading.geometry("320x180")
    loading.title("Loading")
    loading.resizable(False, False)
    loading.protocol("WM_DELETE_WINDOW", False)
    progress = ttk.Progressbar(loading, length=256, maximum=512)
    progress.start()
    progress.pack(anchor=CENTER, expand=YES)
    window.withdraw()
    progress.update()
    print("Welcome to DDC for CRT! Now detecting monitors.....\n")
    print(str(monitornum).strip(), "monitors detected!\n")
    badmonitors = []
    for i, monitor in enumerate(monitors):
        with monitor:
            try:
                monitor.capabilities = monitor.get_vcp_capabilities()
            except:
                print("Monitor", str(i)+": unreadable")
                badmonitors.append(i)
            else:
                print("Monitor", str(i)+":", str(monitor.capabilities["type"]).upper()+", model code:", str(monitor.capabilities["model"]).strip().split(" ")[0])
                if monitor.capabilities["type"].casefold().count("crt") < 1:
                    badmonitors.append(i)
                else:
                    try:
                        monitor.vcp.get_vcp_feature(code=18)
                    except:
                        print("Monitor", i, "is a CRT without DDC support")
                        badmonitors.append(i)
                    else:
                        progress.configure(maximum=((((len(vcp_codes.keys())-32)*(monitornum-len(badmonitors)))+2*(monitornum-len(badmonitors)))+8))
                        progress.update()
    resizable = False
    if monitornum == len(badmonitors):
        progress.stop()
        print("\nNo compatible monitors found.....")
        showerror(title="Oh no.....", message="Sorry!\nDDC for CRT can't connect to your monitors!")
        loading.destroy()
        window.destroy()
    else:
        if len(badmonitors) == 0:
            print("\nAll monitors compatible!")
        else:
            print("\nIncompatible monitors:", badmonitors)
        main_canvas = Canvas(window, highlightthickness=0)
        main_scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=main_canvas.yview)
        main_notebook = ttk.Notebook(main_canvas, padding=4)
        main_canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        main_canvas.configure(yscrollcommand=main_scrollbar.set)
        main_notebook.bind("<Configure>", lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"), width=e.width, height=e.height))
        main_canvas.create_window((0, 0), window=main_notebook, anchor=NW)
        print("\nStarting code detection!")
        for i, monitor in enumerate(monitors):
            print("\nNext monitor:", str(i), "compatible:", str(i not in badmonitors).lower())
            if i not in badmonitors:
                progress.update()
                noteframe = ttk.Frame(main_notebook, padding=4, borderwidth=3)
                noteframe.pack()
                with monitor:
                    while True:
                        try:
                            model = str(monitor.capabilities["model"]).strip().split(" ")[0]
                        except:
                            pass
                        else:
                            break
                    if model == "": 
                        model = "CRT "+str(i+1)
                    main_notebook.add(noteframe, text=model)
                    adjusterindex = 0
                    adjustersdict = {}
                    for code in vcp_codes.keys():
                        progress.update()
                        try:
                            codevalues = monitor.vcp.get_vcp_feature(code=int(code, 16))
                            if codevalues[1] > 0 and codevalues[1] < 256:
                                adjuster = adjustment_box(codevalues, noteframe, monitor, code, adjusterindex)
                                if codevalues[1] > 16:
                                    adjuster.new_sliderbox()
                                    adjusterindex += 1
                                    adjustersdict[code] = adjuster
                                else:
                                    adjuster.new_radiobutton()
                                    adjusterindex += 1
                        except:
                            pass
                    if adjusterindex > 21 and resizable == False:
                        resizable = True
                        main_scrollbar.pack(side=RIGHT, fill=Y)
                        print("\nHigh number of adjustments configured, activating vertical resizability...")
                    buttonframe = ttk.Frame(noteframe, borderwidth=2, relief=SUNKEN)
                    buttonframe.grid(row=adjusterindex+1, column=0, columnspan=5, ipadx=padlarge, ipady=padlarge, pady=padXL)
                    donger = dong_button(buttonframe, monitor)
                    donger.make_button()
                    refresher = code_refresher(buttonframe, adjustersdict, model)
                    refresher.make_button()
                    saver = code_saver(buttonframe, adjustersdict, model)
                    saver.make_button()
                    loader = code_loader(buttonframe, adjustersdict, model)
                    loader.make_button()
                    applier = code_applier(buttonframe, monitor, model)
                    applier.make_button()
                noteframe.columnconfigure(3, weight=1)
        loading.destroy()
        if lowres:
            print("Low resolution detected on main monitor, activating small UI mode...\n")
            s.theme_use("alt")
            s.configure('TNotebook.Tab', font=("",tabfont))
            s.configure('TLabel', font=("",tabfont))
            s.configure('TButton', font=("",buttonfont))
            s.configure('TRadiobutton', font=("",buttonfont))
        else:
            sv_ttk.set_theme("dark")
            s.configure('TNotebook.Tab', font=("", tabfont, "bold"), padding=[20,0])
            s.configure('TLabel', font=("", entryfont, "bold"))
            s.configure('TButton', font=("", buttonfont, "bold"))
            s.configure('TRadiobutton', font=("", buttonfont, "bold"))
        print("\nReady set go!")
        window.deiconify()
        window.resizable(False, resizable)
        window.focus_force()
        window.protocol("WM_DELETE_WINDOW", lambda: window.destroy() if askokcancel("Warning", "Do you want to quit?") else False)
    window.mainloop()