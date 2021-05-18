# -*- coding: ISO-8859-1 -*-
#
# generated by wxGlade 0.9.3 on Fri Jun 28 16:25:14 2019
#

import wx

from .icons import ( icons8_connected_50)
from .mwindow import MWindow

_ = wx.GetTranslation


class Controller(MWindow):
    def __init__(self, *args, **kwds):
        super().__init__(423, 131, *args, **kwds)

        self.text_controller_message = wx.TextCtrl(self, wx.ID_ANY, "The output of the selected device is not a controller, or provides no graphical user interface.", style=wx.TE_CENTRE | wx.TE_MULTILINE | wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(icons8_connected_50.GetBitmap())
        self.SetIcon(_icon)
        self.SetTitle("Controller")
        self.text_controller_message.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Controller.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.text_controller_message, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def window_open(self):
        pass

    def window_close(self):
        pass


#
# from ..kernel import (
#     STATE_ACTIVE,
#     STATE_BUSY,
#     STATE_END,
#     STATE_IDLE,
#     STATE_INITIALIZE,
#     STATE_PAUSE,
#     STATE_TERMINATE,
#     STATE_WAIT,
# )
# from .icons import (
#     icons8_comments_50,
#     icons8_connected_50,
#     icons8_disconnected_50,
#     icons8_emergency_stop_button_50,
#     icons8_laser_beam_hazard_50,
#     icons8_pause_50,
#     icons8_play_50,
# )

# class Controller(MWindow):
#     def __init__(self, *args, **kwds):
#         super().__init__(499, 505, *args, **kwds)
#         self.button_controller_control = wx.Button(
#             self, wx.ID_ANY, _("Start Controller")
#         )
#         self.text_controller_status = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.button_device_connect = wx.Button(self, wx.ID_ANY, _("Connection"))
#         self.text_connection_status = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.text_device = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.text_location = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.gauge_buffer = wx.Gauge(self, wx.ID_ANY, 10)
#         self.checkbox_limit_buffer = wx.CheckBox(
#             self, wx.ID_ANY, _("Limit Write Buffer")
#         )
#         self.text_buffer_length = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.spin_packet_buffer_max = wx.SpinCtrl(
#             self, wx.ID_ANY, "1500", min=1, max=100000
#         )
#         self.button_buffer_viewer = wx.BitmapButton(
#             self, wx.ID_ANY, icons8_comments_50.GetBitmap()
#         )
#         self.packet_count_text = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.rejected_packet_count_text = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.packet_text_text = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.text_byte_0 = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.text_byte_1 = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.text_desc = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.text_byte_2 = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.text_byte_3 = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.text_byte_4 = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.text_byte_5 = wx.TextCtrl(self, wx.ID_ANY, "")
#         self.button_pause = wx.BitmapButton(
#             self, wx.ID_ANY, icons8_pause_50.GetBitmap()
#         )
#         self.button_stop = wx.BitmapButton(
#             self, wx.ID_ANY, icons8_emergency_stop_button_50.GetBitmap()
#         )
#
#         self.__set_properties()
#         self.__do_layout()
#
#         self.Bind(wx.EVT_BUTTON, self.on_button_connect, self.button_device_connect)
#         self.Bind(
#             wx.EVT_CHECKBOX,
#             self.on_check_limit_packet_buffer,
#             self.checkbox_limit_buffer,
#         )
#         self.Bind(
#             wx.EVT_SPINCTRL, self.on_spin_packet_buffer_max, self.spin_packet_buffer_max
#         )
#         self.Bind(
#             wx.EVT_TEXT, self.on_spin_packet_buffer_max, self.spin_packet_buffer_max
#         )
#         self.Bind(
#             wx.EVT_TEXT_ENTER,
#             self.on_spin_packet_buffer_max,
#             self.spin_packet_buffer_max,
#         )
#         self.Bind(
#             wx.EVT_BUTTON,
#             lambda e: self.context("window open BufferView\n"),
#             self.button_buffer_viewer,
#         )
#         self.Bind(wx.EVT_BUTTON, self.on_button_pause_resume, self.button_pause)
#         self.Bind(wx.EVT_BUTTON, self.on_button_emergency_stop, self.button_stop)
#         # end wxGlade
#         self.Bind(wx.EVT_RIGHT_DOWN, self.on_controller_menu, self)
#         self.buffer_max = 1
#         self.last_control_state = None
#         self.gui_update = True
#
#     def window_open(self):
#         self.context.setting(int, "buffer_max", 1500)
#         self.context.setting(bool, "buffer_limit", True)
#         self.context.setting(str, "device_location", "Unknown")
#         self.context.setting(str, "device_name", "Unknown")
#         self.context.listen("pipe;status", self.update_status)
#         self.context.listen("pipe;packet_text", self.update_packet_text)
#         self.context.listen("pipe;buffer", self.on_buffer_update)
#         self.context.listen("pipe;usb_status", self.on_connection_status_change)
#         self.context.listen("pipe;state", self.on_connection_state_change)
#         self.context.listen("pipe;thread", self.on_control_state)
#         self.checkbox_limit_buffer.SetValue(self.context.buffer_limit)
#         self.spin_packet_buffer_max.SetValue(self.context.buffer_max)
#         self.text_device.SetValue(self.context.device_name)
#         self.text_location.SetValue(self.context.device_location)
#
#     def window_close(self):
#         self.gui_update = False
#         self.context.unlisten("pipe;status", self.update_status)
#         self.context.unlisten("pipe;packet_text", self.update_packet_text)
#         self.context.unlisten("pipe;buffer", self.on_buffer_update)
#         self.context.unlisten("pipe;usb_status", self.on_connection_status_change)
#         self.context.unlisten("pipe;state", self.on_connection_state_change)
#         self.context.unlisten("pipe;thread", self.on_control_state)
#
#     def device_execute(self, control_name):
#         def menu_element(event):
#             self.context.execute(control_name)
#
#         return menu_element
#
#     def on_controller_menu(self, event):
#         gui = self
#         menu = wx.Menu()
#         path_scale_sub_menu = wx.Menu()
#         for control_name in self.context.match("control"):
#             gui.Bind(
#                 wx.EVT_MENU,
#                 self.context.execute(control_name),
#                 path_scale_sub_menu.Append(
#                     wx.ID_ANY, list(control_name.split("/"))[-1], "", wx.ITEM_NORMAL
#                 ),
#             )
#         menu.Append(wx.ID_ANY, _("Kernel Force Event"), path_scale_sub_menu)
#         if menu.MenuItemCount != 0:
#             gui.PopupMenu(menu)
#             menu.Destroy()
#
#     def __set_properties(self):
#         # begin wxGlade: Controller.__set_properties
#         _icon = wx.NullIcon
#         _icon.CopyFromBitmap(icons8_connected_50.GetBitmap())
#         self.SetIcon(_icon)
#         self.SetTitle(_("Controller"))
#         self.button_controller_control.SetBackgroundColour(wx.Colour(102, 255, 102))
#         self.button_controller_control.SetFont(
#             wx.Font(
#                 12,
#                 wx.FONTFAMILY_DEFAULT,
#                 wx.FONTSTYLE_NORMAL,
#                 wx.FONTWEIGHT_NORMAL,
#                 0,
#                 "Segoe UI",
#             )
#         )
#         self.button_controller_control.SetForegroundColour(wx.BLACK)
#         self.button_controller_control.SetToolTip(
#             _("Change the currently performed operation.")
#         )
#         self.button_controller_control.SetBitmap(icons8_play_50.GetBitmap())
#         self.text_controller_status.SetToolTip(
#             _("Displays the controller's current process.")
#         )
#         self.button_device_connect.SetBackgroundColour(wx.Colour(102, 255, 102))
#         self.button_device_connect.SetFont(
#             wx.Font(
#                 12,
#                 wx.FONTFAMILY_DEFAULT,
#                 wx.FONTSTYLE_NORMAL,
#                 wx.FONTWEIGHT_NORMAL,
#                 0,
#                 "Segoe UI",
#             )
#         )
#         self.button_device_connect.SetForegroundColour(wx.BLACK)
#         self.button_device_connect.SetToolTip(
#             _("Force connection/disconnection from the device.")
#         )
#         self.button_device_connect.SetBitmap(icons8_connected_50.GetBitmap())
#         self.text_connection_status.SetToolTip(_("Connection status"))
#         self.text_device.SetToolTip(_("Device being used"))
#         self.text_location.SetToolTip(_("Connection location"))
#         self.checkbox_limit_buffer.SetToolTip(
#             _(
#                 "Limit the write buffer to a certain amount. Permits on-the-fly command production."
#             )
#         )
#         self.checkbox_limit_buffer.SetValue(1)
#         self.text_buffer_length.SetMinSize((165, 23))
#         self.text_buffer_length.SetToolTip(
#             _("Current number of bytes in the write buffer.")
#         )
#         self.spin_packet_buffer_max.SetToolTip(_("Current maximum write buffer limit."))
#         self.button_buffer_viewer.SetMinSize((52, 52))
#         self.button_buffer_viewer.SetToolTip(_("View a snapshot of the current buffer"))
#         self.packet_count_text.SetMinSize((77, 23))
#         self.packet_count_text.SetToolTip(_("Total number of packets sent"))
#         self.rejected_packet_count_text.SetMinSize((77, 23))
#         self.rejected_packet_count_text.SetToolTip(
#             _("Total number of packets rejected")
#         )
#         self.packet_text_text.SetToolTip(_("Last packet information sent"))
#         self.text_byte_0.SetMinSize((77, 23))
#         self.text_byte_1.SetMinSize((77, 23))
#         self.text_desc.SetMinSize((75, 23))
#         self.text_desc.SetToolTip(_("The meaning of Byte 1"))
#         self.text_byte_2.SetMinSize((77, 23))
#         self.text_byte_3.SetMinSize((77, 23))
#         self.text_byte_4.SetMinSize((77, 23))
#         self.text_byte_5.SetMinSize((77, 23))
#         self.button_pause.SetBackgroundColour(wx.Colour(255, 255, 0))
#         self.button_pause.SetToolTip(_("Pause/Resume the controller"))
#         self.button_pause.SetSize(self.button_pause.GetBestSize())
#         self.button_stop.SetBackgroundColour(wx.Colour(127, 0, 0))
#         self.button_stop.SetToolTip(_("Emergency stop/reset the controller."))
#         self.button_stop.SetSize(self.button_stop.GetBestSize())
#         # end wxGlade
#
#     def __do_layout(self):
#         # begin wxGlade: Controller.__do_layout
#         sizer_1 = wx.BoxSizer(wx.VERTICAL)
#         sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
#         byte_data_status = wx.BoxSizer(wx.HORIZONTAL)
#         byte5sizer = wx.BoxSizer(wx.VERTICAL)
#         byte4sizer = wx.BoxSizer(wx.VERTICAL)
#         byte3sizer = wx.BoxSizer(wx.VERTICAL)
#         byte2sizer = wx.BoxSizer(wx.VERTICAL)
#         byte1sizer = wx.BoxSizer(wx.VERTICAL)
#         byte0sizer = wx.BoxSizer(wx.VERTICAL)
#         packet_info = wx.BoxSizer(wx.HORIZONTAL)
#         packet_count = wx.BoxSizer(wx.HORIZONTAL)
#         write_buffer = wx.BoxSizer(wx.HORIZONTAL)
#         connection_controller = wx.BoxSizer(wx.VERTICAL)
#         sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
#         start_controller = wx.BoxSizer(wx.VERTICAL)
#         sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
#         start_controller.Add(self.button_controller_control, 0, wx.EXPAND, 0)
#         label_12 = wx.StaticText(self, wx.ID_ANY, _("Process"))
#         label_12.SetMinSize((80, 16))
#         sizer_17.Add(label_12, 1, 0, 0)
#         sizer_17.Add(self.text_controller_status, 10, wx.EXPAND, 0)
#         start_controller.Add(sizer_17, 0, 0, 0)
#         sizer_1.Add(start_controller, 0, wx.EXPAND, 0)
#         connection_controller.Add(self.button_device_connect, 0, wx.EXPAND, 0)
#         sizer_15.Add((20, 20), 0, 0, 0)
#         label_7 = wx.StaticText(self, wx.ID_ANY, _("Status"))
#         sizer_15.Add(label_7, 1, 0, 0)
#         sizer_15.Add(self.text_connection_status, 11, 0, 0)
#         sizer_15.Add((20, 20), 0, 0, 0)
#         label_8 = wx.StaticText(self, wx.ID_ANY, _("Device"))
#         sizer_15.Add(label_8, 1, 0, 0)
#         sizer_15.Add(self.text_device, 11, 0, 0)
#         sizer_15.Add((20, 20), 0, 0, 0)
#         label_9 = wx.StaticText(self, wx.ID_ANY, _("Location"))
#         sizer_15.Add(label_9, 1, 0, 0)
#         sizer_15.Add(self.text_location, 11, 0, 0)
#         connection_controller.Add(sizer_15, 0, 0, 0)
#         sizer_1.Add(connection_controller, 0, wx.EXPAND, 0)
#         static_line_2 = wx.StaticLine(self, wx.ID_ANY)
#         static_line_2.SetMinSize((483, 5))
#         sizer_1.Add(static_line_2, 0, wx.EXPAND, 0)
#         sizer_1.Add(self.gauge_buffer, 0, wx.EXPAND, 0)
#         write_buffer.Add(self.checkbox_limit_buffer, 1, 0, 0)
#         write_buffer.Add(self.text_buffer_length, 10, 0, 0)
#         label_14 = wx.StaticText(self, wx.ID_ANY, "/")
#         write_buffer.Add(label_14, 0, 0, 0)
#         write_buffer.Add(self.spin_packet_buffer_max, 0, 0, 0)
#         write_buffer.Add(self.button_buffer_viewer, 1, 0, 0)
#         sizer_1.Add(write_buffer, 0, 0, 0)
#         static_line_1 = wx.StaticLine(self, wx.ID_ANY)
#         sizer_1.Add(static_line_1, 0, wx.EXPAND, 0)
#         label_11 = wx.StaticText(self, wx.ID_ANY, _("Packet Count"))
#         packet_count.Add(label_11, 0, 0, 0)
#         packet_count.Add(self.packet_count_text, 0, 0, 0)
#         packet_count.Add((165, 20), 0, 0, 0)
#         label_13 = wx.StaticText(self, wx.ID_ANY, _("Rejected Packets"))
#         packet_count.Add(label_13, 0, 0, 0)
#         packet_count.Add(self.rejected_packet_count_text, 0, 0, 0)
#         sizer_1.Add(packet_count, 0, 0, 0)
#         label_10 = wx.StaticText(self, wx.ID_ANY, _("Packet Info"))
#         packet_info.Add(label_10, 1, 0, 0)
#         packet_info.Add(self.packet_text_text, 11, 0, 0)
#         sizer_1.Add(packet_info, 0, 0, 0)
#         byte0sizer.Add(self.text_byte_0, 0, 0, 0)
#         label_1 = wx.StaticText(self, wx.ID_ANY, _("Byte 0"))
#         byte0sizer.Add(label_1, 0, 0, 0)
#         byte_data_status.Add(byte0sizer, 1, wx.EXPAND, 0)
#         byte1sizer.Add(self.text_byte_1, 0, 0, 0)
#         label_2 = wx.StaticText(self, wx.ID_ANY, _("Byte 1"))
#         byte1sizer.Add(label_2, 0, 0, 0)
#         byte1sizer.Add(self.text_desc, 0, 0, 0)
#         byte_data_status.Add(byte1sizer, 1, wx.EXPAND, 0)
#         byte2sizer.Add(self.text_byte_2, 0, 0, 0)
#         label_3 = wx.StaticText(self, wx.ID_ANY, _("Byte 2"))
#         byte2sizer.Add(label_3, 0, 0, 0)
#         byte_data_status.Add(byte2sizer, 1, wx.EXPAND, 0)
#         byte3sizer.Add(self.text_byte_3, 0, 0, 0)
#         label_4 = wx.StaticText(self, wx.ID_ANY, _("Byte 3"))
#         byte3sizer.Add(label_4, 0, 0, 0)
#         byte_data_status.Add(byte3sizer, 1, wx.EXPAND, 0)
#         byte4sizer.Add(self.text_byte_4, 0, 0, 0)
#         label_5 = wx.StaticText(self, wx.ID_ANY, _("Byte 4"))
#         byte4sizer.Add(label_5, 0, 0, 0)
#         byte_data_status.Add(byte4sizer, 1, wx.EXPAND, 0)
#         byte5sizer.Add(self.text_byte_5, 0, 0, 0)
#         label_6 = wx.StaticText(self, wx.ID_ANY, _("Byte 5"))
#         byte5sizer.Add(label_6, 0, 0, 0)
#         byte_data_status.Add(byte5sizer, 1, wx.EXPAND, 0)
#         sizer_1.Add(byte_data_status, 0, wx.EXPAND, 0)
#         sizer_2.Add(self.button_pause, 1, wx.EXPAND, 0)
#         sizer_2.Add(self.button_stop, 1, wx.EXPAND, 0)
#         sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
#         self.SetSizer(sizer_1)
#         self.Layout()
#         # end wxGlade
#
#     def on_check_limit_packet_buffer(self, event):  # wxGlade: JobInfo.<event_handler>
#         self.context.buffer_limit = not self.context.buffer_limit
#
#     def on_spin_packet_buffer_max(self, event):  # wxGlade: JobInfo.<event_handler>
#         self.context.buffer_max = self.spin_packet_buffer_max.GetValue()
#
#     def on_button_emergency_stop(self, event):  # wxGlade: Controller.<event_handler>
#         try:
#             self.context("estop\n")
#         except AttributeError:
#             pass
#
#     def on_button_pause_resume(self, event):  # wxGlade: Controller.<event_handler>
#         try:
#             self.context("pause\n")
#         except AttributeError:
#             pass
#
#     def update_status(self, origin, status_data, code_string):
#         if status_data is not None:
#             if isinstance(status_data, int):
#                 self.text_desc.SetValue(str(status_data))
#                 self.text_desc.SetValue(code_string)
#             else:
#                 if len(status_data) == 6:
#                     self.text_byte_0.SetValue(str(status_data[0]))
#                     self.text_byte_1.SetValue(str(status_data[1]))
#                     self.text_byte_2.SetValue(str(status_data[2]))
#                     self.text_byte_3.SetValue(str(status_data[3]))
#                     self.text_byte_4.SetValue(str(status_data[4]))
#                     self.text_byte_5.SetValue(str(status_data[5]))
#                     self.text_desc.SetValue(code_string)
#         self.packet_count_text.SetValue(str(self.context.packet_count))
#         self.rejected_packet_count_text.SetValue(str(self.context.rejected_count))
#
#     def update_packet_text(self, origin, string_data):
#         if string_data is not None and len(string_data) != 0:
#             self.packet_text_text.SetValue(str(string_data))
#
#     def on_connection_status_change(self, origin, status):
#         self.text_connection_status.SetValue(str(status))
#
#     def on_connection_state_change(self, origin, state):
#         if state == "STATE_CONNECTION_FAILED" or state == "STATE_DRIVER_NO_BACKEND":
#             self.button_device_connect.SetBackgroundColour("#dfdf00")
#             self.button_device_connect.SetLabel(
#                 str(self.context.last_signal("pipe;usb_status")[0])
#             )
#             self.button_device_connect.SetBitmap(icons8_disconnected_50.GetBitmap())
#             self.button_device_connect.Enable()
#         elif state == "STATE_UNINITIALIZED" or state == "STATE_USB_DISCONNECTED":
#             self.button_device_connect.SetBackgroundColour("#ffff00")
#             self.button_device_connect.SetLabel(_("Connect"))
#             self.button_device_connect.SetBitmap(icons8_connected_50.GetBitmap())
#             self.button_device_connect.Enable()
#         elif state == "STATE_USB_SET_DISCONNECTING":
#             self.button_device_connect.SetBackgroundColour("#ffff00")
#             self.button_device_connect.SetLabel(_("Disconnecting..."))
#             self.button_device_connect.SetBitmap(icons8_disconnected_50.GetBitmap())
#             self.button_device_connect.Disable()
#         elif state == "STATE_USB_CONNECTED" or state == "STATE_CONNECTED":
#             self.button_device_connect.SetBackgroundColour("#00ff00")
#             self.button_device_connect.SetLabel(_("Disconnect"))
#             self.button_device_connect.SetBitmap(icons8_connected_50.GetBitmap())
#             self.button_device_connect.Enable()
#         elif state == "STATE_CONNECTING":
#             self.button_device_connect.SetBackgroundColour("#ffff00")
#             self.button_device_connect.SetLabel(_("Connecting..."))
#             self.button_device_connect.SetBitmap(icons8_connected_50.GetBitmap())
#             self.button_device_connect.Disable()
#
#     def on_button_connect(self, event):  # wxGlade: Controller.<event_handler>
#         state = self.context.last_signal("pipe;state")
#         if state is not None and isinstance(state, tuple):
#             state = state[0]
#         if state in (
#             "STATE_USB_DISCONNECTED",
#             "STATE_UNINITIALIZED",
#             "STATE_CONNECTION_FAILED",
#             "STATE_DRIVER_MOCK",
#             None,
#         ):
#             try:
#                 self.context("usb_connect\n")
#             except ConnectionRefusedError:
#                 dlg = wx.MessageDialog(
#                     None,
#                     _("Connection Refused. See USB Log for detailed information."),
#                     _("Manual Connection"),
#                     wx.OK | wx.ICON_WARNING,
#                 )
#                 result = dlg.ShowModal()
#                 dlg.Destroy()
#         elif state in ("STATE_CONNECTED", "STATE_USB_CONNECTED"):
#             self.context("usb_disconnect\n")
#
#     def on_buffer_update(self, origin, value, *args):
#         if self.gui_update:
#             if value > self.buffer_max:
#                 self.buffer_max = value
#             self.text_buffer_length.SetValue(str(value))
#             self.gauge_buffer.SetRange(self.buffer_max)
#             self.gauge_buffer.SetValue(min(value, self.gauge_buffer.GetRange()))
#
#     def on_control_state(self, origin, state):
#         if self.last_control_state == state:
#             return
#         self.last_control_state = state
#         button = self.button_controller_control
#         if self.text_controller_status is None:
#             return
#         value = self.context._kernel.get_text_thread_state(state)
#         self.text_controller_status.SetValue(str(value))
#         if state == STATE_INITIALIZE or state == STATE_END or state == STATE_IDLE:
#
#             def f(event):
#                 self.context("dev start\n")
#                 self.context("dev hold\n")
#
#             self.Bind(wx.EVT_BUTTON, f, button)
#             button.SetBackgroundColour("#009900")
#             button.SetLabel(_("Hold Controller"))
#             button.SetBitmap(icons8_play_50.GetBitmap())
#             button.Enable(True)
#         elif state == STATE_BUSY:
#             button.SetBackgroundColour("#00dd00")
#             button.SetLabel(_("LOCKED"))
#             button.SetBitmap(icons8_play_50.GetBitmap())
#             button.Enable(False)
#         elif state == STATE_WAIT:
#
#             def f(event):
#                 self.context("dev continue\n")
#
#             self.Bind(wx.EVT_BUTTON, f, button)
#             button.SetBackgroundColour("#dddd00")
#             button.SetLabel(_("Force Continue"))
#             button.SetBitmap(icons8_laser_beam_hazard_50.GetBitmap())
#             button.Enable(True)
#         elif state == STATE_PAUSE:
#
#             def f(event):
#                 self.context("dev resume\n")
#
#             self.Bind(wx.EVT_BUTTON, f, button)
#             button.SetBackgroundColour("#00dd00")
#             button.SetLabel(_("Resume Controller"))
#             button.SetBitmap(icons8_play_50.GetBitmap())
#             button.Enable(True)
#         elif state == STATE_ACTIVE:
#
#             def f(event):
#                 self.context("dev hold\n")
#
#             self.Bind(wx.EVT_BUTTON, f, button)
#             button.SetBackgroundColour("#00ff00")
#             button.SetLabel(_("Pause Controller"))
#             button.SetBitmap(icons8_pause_50.GetBitmap())
#             button.Enable(True)
#         elif state == STATE_TERMINATE:
#
#             def f(event):
#                 self.context("dev abort\n")
#
#             self.Bind(wx.EVT_BUTTON, f, button)
#             button.SetBackgroundColour("#00ffff")
#             button.SetLabel(_("Manual Reset"))
#             button.SetBitmap(icons8_emergency_stop_button_50.GetBitmap())
#             button.Enable(True)


# end of class Controller
