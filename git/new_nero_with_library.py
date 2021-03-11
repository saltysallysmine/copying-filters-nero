from pprint import pprint
from datetime import datetime
from Nero_3_layers_library import create_nero_layer, \
    create_nero_links, \
    learning, \
    working, \
    saving_nero


def main():
    print('start working')
    print(f'{datetime.now().hour}:{datetime.now().minute}')

    # creating neuro
    nero_net_layers = [create_nero_layer(3), create_nero_layer(10),
                       create_nero_layer(10), create_nero_layer(3)]
    nero_net_links = [create_nero_links(3, 10),
                      create_nero_links(10, 10),
                      create_nero_links(10, 3)]

    learning('1. before.jpg', '1. after.jpg', nero_net_layers, nero_net_links, 3)

    working('0. have.jpg', 'output.jpg', nero_net_layers, nero_net_links)

    saving_nero('graphs.txt', nero_net_links)

    # print neuro
    for lst in range(len(nero_net_layers) - 1):
        print(f'layer {lst}')
        pprint(nero_net_layers[lst][0])
        print(f'link {lst}{lst + 1}')
        pprint(nero_net_links)
    print(f'layer {len(nero_net_layers) - 1}')
    pprint(nero_net_layers[len(nero_net_layers) - 1][0])

    print('that`s all')
    print(f'{datetime.now().hour}:{datetime.now().minute}')


main()
