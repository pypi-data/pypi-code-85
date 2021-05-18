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
# * File Name : pycrate_csn1dir/ia_rest_octets.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.16 IA Rest Octets
# top-level object: IA Rest Octets

# external references
from pycrate_csn1dir.tmgi_ie import tmgi_ie
from pycrate_csn1dir.egprs_modulation_and_coding_scheme_ie import egprs_modulation_and_coding_scheme_ie
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie
from pycrate_csn1dir.packet_timing_advance_ie import packet_timing_advance_ie
from pycrate_csn1dir.egprs_level_ie import egprs_level_ie

_AccessTechnoType_dict = {
    0 : 'GSM P',
    1 : 'GSM E  --note that GSM E covers GSM P',
    2 : 'GSM R  --note that GSM R covers GSM E and GSM P',
    3 : 'GSM 1800',
    4 : 'GSM 1900',
    5 : 'GSM 450',
    6 : 'GSM 480',
    7 : 'GSM 850',
    8 : 'GSM 750',
    9 : 'GSM T 380',
    10 : 'GSM T 410',
    11 : 'unused',
    12 : 'GSM 710',
    13 : 'GSM T 810',
}

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

access_technologies_request_struct = CSN1List(name='access_technologies_request_struct', list=[
  CSN1Bit(name='access_technology_type', bit=4, dic=_AccessTechnoType_dict),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1SelfRef()])})])

egprs_packet_uplink_assignment = CSN1List(name='egprs_packet_uplink_assignment', list=[
  CSN1Bit(name='extended_ra', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='access_technologies_request', obj=access_technologies_request_struct)])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='alpha', bit=4)])}),
    CSN1Bit(name='gamma', bit=5),
    CSN1Bit(name='tbf_starting_time', bit=16),
    CSN1Bit(name='number_of_radio_blocks_allocated', bit=2),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='p0', bit=4),
      CSN1Val(name='', val='0'),
      CSN1Bit(name='pr_mode')])}),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='pfi', bit=7)])})]),
      'L': ('', []),
      None: ('', [])})]),
    '1': ('', [
    CSN1Bit(name='tfi_assignment', bit=5),
    CSN1Bit(name='polling'),
    CSN1Val(name='', val='0'),
    CSN1Bit(name='usf', bit=3),
    CSN1Bit(name='usf_granularity'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='p0', bit=4),
      CSN1Bit(name='pr_mode')])}),
    CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie),
    CSN1Bit(name='tlli_block_channel_coding'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='bep_period2', bit=4)])}),
    CSN1Bit(name='resegment'),
    CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='alpha', bit=4)])}),
    CSN1Bit(name='gamma', bit=5),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='timing_advance_index', bit=4)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='tbf_starting_time', bit=16)])}),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Alt(alt={
        '0': ('', [
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='reported_timeslots', bit=8),
            CSN1Bit(name='tsh', bit=2)])})])})]),
        '1': ('', [
        CSN1Bit(name='rtti_usf_mode'),
        CSN1Bit(name='pdch_pair_indication', bit=3),
        CSN1Bit(name='additional_usf', bit=3, num=([1], lambda x: -1 * (x + -1))),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='usf2', bit=3),
          CSN1Bit(name='additional_usf2', bit=3, num=([-1, 1], lambda x: -1 * (x + -1)))])}),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='reported_timeslots', bit=8),
          CSN1Bit(name='tsh', bit=2)])})])})]),
      'L': ('', []),
      None: ('', [])})])})])

packet_uplink_assignment = CSN1List(name='packet_uplink_assignment', list=[
  CSN1Alt(alt={
    '0': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='alpha', bit=4)])}),
    CSN1Bit(name='gamma', bit=5),
    CSN1Val(name='', val='01'),
    CSN1Bit(name='tbf_starting_time', bit=16),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Bit(name='p0', bit=4),
      CSN1Val(name='', val='0'),
      CSN1Bit(name='pr_mode')]),
      'L': ('', [])})]),
    '1': ('', [
    CSN1Bit(name='tfi_assignment', bit=5),
    CSN1Bit(name='polling'),
    CSN1Val(name='', val='0'),
    CSN1Bit(name='usf', bit=3),
    CSN1Bit(name='usf_granularity'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='p0', bit=4),
      CSN1Bit(name='pr_mode')])}),
    CSN1Bit(name='channel_coding_command', bit=2),
    CSN1Bit(name='tlli_block_channel_coding'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='alpha', bit=4)])}),
    CSN1Bit(name='gamma', bit=5),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='timing_advance_index', bit=4)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='tbf_starting_time', bit=16)])})])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='extended_ra', bit=5)])})]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='pfi', bit=7)])})]),
    'L': ('', []),
    None: ('', [])})])

