import pygame as pg
import numpy as np
import wave_gen as wg

#keys to be used on the keyboard.
keys = ['a','w','s','e','d','f','t','g','y','h','u','j','k','o','l']

#intialize some important things
pg.display.init()
pg.mixer.init(wg.sample_rate, -16, 1, 2048)
pg.mixer.set_num_channels(16)
print('INITALIZED')

# call the sine wave function and give all the frequencies
wg.sine_wave(wg.frequency_list)

#combine the two lists to assign each key on the keyboard to a different frequency
key_sound = dict(zip(keys, wg.sound_list))

is_playing = {k: False for k in keys}

window = pg.display.set_mode((960,540))
pg.display.set_caption('Digiboard')
window.fill((28,28,88))

print('######   Keys: A W S E D F T G Y H U J K O L   ######\n######  Notes: C   D   E F   G   A   B C   D   ######')

# this code will keep things running
while True:
    event = pg.event.wait()

    if event.type in (pg.KEYDOWN, pg.KEYUP):
        key = pg.key.name(event.key)

    if event.type == pg.KEYDOWN:
        if key in key_sound.keys() and not is_playing[key]:
            is_playing[key] = True
            key_sound[key].play(-1, fade_ms=100)

    elif event.type == pg.KEYUP and key in key_sound.keys():
        key_sound[key].fadeout(200)
        is_playing[key] = False
    
    # this will let us close the Digiboard
    if event.type == pg.QUIT:
        pg.quit()

    #allow window fill to take effect
    pg.display.flip()