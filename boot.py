# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import esp

esp.osdebug(None)
gc.collect() # active



#esp.osdebug(None)
#import webrepl
#webrepl.start()