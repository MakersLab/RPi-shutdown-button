# RPi-shutdown-button
Code and help for our shutdown button.

HOW-TO:
copy shutdown_pi.py to your home folder and make it hidden, if you want (rename it to have "." as first letter in name... it will be ".shutdown_pi.py")
to have it start automaticaly at boot edit /etc/rc.local and add "python3 /home/pi/name_of_file.py"

HW-SETTINGS:
as shutdown_pi says, use pins for LED and BUTTON.
By default, button is connected to pin 29(BOARD numbering)
and LED is connected to pin 40(BOARD numbering).
Both of them are also connected to ground pin.(choose any of them, RPi provides 8 GND pins)
