#!/usr/bin/env python3
# pip install  pymodbus
# pip install pyserial-asyncio
#import sys
#import time
#import logging

from pymodbus.client import ModbusSerialClient as ModbusClient

ID_SLAVE_NUMBER = 1

def setup():
    return ModbusClient(method='rtu', port="COM5", baudrate=9600, stopbits=1, databits=8, parity='N', timeout=1, bytesize=8)

def Function01(client, address, num_registers):
    try:
        result = client.read_coils(address, num_registers, ID_SLAVE_NUMBER) 
        return result.registers

    except Exception as e:
        print ("Error while reading coil status  ", e)
        
def Function02(client, address, num_registers):
    try:
        result = client.read_discrete_inputs(address, num_registers, ID_SLAVE_NUMBER) 
        return result.registers

    except Exception as e:
        print ("Error while reading input status  ", e)
        
def Function03(client, address, num_registers):
    try:
        result = client.read_holding_registers(address, num_registers, ID_SLAVE_NUMBER) 
        return result.registers

    except Exception as e:
        print ("Error while reading holding registers  ", e)
        
def Function04(client, address, num_registers):
    try:
        result = client.read_input_registers(address, num_registers, ID_SLAVE_NUMBER) 
        return result.registers

    except Exception as e:
        print ("Error while reading input registers  ", e)
        
def Function05(client, address, value):
    try:
        result = client.write_coil(address, value, ID_SLAVE_NUMBER) 
        return result.registers

    except Exception as e:
        print ("Error while forcing a single coil  ", e)
        
def Function16(client, address, values):
    try:
        result = client.write_registers(address, values, ID_SLAVE_NUMBER) 
        return result.registers

    except Exception as e:
        print ("Error while presseting multiple registers  ", e)
    

