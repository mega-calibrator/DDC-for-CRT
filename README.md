# DDC-for-CRT

This program creates a GUI with as many CRT related features as are supported by the connected monitor.

<div align="center">
  
![Screenshot of DDC GUI](assets/screenshot.PNG)

</div>

## Credits
rdbende's [Sun-Valley](https://github.com/rdbende/Sun-Valley-ttk-theme) tkinter theme

newAM's [monitorcontrol](https://github.com/newAM/monitorcontrol) API

## Hardware requirements
Your monitor must support [DDC/CI](https://web.archive.org/web/20230504201124/https://www.eevblog.com/forum/projects/i2c-over-cat5e-problem/?action=dlattach;attach=185318)

You must use a VGA connection bridged by a displayport DAC,  HDMI is not supported

Please reach out if you have experience using this program with RAMDACs

## Installing from source
Install [Python](https://www.python.org/downloads/windows/) with `pip` for windows 

clone repository, change to the DDC-for-CRT directory and run

```
pip install --upgrade .
```

## Running

open the executable of your choice ~ legacy build is for windows 7

if installed from source:

run `crtgui` or `crtguiverbose` to see console output
