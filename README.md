# reolink_relay
This is a light micropython application that utilises a ESP8266 microcontroller
as an API client for a Reolink NVR with the intention of providing a method of 
remotely triggering an external device such as an audio alarm or strobe light.

## Installation
This build was done using a NodeMCU ESP8266 microcontroller running Micropython 
version 1.19.

[mbremote](https://docs.micropython.org/en/latest/reference/mpremote.html) was 
used to load files and libraries to the microcontroler once the firmware was loaded.
All .py files must be pushed to the root directory of the microcontroller.
Additionally the config.json.example file needs to be renamed to config.json and 
the configuration values updated appropriately.

# Hardware build
The hardware build uses a NodeMCU ESP8266 microcontroller, however any microcontroller 
that supports Micropython should work with minimal change.
The build uses an LCD with 2x16 charactors and a PCF8574 based i2c interface, for IP address 
and error message feedback.
The alarm in this case uses a self modulating piezo buzzer, however any external interface 
could use this control line with appropriate configuration and hardware.
Connectivity information can be found in the reolink_hardware.drawio drawing.


# External Sources
https://peppe8o.com/download/micropython/LCD/i2c_lcd.py
https://peppe8o.com/download/micropython/LCD/lcd_api.py
