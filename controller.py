from aurora import *
from setup import *
from effects import *
from nanoleaf import Aurora
import time
sys.path.append('/Users/erling/Projects/')
sys.path.append('/Users/erling/Projects/Yr')
sys.path.append('/Users/erling/Projects/ttt')
sys.path.append('/Users/erling/Projects/CryptoExchange')

from weather import *
from crypto_exchange import *
from ttt.main import *

coins = ('BTC','ETH','IOT','NEO')

my_aurora = Aurora(IP,TOKEN)
my_aurora.on = True
my_aurora.effect = 'Inner Peace'

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

while (True):
    (period,symbol,rain,temp,wind) = get_weather_today()
    if max(symbol) < 3:
        weather_color = color_tier_weather[0]
    elif max(symbol) == 2:
        weather_color = color_tier_weather[1]
    else:
        weather_color = color_tier_weather[2]

    crypto_market = []
    coin_colour = []

    for i, coin in enumerate(coins):
        crypto_market.append(get_change_24h(coin))
        coin_colour.append(color_tier_finance[int(translate(crypto_market[i],0,8,0,7))])


    ol = universal_requests.get_balance("sbanken", SSN, ol_konto)
    ol_colour = color_tier_finance[7-int(translate(ol,0,8000,0,7))]


    colors = (ol_colour,ol_colour,ol_colour,weather_color,weather_color,coin_colour[0],coin_colour[1],coin_colour[2],coin_colour[3])

    print(crypto_market,coin_colour)
    set_rgb_all_panels(my_aurora, colors, layout = 'horizontal', T = 20)
    time.sleep(60)
