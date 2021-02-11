"""
https://www.patreon.com/posts/midi-music-pygame-python-43826303
We can use pygame's midi interface, we need to set timidity or fluidsynth 
running in a separate terminal first
timidity -iA

Fluidsynth seems a bit more robust
fluidsynth -a alsa -m alsa_seq /usr/share/sounds/sf2/FluidR3_GM.sf2

we can record the output with
pacat --record -d alsa_output.pci-0000_00_1f.3.analog-stereo.monitor | sox -t raw -r 44100  -L -b 16 -c 2 -e signed-integer - "output.wav"

sudo ln -s /usr/lib/x86_64-linux-gnu/alsa-lib/ /usr/lib/alsa-lib
"""


import pygame.midi
import time
import threading
from  spsounds.midi.sounds import rumbling, tinkly_piano

contrabass=43 #the strings never stop, so you can set up a low rumbling background noise, then slowly do pitch bends to keep it interesting
cello=42
melodic_tom = 117
grand_piano = 0
elec_grand_piano = 2

def playitloud():

    pygame.midi.init()
    pygame.midi.get_device_info(2)
    midi_out = pygame.midi.Output(2, 0)
    midi_out.set_instrument(contrabass,channel = 0)
    midi_out.set_instrument(grand_piano,channel = 1)
    midi_out.set_instrument(elec_grand_piano,channel = 2)
    #https://soundprogramming.net/file-formats/general-midi-instrument-list/
    rumblingthread=threading.Thread(target=rumbling, 
                    args=(midi_out,0, 50, 20, 87), 
                    daemon=False)
    tinklythread00=threading.Thread(target=tinkly_piano, args=(midi_out,1, 120, 0.7), daemon=False)
    midi_out.pitch_bend(1200, channel=2)
    tinklythread01=threading.Thread(target=tinkly_piano, args=(midi_out,2, 120, 1.9), daemon=False)
    tinklythread02=threading.Thread(target=tinkly_piano, args=(midi_out,1, 120, 3.9), daemon=False)
    tinklythread03=threading.Thread(target=tinkly_piano, args=(midi_out,1, 110, 6.9), daemon=False)

    tinklythread00.start()
    time.sleep(0.3)
    tinklythread01.start()
    time.sleep(2.3)
    tinklythread02.start()
    tinklythread03.start()
    rumblingthread.start()

