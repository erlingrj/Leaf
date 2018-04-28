from nanoleaf import Aurora
from setup import IP, TOKEN
import time
import sys

sys.path.append('/Users/erling/Projects')
import Nanoleaf.setup




class Aurora2(Aurora):
    def pulse(self, N = 1):
        for i in range(0,N):
            if self.brightness < self.brightness_max:
                prev = self.brightness
                self.brightness = self.brightness_max
                time.sleep(0.5)
                self.brightness = prev
                time.sleep(0.3)
            else:
                self.brightness = int(self.brightness_max * 0.7)
                time.sleep(0.3)
                self.brightness = self.brightness_max
                time.sleep(0.5)

    def set_rgb_panel(self, panel_id, color):
        print('not finished bro')

    def get_panel_position_horizontal(self):
        # Still workin'
        print(1)

if __name__ == '__main__':
    a = Aurora2(IP,TOKEN)
    a.pulse(N=2)
