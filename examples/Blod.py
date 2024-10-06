from mpython import *
from Sengo1 import *

sengo1 = Sengo1(0x60)


sengo1.begin(i2c)
sengo1.VisionBegin(sengo1_vision_e.kVisionBlob)
sengo1.LedSetColor(sentry_led_color_e.kLedWhite, sentry_led_color_e.kLedClose, 1)
sengo1.SetParamNum(sengo1_vision_e.kVisionBlob, 1)
sengo1.SetParam(sengo1_vision_e.kVisionBlob, [0, 0, 15, 15, color_label_e.kColorWhite], 1)
while True:
    count = sengo1.GetValue(sengo1_vision_e.kVisionBlob, sentry_obj_info_e.kStatus)
    i = 1
    for count in range(int(count)):
        print("{} {} {} {} {} {}".format(i, sengo1.GetValue(sengo1_vision_e.kVisionBlob, sentry_obj_info_e.kXValue, i), sengo1.GetValue(sengo1_vision_e.kVisionBlob, sentry_obj_info_e.kYValue, i), sengo1.GetValue(sengo1_vision_e.kVisionBlob, sentry_obj_info_e.kWidthValue, i), sengo1.GetValue(sengo1_vision_e.kVisionBlob, sentry_obj_info_e.kHeightValue, i), sengo1.GetValue(sengo1_vision_e.kVisionBlob, sentry_obj_info_e.kLabel, i)))
        i = i + 1
