import analisis
class Store(object):
    def __init__(self):
        self.Sensor = analisis.Sensor()

    def set_plant(self, plant_name, irrigation_method):
        self.Sensor.sensor_data(plant_name, irrigation_method)
        print('The plant is ' + str(plant_name) + ', irrigation method is: ' + str(irrigation_method))
