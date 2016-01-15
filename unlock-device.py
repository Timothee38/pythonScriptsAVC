from com.dtmilano.android.viewclient import ViewClient

device, serial = ViewClient.connectToDeviceOrExit()
if device.checkConnected():
    print("Device connected - serial: {}".format(serial))
    print("Device is going to be unlocked...")
    device.wake()
    device.unlock()
else:
    print("Device is not connected!")
