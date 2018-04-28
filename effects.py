import time

color_tier_finance = [(43,201,27),(113,214,20),(184,228,13),(255,242,7),(248,181,16),(242,121,25),(235,60,34),(229,0,43)]
color_tier_weather = [(255,234,74),(255,255,255), (28,44,94)]

def pulse(my_aurora, N=1):
    prev_effect = my_aurora.effect
    for i in range(N):
        print(type(my_aurora.brightness))
        if my_aurora.brightness < my_aurora.brightness_max:
            prev = my_aurora.brightness
            my_aurora.brightness = my_aurora.brightness_max
            time.sleep(0.5)
            my_aurora.brightness = prev
            time.sleep(0.3)
        else:
            my_aurora.brightness = int(my_aurora.brightness_max * 0.7)
            time.sleep(0.3)
            my_aurora.brightness = my_aurora.brightness_max
            time.sleep(0.5)
    my_aurora.effect = prev_effect


def set_rgb_all_panels(my_aurora, colors, layout = 'horizontal', T = 20):
    """ Set all the panels of the nanoleaf to the RGB colors specified in the tuple
    of tuple colors. The layout specifies how they are numbered, i.e. which panel corresponds to the color of color[0] and etc. """


    if layout == 'horizontal':
        #Get panel IDs (Erling added this to the Python API)
        panel_IDs = my_aurora.panel_positions_horizontal
        n = len(panel_IDs)
        animData = []
        #Creating the color data as specified in the API documentation
        for idx, (R,G,B) in enumerate(colors):
            animData.append("{} {} 1 {} {} {} 0 {}".format(n,panel_IDs[idx]['panelId'],R,G,B,T))
        effect_data = {
            "command" : "add",
            "animName" : "Static RGB layout",
            "animType" : "static",
            "animData" : ''.join(animData),
            "loop" : False}

        # Function from the python API
        my_aurora.effect_set_raw(effect_data)

def set_rgb_panel(my_aurora, panel, color, layout='horizontal', T=20):
    # Get the right panel_ID
    panel_ID = my_aurora.panel_positions_horizontal[panel]['panelId']
    (R,G,B) = color
    animData = "1 {} 1 {} {} {} 0 {}".format(panel_ID,color[0],color[1],color[2],T)

    effect_data = {
        "command" : "add",
        "animName" : "RGB layout",
        "animType" : "static",
        "animData" : animData,
        "loop" : False}

    my_aurora.effect_set_raw(effect_data)

if __name__ == '__main__':
    from setup import *
    from nanoleaf import Aurora
    aur = Aurora(IP,TOKEN)

    set_rgb_all_panels(aur, (color_tier[0],color_tier[1],color_tier[2],color_tier[3],color_tier[4],color_tier[5],color_tier[6],color_tier[7],color_tier[7]))
