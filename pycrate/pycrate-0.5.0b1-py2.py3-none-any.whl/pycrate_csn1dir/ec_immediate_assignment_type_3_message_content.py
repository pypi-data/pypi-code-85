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
# * File Name : pycrate_csn1dir/ec_immediate_assignment_type_3_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 9.1.68 EC IMMEDIATE ASSIGNMENT TYPE 3
# top-level object: EC Immediate Assignment Type 3 message content



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

acknowledged_access_request_struct = CSN1Alt(name='acknowledged_access_request_struct', alt={
  '00': ('', [
  CSN1Bit(name='short_id', bit=8)]),
  '01': ('', [
  CSN1Bit(name='random_id_low', bit=4)]),
  '10': ('', [
  CSN1Bit(name='random_id_high', bit=12)]),
  '11': ('', [])})

ec_immediate_assignment_type_3_message_content = CSN1List(name='ec_immediate_assignment_type_3_message_content', list=[
  CSN1Bit(name='message_type', bit=4),
  CSN1Bit(name='used_dl_coverage_class', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='ec_page_extension', bit=4)])}),
  CSN1Ref(name='acknowledged_access_request_1', obj=acknowledged_access_request_struct),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='acknowledged_access_request_2', obj=acknowledged_access_request_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='acknowledged_access_request_3', obj=acknowledged_access_request_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='acknowledged_access_request_4', obj=acknowledged_access_request_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='acknowledged_access_request_5', obj=acknowledged_access_request_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='acknowledged_access_request_6', obj=acknowledged_access_request_struct)])}),
  CSN1Ref(obj=spare_padding)])

