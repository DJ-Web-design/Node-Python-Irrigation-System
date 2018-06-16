# -*- coding: UTF-8 -*-
from time import sleep
from subprocess import Popen

class Sensor(object):
    def __init__(self):
        self.__initialParams()
        self.run = False


    #########################################################
    #                       PUBLIC METHODS                  #
    #########################################################

    def sensor_data(self, plant, irrigationMethod):
        self.__set_sensorData(plant, irrigationMethod)
        print("The Sensor Data is: Plant Name="+plant+" Irrigation Method="+irrigationMethod)

    def irrigationParams(self, airHumidity, groundHumidity, sun, wind):
        self.__set_humidityData(airHumidity, groundHumidity, sun, wind)

    def calculate(self):
        humidity = self.__calculateHumidity()
        if humidity > self.__get_plantData().humidityRequired:
            return "Pass"
        else:
            return "Run"
    def __count(self):
        counter = 1
        while self.run == True:
            print(counter)
            counter+=1
            sleep(1)

    def start(self):
        self.run = True
        self.process = Popen(executable=self.__count)

    def stop(self):
        self.run = False
    #########################################################
    #                     INTERNALS METHODS                 #
    #########################################################
    def __initialParams(self):
        self.__airHumidity = 0
        self.__groundHumidity = 0
        self.__sun = 0
        self.__wind = 0

    def __calculateHumidity(self):
        __totalHumidity = self.__airHumidity + self.__groundHumidity
        __finalHumidity = __totalHumidity - self.__sun
        return __finalHumidity

    #########################################################
    #                GETTERS AND SETTERS METHODS            #
    #########################################################
    def __set_sensorData(self, plant, method):
        self.__plant = plant
        self.__method = method
        self.__set_plantData(plant)


    def __get_sensorData(self):
        return {
            "plant":self.__plant,
            "method":self.__method
        }
    def __set_humidityData(self, air, ground, sun, wind):
        self.__airHumidity = air
        self.__groundHumidity = ground
        self.__sun = sun
        self.__wind = wind
        self.humidityData = self.__get_humidityData()

    def __get_humidityData(self):
        return {
            "airHumidity": self.__airHumidity,
            "groundHumidity":self.__groundHumidity,
            "sun":self.__sun,
            "wind":self.__wind
        }
    def __set_plantData(self, plant):
        self.plantData = self.__get_plantData()
        pass
    def __get_plantData(self):
        pass

