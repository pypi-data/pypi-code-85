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
# * File Name : pycrate_csn1dir/psi2_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.19 Packet System Information Type 2
# top-level object: PSI2 message content

# external references
from pycrate_csn1dir.non_gprs_cell_options_ie import non_gprs_cell_options_ie
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.cell_identification_ie import cell_identification_ie
from pycrate_csn1dir.gprs_mobile_allocation_ie import gprs_mobile_allocation_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

reference_frequency_struct = CSN1List(name='reference_frequency_struct', list=[
  CSN1Bit(name='rfl_number', bit=4),
  CSN1Bit(name='length_of_rfl_contents', bit=4),
  CSN1Bit(name='rfl_contents', bit=8, num=([1], lambda x: x + 3))])

gprs_mobile_allocations_struct = CSN1List(name='gprs_mobile_allocations_struct', list=[
  CSN1Bit(name='ma_number', bit=4),
  CSN1Ref(name='gprs_mobile_allocation', obj=gprs_mobile_allocation_ie)])

number_of_idle_blocks_struct = CSN1List(name='number_of_idle_blocks_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='nib_ccch_0', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='nib_ccch_1', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='nib_ccch_2', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='nib_ccch_3', bit=4)])})])

compact_control_info_struct = CSN1List(name='compact_control_info_struct', list=[
  CSN1Bit(name='large_cell_operation'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='number_of_idle_blocks', obj=number_of_idle_blocks_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='n_ccch_nh', bit=4)])})])

hopping_pccch_carriers_struct = CSN1List(name='hopping_pccch_carriers_struct', list=[
  CSN1Bit(name='maio', bit=6),
  CSN1Bit(name='timeslot_allocation', bit=8)])

cell_allocation_struct = CSN1Bit(name='cell_allocation_struct', bit=4)

additional_psi_messages_struct = CSN1List(name='additional_psi_messages_struct', list=[
  CSN1Bit(name='non_gsm_information', bit=2),
  CSN1Bit(name='psi8_broadcast'),
  CSN1Bit(name='psi3ter_broadcast'),
  CSN1Bit(name='psi3quater_broadcast')])

reference_frequency_lists_struct = CSN1List(name='reference_frequency_lists_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(obj=reference_frequency_struct)]),
  CSN1Val(name='', val='0')])

hopping_pccch_carriers_lists_struct = CSN1List(name='hopping_pccch_carriers_lists_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(obj=hopping_pccch_carriers_struct)]),
  CSN1Val(name='', val='0')])

non_hopping_pccch_carriers_struct = CSN1List(name='non_hopping_pccch_carriers_struct', list=[
  CSN1Bit(name='arfcn', bit=10),
  CSN1Bit(name='timeslot_allocation', bit=8)])

gprs_mobile_allocations_lists_struct = CSN1List(name='gprs_mobile_allocations_lists_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(obj=gprs_mobile_allocations_struct)]),
  CSN1Val(name='', val='0')])

cell_allocation_lists_struct = CSN1List(name='cell_allocation_lists_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(obj=cell_allocation_struct)]),
  CSN1Val(name='', val='0')])

non_hopping_pccch_carriers_lists_struct = CSN1List(name='non_hopping_pccch_carriers_lists_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(obj=non_hopping_pccch_carriers_struct)]),
  CSN1Val(name='', val='0')])

pccch_description_struct = CSN1List(name='pccch_description_struct', list=[
  CSN1Bit(name='tsc', bit=3),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Ref(name='non_hopping_pccch_carriers', obj=non_hopping_pccch_carriers_lists_struct)]),
    '1': ('', [
    CSN1Bit(name='ma_number', bit=4),
    CSN1Ref(name='hopping_pccch_carriers', obj=hopping_pccch_carriers_lists_struct)])})])

pccch_description_lists_struct = CSN1List(name='pccch_description_lists_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(obj=pccch_description_struct)]),
  CSN1Val(name='', val='0')])

psi2_message_content = CSN1List(name='psi2_message_content', trunc=True, list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1Bit(name='psi2_change_mark', bit=2),
  CSN1Bit(name='psi2_index', bit=3),
  CSN1Bit(name='psi2_count', bit=3),
  CSN1List(list=[
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='cell_identification', obj=cell_identification_ie)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='non_gprs_cell_options', obj=non_gprs_cell_options_ie)])}),
    CSN1Ref(name='reference_frequency_lists', obj=reference_frequency_lists_struct),
    CSN1Ref(name='cell_allocation', obj=cell_allocation_lists_struct),
    CSN1Ref(name='gprs_mobile_allocations', obj=gprs_mobile_allocations_lists_struct),
    CSN1Ref(name='pccch_description', obj=pccch_description_lists_struct),
    CSN1Alt(alt={
      '0': ('', [
      CSN1Bit(bit=-1)]),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Ref(name='compact_control_information', obj=compact_control_info_struct)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Ref(name='additional_psi_messages', obj=additional_psi_messages_struct)])}),
      CSN1Ref(obj=padding_bits)]),
      None: ('', [])})])])

