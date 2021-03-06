"""
https://www.patreon.com/posts/midi-music-pygame-python-43826303
We can use pygame's midi interface, we need to set timidity or fluidsynth
running in a separate terminal first
timidity -iA

Fluidsynth seems a bit more robust
fluidsynth -a alsa -m alsa_seq /usr/share/sounds/sf2/FluidR3_GM.sf2

we can record the output with
pacat --record -d alsa_output.pci-0000_00_1f.3.analog-stereo.monitor
| sox -t raw -r 44100  -L -b 16 -c 2 -e signed-integer - "output.wav"

sudo ln -s /usr/lib/x86_64-linux-gnu/alsa-lib/ /usr/lib/alsa-lib
"""

import time
import random

#midi note 10 is 14.47 kilohertz it has no note name
#c minor scale c, d, eflat, f, g, a, b natural
C4 = 60
D4 = 62
EF4 = 63
F4 = 65
G4 = 67
A4 = 69
BN4 = 71

#what we want is a parent function that takes a fadestep, fadesleep,
#and peak volume,
#that handles the fading etc.
#it could also handle the pitch_bends?
#then the other bits are children that implement specfic melodies
def rumbling(midi_out, channel, duration, fadetime, peak_volume):
    """
    Makes a terrifying rumbling noise
    """
    start=time.time()
    volume = 0
    midi_out.note_on(C4-(4*12), volume, channel=channel)
    rise_time = fadetime / peak_volume
    while volume < peak_volume:
        midi_out.note_off(C4-(4*12), volume, channel=channel)
        volume = volume + 1
        midi_out.note_on(C4-(4*12), volume, channel=channel)
        time.sleep(rise_time)

    while (time.time() - start) < (duration - fadetime):
        midi_out.note_off(C4-(4*12), volume, channel=channel)
        midi_out.note_on(C4-(4*12), volume, channel=channel)
        midi_out.note_off(F4-(5*12), velocity=volume, channel=channel)
        midi_out.note_on(F4-(5*12), velocity=volume, channel=channel)
        pitch_bend=random.randrange(-200, 200)
        time.sleep(rise_time)
        midi_out.pitch_bend(pitch_bend, channel=channel)

    midi_out.note_off(F4-(5*12), velocity=volume, channel=channel)
    while volume > 0:
        midi_out.note_off(C4-(4*12), volume, channel=channel)
        volume = volume -1
        midi_out.note_on(C4-(4*12), volume, channel=channel)
        time.sleep(rise_time)

    midi_out.note_off(C4-(4*12), velocity=127, channel=channel)


def tinkly_piano(midi_out, channel, duration, speed = 1.0):
    """
    Makes some tinkly noises, you can change the time between
    notes with the speed parameter
    """
    start=time.time()
    while (time.time() - start) < duration:
        midi_out.note_on(note=A4+12, velocity=127, channel=channel)
        time.sleep(3.3 * speed)
        midi_out.note_on(note=A4+24, velocity=127, channel= channel)
        time.sleep(1.3 * speed)
        midi_out.note_on(note=EF4+24, velocity=70, channel = channel)
        midi_out.note_on(note=F4+24, velocity=70, channel = channel)
        midi_out.note_on(note=A4+24, velocity=70, channel = channel)
        time.sleep(2.2 * speed)

    midi_out.note_off(note=A4+12, velocity=127, channel=channel)
    midi_out.note_off(note=A4+24, velocity=127, channel=channel)
    midi_out.note_off(note=EF4+24, velocity=127, channel=channel)
    midi_out.note_off(note=F4+24, velocity=127, channel=channel)
    midi_out.note_off(note=A4+24, velocity=127, channel=channel)
