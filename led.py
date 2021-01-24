from gpiozero import LED

class Led():
    led = None
    pin = 0
    def __init__(self, pin):
        self.pin = pin
        self.led = LED(pin)

    def status(self):
        if self.leds_on():
            return 1
        else:
            return 0
    def leds_on(self):
        return self.led.is_active
    def switch_leds(self, on):
        if(on):
            self.led.on()
        else:
            self.led.off()
