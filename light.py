class bulb:
    def __init__(self,isOff):
        self.isOff=isOff
    def on(self):
        self.isOff=False

    def off(self):
        self.isOff=True
    def status(self):
        if self.isOff:
            return "light is off"
        else:
            return "light is on"
bulb1=bulb(True)
print(bulb1.status())
bulb1.off()
print(bulb1.status())
bulb1.on()
print(bulb1.status())

        
