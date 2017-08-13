import os

from modules import cbpi
from modules.core.hardware import SensorPassive
from modules.core.props import Property

TEMP_PATH = '/sys/class/thermal/thermal_zone0/temp'

@cbpi.sensor
class SystemTempSensor(SensorPassive):
    def init(self):
        pass

    def stop(self):
        pass

    def read(self):
        temp = 0.0
        try:
            with open(TEMP_PATH, 'r') as fp:
                temp = float(fp.read().strip('\t\n\r')) / 1000.0
        except Exception,e:
            print 'Error reading system temperature : % s' % e

        if self.get_config_parameter("unit", "C") == "C":
            self.data_received(round(temp, 2))
        else:
            self.data_received(round(9.0 / 5.0 * temp + 32, 2))