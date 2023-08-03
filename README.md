# epaper

This is a fork on (geekpi's Epaper library)[https://github.com/geeekpi/epaper]. It's basically the same as the original one, but provides a set of functions to paste images and text to the epaper display.

This is a library driven by 52Pi E-ink, which can drive 2.13 inch electronic paper and other sizes of electronic paper.
* Currently, only 2.13 inch screen support is provided.
- [] 2.13 Inch E-Ink
## How to use it
* Snap the 2.13 inch epaper hat board into the Raspberry Pi GPIO
* OS Requirement: Raspberry Pi OS 
* Enable `SPI` interface via `sudo raspi-config` tool.
* Install `Pillow`, `spidev`, `RPi.GPIO` libraries.
* Download demo code by:
```bash
cd ~
git clone https://github.com/geeekpi/epaper.git
cd epaper/
python3 eink2.13_demo.py
```
And the display will flash `red`, `black`, `white` and finally a picture.

