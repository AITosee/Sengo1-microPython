from mpython import *
from Sengo1 import *

sengo1 = Sengo1(0x60)


sengo1.begin(i2c)
sengo1.VisionBegin(sengo1_vision_e.kVisionColor)
sengo1.LedSetColor(sentry_led_color_e.kLedWhite, sentry_led_color_e.kLedClose, 1)
sengo1.SetParamNum(sengo1_vision_e.kVisionColor, 1)
sengo1.SetParam(sengo1_vision_e.kVisionColor, [120, 120, 40, 40, 0], 1)
while True:
    count = sengo1.GetValue(sengo1_vision_e.kVisionColor, sentry_obj_info_e.kStatus)
    i = 1
    for count in range(int(count)):
        print("{} {} {} {} {}".format(i, sengo1.GetValue(sengo1_vision_e.kVisionColor, sentry_obj_info_e.kRValue, i), sengo1.GetValue(sengo1_vision_e.kVisionColor, sentry_obj_info_e.kGValue, i), sengo1.GetValue(sengo1_vision_e.kVisionColor, sentry_obj_info_e.kBValue, i), sengo1.GetValue(sengo1_vision_e.kVisionColor, sentry_obj_info_e.kLabel, i)))
        if (sengo1.GetValue(sengo1_vision_e.kVisionColor, sentry_obj_info_e.kLabel, i) == color_label_e.kColorRed):
            print("red")
        i = i + 1
