# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/si9_rest_octets.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.37a SI 9 Rest Octets
# top-level object: SI9 rest octets



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

position = CSN1Alt(name='position', alt={
  '0000': ('modulus', [
  CSN1Bit(name='bcch_type')]),
  '0001': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '0010': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '0011': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '0100': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '0101': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '0110': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '0111': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '1000': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '1001': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '1010': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '1011': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '1100': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '1101': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '1110': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')]),
  '1111': ('modulus', [
  CSN1Bit(name='relative_position', bit=([0], lambda x: x + 1)),
  CSN1Bit(name='bcch_type')])})

info_type = CSN1Alt(name='info_type', alt={
  '0': ('', [
  CSN1Bit(name='info_type_4', bit=4)]),
  '10': ('', [
  CSN1Bit(name='info_type_5', bit=5)]),
  '11': ('', [
  CSN1Bit(name='info_type_6', bit=6)])})

positions = CSN1List(name='positions', list=[
  CSN1Ref(obj=position),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(obj=position)])})])

scheduling_info = CSN1List(name='scheduling_info', list=[
  CSN1Ref(obj=info_type),
  CSN1Ref(obj=positions),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1SelfRef()])})])

si9_rest_octets = CSN1List(name='si9_rest_octets', list=[
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(obj=scheduling_info)]),
    'L': ('', [])}),
  CSN1Ref(obj=spare_padding)])

