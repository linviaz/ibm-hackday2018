# Accessing Sensor Data with Python:
> Average the temperature readings from the 2 sensors:

```python3
def get_temperature():
    """Average temperature in degrees Celsius from humidity and pressure sensor

    >>> temp1 = get_temperature()
    >>> (isinstance(temp1, float)) and (-50.0 <= temp1 <= 150.0)
    True
    """
    return((sense.get_temperature_from_humidity() + sense.get_temperature_from_pressure()) / 2)
```

# Calibrating the temperature:

> The sensehat sits too close to the Raspberry Pi CPU.
> A function was created to calibrate the temperature reading.

```python3
PI_CPUTEMP_CMD = '/opt/vc/bin/vcgencmd measure_temp'
def get_cpu_temp():
    """Returns the Raspberry Pi CPU Temperature

    >>> type(get_cpu_temp())
    <class 'float'>
    """
    # Check if the command returns a temperature.. if not, return an error?
    stdout_data = subprocess.getoutput(PI_CPUTEMP_CMD)
    return clean_temp(stdout_data.split()[0])

def get_corrected_temp():
    """Returns corrected temperature readings

    >>> type(get_corrected_temp())
    <class 'float'>
    """
    temp = get_temperature()
    cpu_temp = get_cpu_temp()
    temp_calibrated = temp - ((cpu_temp - temp)/5.466) - 5
    return temp_calibrated
```
