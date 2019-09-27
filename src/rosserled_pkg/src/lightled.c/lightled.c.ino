/*
 * rosserial FastLED Subscriber
 * "Led subscriber"
 */

#include <ros.h>
#include <std_msgs/String.h>
#include "lib/FastLED/FastLED.h"
#include <std_msgs/ByteMultiArray.h>

#define DATA_PIN 30
#define BRIGHTNESS 200
#define NUM_LEDS 24
CRGB leds[NUM_LEDS]

class NewHardware : public ArduinoHardware
{
  public:
  NewHardware():ArduinoHardware(&Serial1, 115200){};
}

void  massageCb(const std_msgs::ByteMultiArray& arrscan)
{
  int pincolorred;
  int pincolorgreen;
  int pincolorblue;
  int i = 0;
  for(i = 0; i < NUM_LEDS; i++)
  {
    pincolorred = arrscan.data[i*3];
    pincolorgreen = arrscan.data[i*3+1];
    pincolorblue = arrscan.data[i*3+2];
    leds[NUM_LEDS - i].r = pincolorred * 2;
    leds[NUM_LEDS - i].g = pincolorgreen * 2;
    leds[NUM_LEDS - i].b = pincolorblue * 2;
    FastLED.show();
  }
}

ros::NodeHandle_<NewHardware>  nh;
ros::Subscriber<std_msgs::ByteMultiArray> sub("toggle_led", &messageCb);

void setup()
{
  delay(3000);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  FastLED.setBrightness(BRIGHTNESS);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}
