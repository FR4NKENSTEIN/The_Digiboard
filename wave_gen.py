import numpy as np
import pygame as pg

sample_rate = 44100

# Note/Frequencies we are using (hertz) 
# will probably shorten this list
frequency_list = [
    207.65, 220.00, 233.08, 246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23,
    369.99, 392.99, 415.30, 440.00, 466.16, 493.88, 523.25, 554.37, 527.33, 622.25
]

# an empty list to hold pg.sound_objects
sound_list = []

# Generates sine waves with the values above
def sine_wave(fr_l):
    # make a special numpy array
    each_sample_number = np.arange(10 * sample_rate)
    # for each frequency...
    for frequency in fr_l:
        # make a sine wave...
        wave_form = np.sin(2 * np.pi * each_sample_number * frequency / sample_rate)
        # then attunate it a bit because noises are loud...
        wave_form *= .3
        # and change them to 16-bit integers as they were float values...
        integer_wave = np.int16(wave_form * 32767)
        # finally turn them into pg.sound_objects...
        new_sound_object = pg.sndarray.make_sound(integer_wave)
        print(f"sound object with {frequency}hz")
        # lastly add it to the list of sound_objects
        sound_list.append(new_sound_object)
    return sound_list