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
# * File Name : pycrate_csn1dir/si_19_rest_octets.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.37g SI 19 Rest Octets
# top-level object: SI 19 Rest Octets



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

la_different_struct = CSN1Alt(name='la_different_struct', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Bit(name='cell_reselect_hysterisis', bit=3)])})

compact_cell_selection_struct = CSN1List(name='compact_cell_selection_struct', list=[
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='bcc', bit=3)]),
    '1': ('', [
    CSN1Bit(name='bsic', bit=6)])}),
  CSN1Bit(name='cell_barred'),
  CSN1Val(name='', val='00'),
  CSN1Ref(name='la_different_parameters', obj=la_different_struct),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='ms_txpwr_max_cch', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='rxlev_access_min', bit=6)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='cell_reselect_offset', bit=6)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='temporary_offset', bit=3),
    CSN1Bit(name='penalty_time', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='time_group', bit=2)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='guar_constant_pwr_blks', bit=2)])})])

compact_neighbour_cell_params_struct = CSN1List(name='compact_neighbour_cell_params_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='start_frequency', bit=10),
    CSN1Ref(name='compact_cell_selection_params', obj=compact_cell_selection_struct),
    CSN1Bit(name='nr_of_remaining_cells', bit=4),
    CSN1Bit(name='freq_diff_length', bit=3),
    CSN1List(num=([3], lambda x: x), list=[
      CSN1Bit(name='frequency_diff', bit=([-1, 4], lambda x: x + 1)),
      CSN1Ref(obj=compact_cell_selection_struct)])]),
  CSN1Val(name='', val='0')])

si_19_rest_octets = CSN1List(name='si_19_rest_octets', list=[
  CSN1Bit(name='si19_change_mark', bit=2),
  CSN1Bit(name='si19_index', bit=3),
  CSN1Bit(name='si19_last'),
  CSN1Ref(name='compact_neighbour_cell_parameters', obj=compact_neighbour_cell_params_struct),
  CSN1Ref(obj=spare_padding)])

