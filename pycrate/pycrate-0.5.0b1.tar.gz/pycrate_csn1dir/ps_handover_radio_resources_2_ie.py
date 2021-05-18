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
# * File Name : pycrate_csn1dir/ps_handover_radio_resources_2_ie.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.42a PS Handover Radio Resources 2
# top-level object: PS Handover Radio Resources 2 IE

# external references
from pycrate_csn1dir.frequency_parameters_ie import frequency_parameters_ie
from pycrate_csn1dir.dual_carrier_frequency_parameters_ie import dual_carrier_frequency_parameters_ie
from pycrate_csn1dir.global_packet_timing_advance_ie import global_packet_timing_advance_ie
from pycrate_csn1dir.egprs_mode_2_ie import egprs_mode_2_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_bit = CSN1Bit(name='spare_bit')
Spare_bit = spare_bit
Spare_Bit = spare_bit

extension_information = CSN1List(name='extension_information', trunc=True, list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='mtti_downlink_assignment_c1')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='mtti_downlink_assignment_c2')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='mtti_uplink_assignment_c1')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='mtti_uplink_assignment_c2')])}),
  CSN1Bit(name='egprs_packet_downlink_ack_nack_type_3_support'),
  CSN1Ref(obj=spare_bit, num=-1)])

ccn_support_description_struct = CSN1List(name='ccn_support_description_struct', list=[
  CSN1Bit(name='number_cells', bit=7),
  CSN1Bit(name='ccn_supported', num=([0], lambda x: x))])

ps_handover_radio_resources_2_ie = CSN1List(name='ps_handover_radio_resources_2_ie', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='handover_reference', bit=8)])}),
  CSN1Bit(name='arfcn', bit=10),
  CSN1Bit(name='si', bit=2),
  CSN1Bit(name='nci'),
  CSN1Bit(name='bsic', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='ccn_active')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_3g_ccn_active')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='ccn_support_description', obj=ccn_support_description_struct)])}),
  CSN1Alt(alt={
    '01': ('', [
    CSN1Ref(name='frequency_parameters_c1', obj=frequency_parameters_ie),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='frequency_parameters_c2', obj=frequency_parameters_ie)])})]),
    '10': ('', [
    CSN1Ref(name='dual_carrier_frequency_parameters', obj=dual_carrier_frequency_parameters_ie)])}),
  CSN1Bit(name='network_control_order', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='global_packet_timing_advance', obj=global_packet_timing_advance_ie),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='packet_extended_timing_advance', bit=2)])})])}),
  CSN1Bit(name='rlc_reset'),
  CSN1Ref(name='egprs_mode', obj=egprs_mode_2_ie),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='extension_length', bit=6),
    CSN1Ref(obj=extension_information, lref=([1], lambda x: x + 1))])})])

