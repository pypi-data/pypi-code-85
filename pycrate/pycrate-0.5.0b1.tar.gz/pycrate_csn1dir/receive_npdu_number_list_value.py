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
# * File Name : pycrate_csn1dir/receive_npdu_number_list_value.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 24.008 - d90
# section: 10.5.5.11 Receive N‑PDU Numbers list
# top-level object: Receive NPDU Number list value



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

padding_bits = CSN1Alt(name='padding_bits', alt={
  '0000': ('', []),
  None: ('', [])})

receive_npdu_number_list = CSN1List(name='receive_npdu_number_list', list=[
  CSN1Bit(name='sapi', bit=4),
  CSN1Bit(name='receive_npdu_number_value', bit=8),
  CSN1Alt(alt={
    '': ('', [
    CSN1SelfRef()]),
    None: ('', [])})])

nsapi = CSN1Alt(name='nsapi', alt={
  '0101': ('', []),
  '0110': ('', []),
  '0111': ('', []),
  '1000': ('', []),
  '1001': ('', []),
  '1010': ('', []),
  '1011': ('', []),
  '1100': ('', []),
  '1101': ('', []),
  '1110': ('', []),
  '1111': ('', [])})

receive_npdu_number_value = CSN1Alt(name='receive_npdu_number_value', num=8, alt={
  '0': ('', []),
  '1': ('', [])})

receive_npdu_number_list_value = CSN1List(name='receive_npdu_number_list_value', list=[
  CSN1Ref(obj=receive_npdu_number_list),
  CSN1Ref(obj=padding_bits)])

