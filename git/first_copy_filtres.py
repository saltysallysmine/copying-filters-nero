from pprint import pprint
from PIL import Image
from random import randrange
from math import exp
from datetime import datetime


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


def main():
    print('start working')
    print(f'{datetime.now().hour}:{datetime.now().minute}')

    # creating neuro
    input_layer = [[0 for _ in range(3)] for x in range(2)]
    links_12 = [[(randrange(11) - 5) / 10 for y in range(10)] for x in range(3)]
    first_layer = [[0 for _ in range(10)] for x in range(2)]
    links_23 = [[(randrange(11) - 5) / 10 for y in range(10)] for x in range(10)]
    second_layer = [[0 for _ in range(10)] for x in range(2)]
    links_34 = [[(randrange(11) - 5) / 10 for y in range(3)] for x in range(10)]
    output_layer = [[0 for _ in range(3)] for x in range(2)]

    # openning first photo
    im_before = Image.open('1. before.jpg')
    im_after = Image.open('1. after.jpg')
    pixels_before = im_before.load()
    pixels_after = im_after.load()
    x, y = im_after.size
    for z in range(3):
        for i in range(x):
            for j in range(y):
                r_b, g_b, b_b = pixels_before[i, j]
                input_layer[0][0] = r_b / 255
                input_layer[0][1] = g_b / 255
                input_layer[0][2] = b_b / 255
                r_a, g_a, b_a = pixels_after[i, j]
                # passing signal
                signal_passing(input_layer[0], links_12, first_layer[0])
                signal_passing(first_layer[0], links_23, second_layer[0])
                signal_passing(second_layer[0], links_34, output_layer[0])
                # error for output
                output_layer[1][0] = r_a / 255 - output_layer[0][0]
                output_layer[1][1] = g_a / 255 - output_layer[0][1]
                output_layer[1][2] = b_a / 255 - output_layer[0][2]
                # find error
                find_error(second_layer[1], links_34, output_layer[1])
                find_error(first_layer[1], links_23, second_layer[1])
                find_error(input_layer[1], links_12, first_layer[1])
                # correcting weights
                correcting_weights(input_layer, links_12, first_layer)
                correcting_weights(first_layer, links_23, second_layer)
                correcting_weights(second_layer, links_34, output_layer)

        print(f'end {z} iteration')
        print(f'{datetime.now().hour}:{datetime.now().minute}')

    # openning second photo
    im_before = Image.open('2. before.jpg')
    im_after = Image.open('2. after.jpg')
    pixels_before = im_before.load()
    pixels_after = im_after.load()
    x, y = im_after.size
    for z in range(3):
        for i in range(x):
            for j in range(y):
                r_b, g_b, b_b = pixels_before[i, j]
                input_layer[0][0] = r_b / 255
                input_layer[0][1] = g_b / 255
                input_layer[0][2] = b_b / 255
                r_a, g_a, b_a = pixels_after[i, j]
                # pass one signal
                signal_passing(input_layer[0], links_12, first_layer[0])
                signal_passing(first_layer[0], links_23, second_layer[0])
                signal_passing(second_layer[0], links_34, output_layer[0])
                # error for output
                output_layer[1][0] = r_a / 255 - output_layer[0][0]
                output_layer[1][1] = g_a / 255 - output_layer[0][1]
                output_layer[1][2] = b_a / 255 - output_layer[0][2]
                # find error
                find_error(second_layer[1], links_34, output_layer[1])
                find_error(first_layer[1], links_23, second_layer[1])
                find_error(input_layer[1], links_12, first_layer[1])
                # correcting weights
                correcting_weights(input_layer, links_12, first_layer)
                correcting_weights(first_layer, links_23, second_layer)
                correcting_weights(second_layer, links_34, output_layer)

        print(f'end {z + 3} iteration')
        print(f'{datetime.now().hour}:{datetime.now().minute}')

    # print neuro
    print('layer1')
    pprint(input_layer)
    print('link12')
    pprint(links_12)
    print('layer2')
    pprint(first_layer)
    print('link23')
    pprint(links_23)
    print('layer3')
    pprint(second_layer)
    print('link34')
    pprint(links_34)
    print('layer4')
    pprint(output_layer)

    # tec
    im = Image.open('0. have.jpg')
    pixels = im.load()
    x, y = im.size
    im_nero = Image.new('RGB', (x, y), (0, 0, 0))
    pixels_nero = im_nero.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            input_layer[0][0] = r / 255
            input_layer[0][1] = g / 255
            input_layer[0][2] = b / 255
            # pass one signal
            signal_passing(input_layer[0], links_12, first_layer[0])
            signal_passing(first_layer[0], links_23, second_layer[0])
            signal_passing(second_layer[0], links_34, output_layer[0])
            n_r = round(output_layer[0][0] * 255)
            n_g = round(output_layer[0][1] * 255)
            n_b = round(output_layer[0][2] * 255)
            pixels_nero[i, j] = n_r, n_g, n_b
    im_nero.save('output.jpg')

    print('picture changed')
    print(f'{datetime.now().hour}:{datetime.now().minute}')

    with open('graphs' + '.' + 'txt', 'w', encoding='utf-8') as fp:
        print(links_12, file=fp)
        print(links_23, file=fp)
        print(links_34, file=fp)
        fp.close()

    print('that`s all')
    print(f'{datetime.now().hour}:{datetime.now().minute}')


main()
