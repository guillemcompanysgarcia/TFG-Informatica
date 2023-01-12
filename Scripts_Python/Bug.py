# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:37:33 2023

@author: Guillem
"""
import struct


reg1 = 17481
reg2 = 3563



def hex_to_float(hexa):
    return struct.unpack('!f',struct.pack('!I', int(hexa, 16)))[0]


def parse_register(reg, padding):
    
    return f"{reg:#0{padding}x}"
        
resultat = parse_register(reg1, 6) + parse_register(reg2, 6).split('x')[1]  
print(hex_to_float(resultat))