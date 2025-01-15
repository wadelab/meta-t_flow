from pypixxlib.viewpixx import VIEWPixx3D

from pypixxlib.datapixx import DATAPixx
import numpy as np

# viewpixx and VIEWPixx3D would need to be replaced by the appropriate devices.
#my_device = VIEWPixx3D() # Opens and initiates the device
#my_device.setVideoMode('C24') # Set the right video mode
#my_device.updateRegisterCache() # Update the device

#import sys
#sys.path.append('/Users/tyrion/Documents/HaoTing/nbackmindwandering/src/pypixxlib-2.0.3917')

myDevice = VIEWPixx3D() # &lt;&lt;&lt;&lt;&lt; We get an error here

# However, in the error mesb sage, no line number was indicated.

myDevice.writeRegisterCache()  # Writes the registers with local register cache.
myDevice.dout.setBitValue(2, 0xFFFFFF) # 0 for instruction

myDevice.writeRegisterCache()
myDevice.close()