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
# * File Name : pycrate_csn1dir/ec_system_information_type_4.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 9.1.43s EC System information type 4
# top-level object: EC System Information Type 4



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

network_sharing_information_struct = CSN1List(name='network_sharing_information_struct', list=[
  CSN1Bit(name='common_plmn_allowed'),
  CSN1Bit(name='nb_additional_plmns', bit=2),
  CSN1List(num=([1], lambda x: x + 1), list=[
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='mcc', bit=12)])}),
    CSN1Bit(name='mnc', bit=12),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='ncc_permitted', bit=8)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='ec_access_control_class', bit=7),
      CSN1Bit(name='exception_report_status')])})])])

ec_system_information_type_4 = CSN1List(name='ec_system_information_type_4', list=[
  CSN1Bit(name='message_type', bit=3),
  CSN1Bit(name='ec_si_4_index', bit=2),
  CSN1Bit(name='ec_si_4_count', bit=2),
  CSN1Bit(name='ec_si_change_mark', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='network_sharing_information', obj=network_sharing_information_struct)])}),
  CSN1Ref(obj=spare_padding)])

