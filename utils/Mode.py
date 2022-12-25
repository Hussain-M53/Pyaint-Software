from utils.settings import *


class Mode:
    def __init__(self):
        self.text1 = "Red"
        self.text2 = "Green"
        self.text3 = "Blue"
        self.isRGB = True
    
    def set_mode_text(self, buttons,t1,t2,t3):
        for btn in buttons:
            if (btn.name == "input_box_rh_text"):
                btn.text = t1
                if self.isRGB:
                    btn.text_color = RED
                else:
                    btn.text_color = PURPLE
            elif (btn.name == "input_box_gs_text"):
                btn.text = t2
                if self.isRGB:
                    btn.text_color = GREEN
                else:
                    btn.text_color = PURPLE
            elif (btn.name == "input_box_bv_text"):
                btn.text = t3
                if self.isRGB:
                    btn.text_color = BLUE
                else:
                    btn.text_color = PURPLE