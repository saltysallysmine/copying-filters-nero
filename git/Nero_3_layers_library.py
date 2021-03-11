from PIL import Image
from random import randrange
from math import exp
from datetime import datetime


def create_nero_layer(numb_neros):
    return [[0 for _ in range(numb_neros)] for x in range(2)]


def create_nero_links(numb_inp, numb_out):
    return [[(randrange(11) - 5) / 10 for y in range(numb_out)]
            for x in range(numb_inp)]


def signal_passing(inp, lin, out):
    for jj in range(len(lin[0])):
        out[jj] = 0
        for ii in range(len(lin)):
            out[jj] += (inp[ii] * lin[ii][jj])
            if ii == len(lin) - 1:
                out[jj] = 1 / (1 + exp(-out[jj]))


def find_error(inp, lin, out):
    for ii in range(len(lin)):
        inp[ii] = 0
        for jj in range(len(lin[0])):
            inp[ii] += out[jj] * lin[ii][jj]


def correcting_weights(inp, lin, out):
    for jj in range(len(lin[0])):  # output
        for ii in range(len(lin)):  # input
            lin[ii][jj] += 0.42 * out[1][jj] * out[0][jj] * (1 - out[0][jj]) * inp[0][ii]


def learning(name_img_b, name_img_a, layers_list, links_list, numb_trains=1):
    im_before = Image.open(name_img_b)
    im_after = Image.open(name_img_a)
    pixels_before = im_before.load()
    pixels_after = im_after.load()
    x, y = im_after.size
    for z in range(numb_trains):
        for i in range(x):
            for j in range(y):
                r_b, g_b, b_b = pixels_before[i, j]
                layers_list[0][0][0] = r_b / 255
                layers_list[0][0][1] = g_b / 255
                layers_list[0][0][2] = b_b / 255
                r_a, g_a, b_a = pixels_after[i, j]
                # passing signal
                for lst in range(len(layers_list) - 1):
                    signal_passing(layers_list[lst][0], links_list[lst], layers_list[lst + 1][0])
                # error for output
                layers_list[3][1][0] = r_a / 255 - layers_list[3][0][0]
                layers_list[3][1][1] = g_a / 255 - layers_list[3][0][1]
                layers_list[3][1][2] = b_a / 255 - layers_list[3][0][2]
                # find error
                for lst in range(len(layers_list) - 1, 0, -1):
                    find_error(layers_list[lst - 1][1], links_list[lst - 1], layers_list[lst][1])
                # correcting weights
                for lst in range(len(layers_list) - 1):
                    correcting_weights(layers_list[lst], links_list[lst], layers_list[lst + 1])

        print(f'end {z} iteration')
        print(f'{datetime.now().hour}:{datetime.now().minute}')


def working(name_img_b, name_img_a, layers_list, links_list):
    im = Image.open(name_img_b)
    pixels = im.load()
    x, y = im.size
    im_nero = Image.new('RGB', (x, y), (0, 0, 0))
    pixels_nero = im_nero.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            layers_list[0][0][0] = r / 255
            layers_list[0][0][1] = g / 255
            layers_list[0][0][2] = b / 255
            # pass one signal
            for lst in range(len(layers_list) - 1):
                signal_passing(layers_list[lst][0], links_list[lst], layers_list[lst + 1][0])
            n_r = round(layers_list[3][0][0] * 255)
            n_g = round(layers_list[3][0][1] * 255)
            n_b = round(layers_list[3][0][2] * 255)
            pixels_nero[i, j] = n_r, n_g, n_b
    im_nero.save(name_img_a)
    print('picture changed')


def saving_nero(file_name, links_list):
    with open(file_name, 'w', encoding='utf-8') as fp:
        for lst in range(len(links_list)):
            print(links_list[lst], file=fp)
        fp.close()
    print('links saved')
