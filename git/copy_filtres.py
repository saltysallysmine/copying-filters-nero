from datetime import datetime
from Nero_3_layers_library import create_nero_links, \
    create_nero_layer, working


def main():
    print('start working')
    print(f'{datetime.now().hour}:{datetime.now().minute}')

    # creating neuro
    nero_net_layers = [create_nero_layer(3), create_nero_layer(10),
                       create_nero_layer(10), create_nero_layer(3)]
    nero_net_links = [[[-1.9524109666462164, 0.794171250724122, 1.183803184789775, 0.19788037756230625,
                        1.0761286838350763, 0.47036020292436187, -1.3450710381698283, 8.021546875850202,
                        10.530480520182653, 0.28058409203467904],
                       [-3.3928935502556907, -6.665357243698409, 7.929684570192148, -6.854399501429683,
                        -8.275178217463694, -7.223888333232535, -4.250902931220512, -14.442353478600909,
                        -11.411291797070731, -6.996960802536583],
                       [-3.9343578436948126, -4.456952284992891, -15.225467761142054, -2.7072165080094392,
                        -2.238018553763329, -2.621831294979116, -4.203891338741272, 17.569951047942,
                        -2.8538181559238462, -2.6099161265044897]], [
                          [-4.903764895515147, -8.133106937410858, -2.115003113730809, -34.25097900290865,
                           -2.423522418164275, -2.3467319245806775, 0.4480149068029911, 5.06844976778818,
                           -3.321623988362295, -1.7510900113073464],
                          [2.26980119909565, -4.6360800124569765, 4.7664747481849306, -20.836113673726608,
                           1.4118186601172067, 2.338600193582846, 2.1232337824737657, 5.773236845109569,
                           -0.14970159922530007, -2.9390746073309795],
                          [-0.06291873877435289, -2.5956560632881525, 0.8329260849845713, 1.0641279146599703,
                           -1.283580805259317, -0.5820244322245866, -2.6828480881909824, -0.9932916837070076,
                           -2.4244612039454676, -3.620465386350973],
                          [-0.8848797173897464, -3.2986027258190815, -2.1756975687089124, -27.771983473318397,
                           0.372128715666403, 0.12229587904125726, 3.313084500679503, 8.110863111793106,
                           -0.6679828963829648, -0.7148724363998616],
                          [-0.9757173124940534, -2.3551333802639487, -0.5654330128716141, -26.86201030361409,
                           -0.2560678544793924, -0.22033746599436776, 3.71482978706593, 7.284207714147638,
                           -0.659879223393013, -1.1417178938026407],
                          [-0.3966272205358514, -1.4181955600691352, -1.6870597807851415, -27.40044013163925,
                           0.20451695578125034, -0.5464831396308836, 3.9421095926225864, 7.929968988454157,
                           -1.0381788830718803, -0.8433607381973603],
                          [-1.4568063613531141, -3.659850535536651, -1.7595883122707143, -29.790778899978225,
                           0.7589560741326674, 0.03815368543077323, 2.282011743286504, 8.462524424872194,
                           -0.8776604130875275, -1.7616750315029264],
                          [-1.1977781305931714, 0.410571531075156, -1.427726509743732, 0.11942360401706126,
                           -4.3753796897194155, -3.261781739132198, -2.503042133261511, -0.8429984355427242,
                           -1.2422524274872746, -1.8298975099042134],
                          [3.07295019086371, 3.5386096754614913, 1.540215761094717, -0.6428003526530719,
                           -5.301847680636713, 1.4721677048375166, 0.8211705210150325, -0.8018894292167085,
                           -2.261966268413456, -4.238130602034179],
                          [-0.694276704512794, -1.6739045368462113, -1.6271792013957092, -27.7702349183758,
                           -0.34469930123770376, -0.09872217995953414, 3.867860916226415, 8.02692770419346,
                           -0.551351813723822, -0.26645387952477567]],
                      [[0.9437287314230176, -0.10404084536170428, 0.005305558538328778],
                       [0.4071419195836176, -0.17574587449219728, -0.11098933494704434],
                       [0.3116537284948162, 0.2012173129655636, -1.104349225800967],
                       [1.8098651718512757, 1.7687251281137093, 0.6333306445807774],
                       [-0.5521076414806279, -0.6996821300614723, -0.7135457586041933],
                       [-0.04281256777476646, 1.004332129944687, -0.14048847133454784],
                       [-0.12234097191992159, -0.7528393547643862, -0.5442840116318515],
                       [-0.7702002991995308, -1.0560813385550092, -0.7859992331197795],
                       [-2.372373141488482, -0.4820632501024965, -0.8096301574283091],
                       [-1.1591338326801999, -0.48215938132706154, 1.7498207887282498]]
                      ]

    name = input()

    print('start developing 1')
    print(f'{datetime.now().hour}:{datetime.now().minute}')

    working(name + '.jpg', name + '_done.jpg', nero_net_layers, nero_net_links)

    print('finish developing 1')
    print(f'{datetime.now().hour}:{datetime.now().minute}')

    print('that`s all')
    print(f'{datetime.now().hour}:{datetime.now().minute}')


main()