frequency_parameters_before_time = CSN1Alt(name='frequency_parameters_before_time', alt={
  '00': ('', [
  CSN1Bit(name='maio', bit=6),
  CSN1Bit(name='mobile_allocation', bit=-1)]),
  None: ('', [])})

second_part_packet_assignment = CSN1Alt(name='second_part_packet_assignment', alt={
  'H': ('', [
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='extended_ra', bit=5)])})]),
  'L': ('', []),
  None: ('', [])})

multiple_blocks_packet_downlink_assignment = CSN1List(name='multiple_blocks_packet_downlink_assignment', list=[
  CSN1Bit(name='tbf_starting_time', bit=16),
  CSN1Bit(name='number_of_allocated_blocks', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', [
      CSN1Ref(name='tmgi', obj=tmgi_ie),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='mbms_session_identity', bit=8)])})]),
      '1': ('', [
      CSN1Bit(name='tlli_g_rnti', bit=32),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='length_indicator_of_ms_id', bit=2),
        CSN1Bit(name='ms_id', bit=([1], lambda x: x + 1)),
        CSN1Ref(name='packet_timing_advance', obj=packet_timing_advance_ie),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='alpha', bit=4),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='gamma', bit=5)])})])})])})])})])})])

packet_downlink_assignment = CSN1List(name='packet_downlink_assignment', list=[
  CSN1Bit(name='tlli', bit=32),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tfi_assignment', bit=5),
    CSN1Bit(name='rlc_mode'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='alpha', bit=4)])}),
    CSN1Bit(name='gamma', bit=5),
    CSN1Bit(name='polling'),
    CSN1Bit(name='ta_valid')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='timing_advance_index', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tbf_starting_time', bit=16)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='p0', bit=4),
    CSN1Val(name='', val='0'),
    CSN1Bit(name='pr_mode')])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie),
    CSN1Bit(name='link_quality_measurement_mode', bit=2),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='bep_period2', bit=4)])})]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='pfi', bit=7)])})]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='npm_transfer_time', bit=5)])}),
    CSN1Alt(alt={
      '0': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='event_based_fanr')])})]),
      '1': ('', [
      CSN1Bit(name='event_based_fanr'),
      CSN1Bit(name='pdch_pair_indication', bit=3)])}),
    CSN1Ref(name='downlink_egprs_level', obj=egprs_level_ie)]),
    'L': ('', []),
    None: ('', [])})])

ia_rest_octets = CSN1List(name='ia_rest_octets', list=[
  CSN1Alt(alt={
    'HH': ('', [
    CSN1Alt(alt={
      '00': ('', [
      CSN1Ref(obj=packet_uplink_assignment)]),
      '01': ('', [
      CSN1Ref(obj=packet_downlink_assignment)]),
      '1': ('', [
      CSN1Ref(obj=second_part_packet_assignment)])}),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Bit(name='implicit_reject_cs'),
      CSN1Bit(name='implicit_reject_ps')]),
      'L': ('', []),
      None: ('', [])}),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Bit(name='peo_bcch_change_mark', bit=2),
      CSN1Bit(name='rcc', bit=3)]),
      'L': ('', []),
      None: ('', [])})]),
    'HL': ('', [
    CSN1Bit(name='length_of_frequency_parameters', bit=6),
    CSN1Ref(obj=frequency_parameters_before_time, lref=([1], lambda x: 8 * x)),
    CSN1Bit(name='compressed_inter_rat_ho_info_ind'),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Bit(name='implicit_reject_ps'),
      CSN1Bit(name='peo_bcch_change_mark', bit=2),
      CSN1Bit(name='rcc', bit=3)]),
      'L': ('', []),
      None: ('', [])})]),
    'LH': ('', [
    CSN1Alt(alt={
      '00': ('', [
      CSN1Ref(obj=egprs_packet_uplink_assignment)]),
      '01': ('', [
      CSN1Ref(obj=multiple_blocks_packet_downlink_assignment)]),
      '1': ('', [])}),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Bit(name='implicit_reject_ps'),
      CSN1Bit(name='peo_bcch_change_mark', bit=2),
      CSN1Bit(name='rcc', bit=3)]),
      'L': ('', []),
      None: ('', [])})]),
    'LL': ('', [
    CSN1Bit(name='compressed_inter_rat_ho_info_ind'),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Bit(name='implicit_reject_ps'),
      CSN1Bit(name='peo_bcch_change_mark', bit=2),
      CSN1Bit(name='rcc', bit=3)]),
      'L': ('', []),
      None: ('', [])})])}),
  CSN1Ref(obj=spare_padding)])

