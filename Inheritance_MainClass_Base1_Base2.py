class TV:
    def __init__(self,brand, channel, price, inches, OnOFF_status,volume):

        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.OnOFF_status = OnOFF_status
        self.volume = volume
    def volume_change(self, value):
        if value<=100:
            self.volume=value
        elif value>self.volume:
            pass
        print("Present volume is", self.volume)
    def channel_change(self,value):
        if value<=50:
            self.channel=value
        elif value>self.channel:
            pass
        print("Present Channel is", self.channel)

    def status(self):
        print(self.brand, "at the channel", self.channel, "and at the volume",  self.volume)

action=TV("Sony",1,15000,32, "On", 50)

action.volume_change(23)
action.channel_change(35)
action.status()

# Child Class One
class plasma(TV):
    def __init__(self, channel, volume, brand):
        self.screen = 'Wide'
        self.thickness = 24
        self.energy_usage = 'High'
        self.Lifespan = 'High'
        self.Refresh_rate = 'Slow'
        self.channel = channel
        self.volume = volume
        self.brand = brand

    def viewingAngle(self):
        print("Viewing Angle is 180 degrees")

    def Backlight(self):
        print("Backlight is OFF")

    def DisplayDetails1(self):
        print("Volume:", self.volume, "Channel: ", self.channel, "Screen: ", self.screen, "Thickness: ", self.thickness,
              "Energy: ", self.energy_usage, "Lifespan: ", self.Lifespan, "Refresh_rate: ", self.Refresh_rate)


# Child Class Two
class LED(TV):
    def __init__(self, channel, volume, brand):
        self.screen = 'Flat'
        self.thickness = 32
        self.energy_usage = 'Low'
        self.Lifespan = 'High'
        self.Refresh_rate = 'Fast'
        self.channel = channel
        self.volume = volume
        self.brand = brand

    def viewingAngle(self):
        print("Viewing Angle is 90 degrees")

    def Backlight(self):
        print("Backlight is ON")

    def DisplayDetails2(self):
        print("Volume:", self.volume, "Channel: ", self.channel, "Screen: ", self.screen, "Thickness: ", self.thickness,
              "Energy: ", self.energy_usage, "Lifespan: ", self.Lifespan, "Refresh_rate: ", self.Refresh_rate)


# The Methods from parent class is called as below:
plasma_display = plasma(50, 50, 'Samsung')
plasma_display.channel_change(12)
plasma_display.volume_change(15)
plasma_display.status()
plasma_display.DisplayDetails1()

LED_display = LED(50, 100, 'LG')
LED_display.volume_change(14)
LED_display.channel_change(21)
LED_display.status()
LED_display.DisplayDetails2()