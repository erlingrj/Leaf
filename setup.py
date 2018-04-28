from nanoleaf import Aurora
from nanoleaf import setup
import time

IP = '192.168.1.2'
TOKEN = 'hwEP4FGOHQhr7coYajZIBagI9jCtWRHD'
PANEL_ID = []
T=20
my_aurora = None

def connect_to_aurora():
    ipAddressList = setup.find_auroras()

    print('Number of Auoras found: %i', len(ipAddressList))
    print('Connecting to first available')

    IP = ipAddressList[0]

    raw_input('Press and hold reset for 5-7s and then enter any key')

    TOKEN = setup.generate_auth_token(IP)

def initialize_aurora():
    my_aurora = Aurora(IP,TOKEN)
    PANEL_ID = update_panel_IDs(my_aurora)

    return my_aurora

def find_auroras():
    ipAddressList = setup.find_auroras()

    print('Number of Auoras found: %i', len(ipAddressList))
    print('Connecting to first available')

    IP = ipAddressList[0]

def update_panel_IDs(my_aurora):
    #Panels
    Panels = []

    #Get the layout
    layout = my_aurora.info['panelLayout']['layout']['positionData']

    #Sort them after horisontal position
    layout = sorted(layout, key=lambda k: k['x'])
    layout = layout[::-1]

    for idx, dict in enumerate(layout):
        Panels.append(dict['panelId'])

    return Panels


def set_hue(my_aurora,hue,sat,bright):
    effect_data = {
        "command": "add",
        "animName": "Ingrids rødfarve",
        "animType": "solid",
        "colorType": "HSB",
        "animeData": None,
        "palette": [
            {
                "hue": hue,
                "saturation": sat,
                "brightness": bright
            },
        ],

    }

    my_aurora.effect_set_raw(effect_data)


def setPanel(panelID, RGB):
    animData = " 1 {} 1 {} {} {} 0 20".format(PANEL_ID[panelID],RGB[0], RGB[1], RGB[2])

    effect_data = {
        "command" : "add",
        "animName" : "The Matrix",
        "animType" : "static",
        "animData" : animData,
        "loop" : False}
    my_aurora.effect_set_raw(effect_data)

if __name__ == '__main__':
    my_aurora = initialize_aurora()
    PANEL_ID = update_panel_IDs(my_aurora)
    set_hue(my_aurora, 100,100,100)
    #setPanel(my_aurora,0,(255,255,255))
