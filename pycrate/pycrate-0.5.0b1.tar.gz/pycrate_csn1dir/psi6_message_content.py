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
# * File Name : pycrate_csn1dir/psi6_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.23a Packet System Information Type 6
# top-level object: PSI6 message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.si_18_rest_octets import non_gsm_message_struct

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_bit = CSN1Bit(name='spare_bit')
Spare_bit = spare_bit
Spare_Bit = spare_bit

nongsm_message_struct = CSN1List(name='nongsm_message_struct', list=[
  CSN1Bit(name='nongsm_protocol_discriminator', bit=3),
  CSN1Bit(name='nr_of_container_octets', bit=5, excl=['00000']),
  CSN1Bit(name='container', bit=8, num=([1], lambda x: x))])

psi6_message_content = CSN1List(name='psi6_message_content', list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1Bit(name='psi6_change_mark', bit=2),
  CSN1Bit(name='psi6_index', bit=3),
  CSN1Bit(name='psi6_count', bit=3),
  CSN1List(trunc=True, list=[
    CSN1Ref(name='nongsm_message', obj=non_gsm_message_struct, num=-1),
    CSN1Ref(obj=spare_bit, num=300000),
    CSN1Ref(obj=padding_bits)])])

