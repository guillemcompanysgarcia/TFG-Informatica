# -*- coding: utf-8 -*-

from pymodbus.client import (
    ModbusSerialClient as ModbusClient,
)  # Import the ModbusSerialClient class from the pymodbus library

# which allows the user to establish communication with a Modbus slave device

import struct  # Import struct library which is used to unpack the data received from the Modbus slave device


# ID of the slave number to communicate with
ID_SLAVE_NUMBER = 1


def setup():
    """
    Function to setup the modbus client
    Returns:
        The ModbusClient object for communication
    """
    return ModbusClient(
        method="rtu",
        port="/dev/ttyUSB0",
        baudrate=9600,
        stopbits=1,
        databits=8,
        parity="N",
        timeout=1,
        bytesize=8,
    )


def Function01(client, address, num_registers):
    """
    Function to read coils
    Parameters:
        client: The modbus client to communicate with
        address: The address to read coils from
        num_registers: The number of registers to read
    Returns:
        the value read
    """
    try:
        result = client.read_coils(
            address, num_registers, ID_SLAVE_NUMBER
        )  # sending command to read coils
        resultat = (
            parse_register(result.registers[0], 6)
            + parse_register(result.registers[1], 6).split("x")[1]
        )  # process the registers to be in hexa
        return hex_to_float(resultat)  # return the float

    except Exception as e:
        print("Error while reading coil status  ", e)


def Function02(client, address, num_registers):
    """
    Function to read discrete inputs
    Parameters:
        client: The modbus client to communicate with
        address: The address to read discrete inputs from
        num_registers: The number of registers to read
    Returns:
        the value read
    """
    try:
        result = client.read_discrete_inputs(
            address, num_registers, ID_SLAVE_NUMBER
        )  # sending command to read discrete inputs
        resultat = (
            parse_register(result.registers[0], 6)
            + parse_register(result.registers[1], 6).split("x")[1]
        )  # process the registers to be in hexa
        return hex_to_float(resultat)  # return the float

    except Exception as e:
        print("Error while reading input status  ", e)


def Function03(client, address, num_registers):
    """
    Function to read holding registers
    Parameters:
        client: The modbus client to communicate with
        address: The address to read holding registers from
        num_registers: The number of registers to read
    Returns:
        the value read
    """
    try:
        result = client.read_holding_registers(
            address, num_registers, ID_SLAVE_NUMBER
        )  # sending command to read holding registers
        resultat = (
            parse_register(result.registers[0], 6)
            + parse_register(result.registers[1], 6).split("x")[1]
        )  # process the registers to be in hexa
        return hex_to_float(resultat)  # return the float

    except Exception as e:
        print("Error while reading holding registers  ", e)


def Function04(client, address, num_registers):
    try:
        result = client.read_input_registers(
            address, num_registers, ID_SLAVE_NUMBER
        )  # sending command to read input registers
        resultat = (
            parse_register(result.registers[0], 6)
            + parse_register(result.registers[1], 6).split("x")[1]
        )  # process the registers to be in hexa
        return hex_to_float(resultat)  # return the float

    except Exception as e:
        print("Error while reading input registers  ", e)


def Function05(client, address, value):
    try:
        result = client.write_coil(
            address, value, ID_SLAVE_NUMBER
        )  # sending command to write coils
        resultat = (
            parse_register(result.registers[0], 6)
            + parse_register(result.registers[1], 6).split("x")[1]
        )  # process the registers to be in hexa
        return hex_to_float(resultat)  # return the float

    except Exception as e:
        print("Error while forcing a single coil  ", e)


def Function16(client, address, values):
    try:
        result = client.write_registers(
            address, values, ID_SLAVE_NUMBER
        )  # sending command to write registers
        resultat = (
            parse_register(result.registers[0], 6)
            + parse_register(result.registers[1], 6).split("x")[1]
        )  # process the registers to be in hexa
        return hex_to_float(resultat)  # return the float

    except Exception as e:
        print("Error while presseting multiple registers  ", e)


def hex_to_float(hexa):
    """
    Convert hexa to float
    Parameters:
        hexa (str): hexa string
    Returns:
        float: equivalent float value of the hexa
    """
    return struct.unpack("!f", struct.pack("!I", int(hexa, 16)))[0]


def parse_register(reg, padding):
    """
    Convert register to hex string
    Parameters:
        reg (int): register value
        padding (int): number of digits in the resulting hex string
    Returns:
        str: hex string of the register value
    """
    return f"{reg:#0{padding}x}"
