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
# * File Name : pycrate_csn1dir/multiple_uplink_assignment_2_ie.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.48a.6 Multiple Uplink Assignment 2
# top-level object: Multiple Uplink Assignment 2 IE

# external references
from pycrate_csn1dir.pulse_format_ie import pulse_format_ie
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie
from pycrate_csn1dir.egprs_level_ie import egprs_level_ie
from pycrate_csn1dir.pdch_pairs_description_ie import pdch_pairs_description_ie
from pycrate_csn1dir.egprs_modulation_and_coding_scheme_ie import egprs_modulation_and_coding_scheme_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

timeslot_description_2_struct = CSN1Alt(name='timeslot_description_2_struct', alt={
  '0': ('', [
  CSN1Bit(name='ms_timeslot_allocation_c1', bit=8),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='ms_timeslot_allocation_c2', bit=8)])})]),
  '1': ('', [
  CSN1Bit(name='alpha_c1', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn0_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn1_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn2_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn3_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn4_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn5_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn6_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn7_c1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='alpha_c2', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn0_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn1_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn2_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn3_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn4_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn5_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn6_c2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn7_c2', bit=5)])})])})

rtti_uplink_tbf_assignment_struct = CSN1List(name='rtti_uplink_tbf_assignment_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='pfi', bit=7)])}),
  CSN1Bit(name='rlc_mode'),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='uplink_egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_timeslots_c1', bit=8),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='reported_timeslots_c2', bit=8)])})])}),
  CSN1Bit(name='usf_granularity'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tbf_uplink_pairs_allocation', bit=('# unresolved: N_PAIRS', lambda: 0))])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='usf_c1', bit=3),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='usf_c2', bit=3)])})]),
    '1': ('', [
    CSN1Bit(name='usf', bit=3),
    CSN1Alt(num=('# unresolved: N_PAIRS', lambda: 0), alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='usf', bit=3)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='usf_2', bit=3),
      CSN1Alt(num=('# unresolved: N_PAIRS', lambda: 0), alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='usf_2', bit=3)])})])})])})])

btti_uplink_tbf_assignment_struct = CSN1List(name='btti_uplink_tbf_assignment_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='pfi', bit=7)])}),
  CSN1Bit(name='rlc_mode'),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='uplink_egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='reported_timeslots_c1', bit=8),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='reported_timeslots_c2', bit=8)])})])}),
  CSN1Bit(name='usf_granularity'),
  CSN1Bit(name='n_ts', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tbf_timeslot_allocation', bit=([-1, 8], lambda x: x + 1))])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='usf_c1', bit=3),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='usf_c2', bit=3)])})]),
    '1': ('', [
    CSN1Bit(name='usf', bit=3),
    CSN1Alt(num=([-1, 8], lambda x: x + 1), alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='usf', bit=3)])})])})])

multiple_uplink_assignment_2_ie = CSN1List(name='multiple_uplink_assignment_2_ie', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)])}),
  CSN1Bit(name='resegment'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='uplink_egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Bit(name='extended_dynamic_allocation'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='p0_c1', bit=4),
    CSN1Bit(name='pr_mode_c1'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='p0_c2', bit=4),
      CSN1Bit(name='pr_mode_c2')])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='tsh', bit=2)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='global_timeslot_description', obj=timeslot_description_2_struct),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='btti_uplink_tbf_assignment', obj=btti_uplink_tbf_assignment_struct)]),
    CSN1Val(name='', val='0')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='uplink_assignment_pdch_pairs_description', obj=pdch_pairs_description_ie)])}),
    CSN1Bit(name='n_pairs', bit=3),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='alpha_c1', bit=4),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='alpha_c2', bit=4)])}),
      CSN1Alt(num=([-1, 2], lambda x: x + 1), alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='gamma', bit=5)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Alt(num=([-1, -1, 2], lambda x: x + 1), alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='gamma', bit=5)])})])})])}),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Bit(name='rtti_usf_mode'),
      CSN1Ref(name='rtti_uplink_tbf_assignment', obj=rtti_uplink_tbf_assignment_struct)]),
    CSN1Val(name='', val='0')])}),
  CSN1Ref(name='uplink_egprs_level', obj=egprs_level_ie),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='pulse_format', obj=pulse_format_ie)])})])

