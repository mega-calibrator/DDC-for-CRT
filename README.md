# DDC-for-CRT

this program creates a GUI with as many CRT related DDC/CI MCCS features as are supported by the connected monitor

<div align="center">
  
![Screenshot of DDC GUI](assets/screenshot.PNG)

</div>

## Credits
rdbende's [Sun-Valley](https://github.com/rdbende/Sun-Valley-ttk-theme) tkinter theme

newAM's [monitorcontrol](https://github.com/newAM/monitorcontrol) API

## Hardware requirements
your monitor must support DDC/CI MCCS (see [ddcutil docs](https://www.ddcutil.com/mccs_background/) for clarification)

you must use a native VGA connection (RAMDAC) or a VGA connection bridged by a displayport DAC

HDMI DACs are not supported

## Building from source
install [Python](https://www.python.org/downloads/windows/) with `pip` for windows 

clone repository, change to the DDC-for-CRT directory and run

```
pip install --upgrade .
```

## Running
open the executable of your choice ~ legacy build is for windows 7

if installed from source:

run `crtgui` or `crtguiverbose` to see console output

## Usage
use mouse and keyboard to adjust controls usually available in the OSD menu of your PC CRT monitor

save and load profiles of settings

degauss the monitor

## Notes
the refresh button should be used after changing the resolution or settings on the monitor itself

the monitor will forget the changes made over DDC if you for change input, change resolution, etc.
<br/>
please use the apply button to confirm your changes and save to the monitor NVRAM

some monitors support extra "manufacturer specific" AKA unspecified codes, these will vary by model
<br/>
these codes normally adjust controls found in the OSD menu that are not listed in the DDC specifications

some monitors support controls not found in the standard/user OSD menu

unspecified codes may cause unexpected behavior ~ if possible, make a post with your unique findings 

## Disclaimer
I nor any of the contributors to this project are responsible for unexpected behavior of your monitor
