from datetime import datetime, timedelta


from Sensor_class import Sensor

def load_sensors(config_sensors):
    llista_sensors = list()
    for sensor in config_sensors:
        llista_sensors.append(Sensor(sensor))
        
    llista_timers = configure_timers(llista_sensors)
    
    for sensor, timer in zip(llista_sensors,llista_timers):
        sensor.add_Timer(timer)
        
    return llista_sensors


def calculate_timer(time_interval):
    timer = datetime.now()
    

    if time_interval == "Cada minuto":
        timer = timer + timedelta(minutes=1)
    if time_interval == "Cada hora":
        timer = timer + timedelta(hours=1)
    if time_interval == "Una vez al día":
        timer = timer + timedelta(days=1)
    if time_interval == "Una vez a la semana":
        timer = timer + timedelta(weeks=1)
    return timer
        
    
def configure_timers(llista_sensors):
    llista_timers = list()
    for sensor in llista_sensors:
        time_interval = sensor.time_interval
        llista_timers.append(calculate_timer(time_interval))
    
    return llista_timers