"""
https://www.patreon.com/posts/midi-music-pygame-python-43826303
We can use pygame's midi interface, we need to set timidity or fluidsynth 
running in a separate terminal first
timidity -iA

Fluidsynth seems a bit more robust
fluidsynth -a alsa -m alsa_seq /usr/share/sounds/sf2/FluidR3_GM.sf2

sudo ln -s /usr/lib/x86_64-linux-gnu/alsa-lib/ /usr/lib/alsa-lib
"""


import pygame.midi
import time
import threading


def sequence00(midi_out):
    for _ in range(3):
        midi_out.note_on(note=10, velocity=127)
        time.sleep(1.4)
        midi_out.note_on(note=100, velocity=127)
        time.sleep(0.3)
        midi_out.note_on(note=109, velocity=120)
        midi_out.note_on(note=79, velocity=120)
        time.sleep(0.2)

def sequence01(midi_out):
    for _ in range(3):
        time.sleep(0.7)
        midi_out.note_on(note=8, velocity=127)
        time.sleep(1.1)
        midi_out.note_on(note=89, velocity=127)
        time.sleep(0.3)
        midi_out.note_on(note=56, velocity=120)
        midi_out.note_on(note=65, velocity=120)
        time.sleep(0.2)

def sequence02(midi_out):
    for _ in range(40):
        time.sleep(0.1)
        midi_out.note_on(note=20, velocity=127)
        midi_out.note_off(note=20, velocity=0)


if __name__ == '__main__':

    pygame.midi.init()
    pygame.midi.get_device_info(6)
    midi_out = pygame.midi.Output(6, 0)
    seq00=threading.Thread(target=sequence00, args=(midi_out,))
    seq01=threading.Thread(target=sequence01, args=(midi_out,))
    seq02=threading.Thread(target=sequence02, args=(midi_out,))
    seq00.start()
    time.sleep(2.3)
    seq01.start()
    time.sleep(1.3)
    seq02.start()

