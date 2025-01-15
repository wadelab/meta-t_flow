from pypixxlib.viewpixx import VIEWPixx3D
# viewpixx and VIEWPixx3D would need to be replaced by the appropriate devices.
my_device = VIEWPixx3D() # Opens and initiates the device
my_device.setVideoMode('C24') # Set the right video mode
my_device.updateRegisterCache() # Update the device