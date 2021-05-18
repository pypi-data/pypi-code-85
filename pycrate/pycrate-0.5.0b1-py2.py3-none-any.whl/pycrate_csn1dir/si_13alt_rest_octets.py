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
# * File Name : pycrate_csn1dir/si_13alt_rest_octets.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.37l SI 13alt Rest Octets
# top-level object: SI 13alt Rest Octets

# external references
from pycrate_csn1dir.frequency_parameters_ie import frequency_parameters_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

pbcch_description_2_struct = CSN1List(name='pbcch_description_2_struct', list=[
  CSN1Bit(name='psi1_repeat_period', bit=4),
  CSN1Bit(name='pb', bit=4),
  CSN1Bit(name='tn', bit=3),
  CSN1Ref(name='pbcch_frequency_description', obj=frequency_parameters_ie)])

si_13alt_rest_octets = CSN1List(name='si_13alt_rest_octets', list=[
  CSN1Ref(name='pbcch_description', obj=pbcch_description_2_struct),
  CSN1Ref(obj=spare_padding)])

