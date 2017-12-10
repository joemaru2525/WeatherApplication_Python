# -*- coding: utf-8 -*- 

import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300,400))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

s_text_01 = wx.StaticText(panel, wx.ID_ANY, u"")
s_text_02 = wx.StaticText(panel, wx.ID_ANY, u"天気予報の対象地域")
s_text_03 = wx.StaticText(panel, wx.ID_ANY, u"")
s_text_04 = wx.StaticText(panel, wx.ID_ANY, u"発表日時")
s_text_05 = wx.StaticText(panel, wx.ID_ANY, u"対象日")
s_text_06 = wx.StaticText(panel, wx.ID_ANY, u"天気予報")

s_text_07 = wx.StaticText(panel, wx.ID_ANY, u"")
s_text_08 = wx.StaticText(panel, wx.ID_ANY, u"最高気温")
s_text_09 = wx.StaticText(panel, wx.ID_ANY, u"最低気温")
s_text_10 = wx.StaticText(panel, wx.ID_ANY, u"")
s_text_11 = wx.StaticText(panel, wx.ID_ANY, u"時間帯")
s_text_12 = wx.StaticText(panel, wx.ID_ANY, u"0-6")
s_text_13 = wx.StaticText(panel, wx.ID_ANY, u"6-12")
s_text_14 = wx.StaticText(panel, wx.ID_ANY, u"12-18")
s_text_15 = wx.StaticText(panel, wx.ID_ANY, u"18-24")
s_text_16 = wx.StaticText(panel, wx.ID_ANY, u"降水確率")
s_text_17 = wx.StaticText(panel, wx.ID_ANY, u"---")
s_text_18 = wx.StaticText(panel, wx.ID_ANY, u"0%")
s_text_19 = wx.StaticText(panel, wx.ID_ANY, u"50%")
s_text_20 = wx.StaticText(panel, wx.ID_ANY, u"100%")

bitmap01 = wx.BitmapButton(panel, wx.ID_ANY, wx.Bitmap("sun_clouds_st.gif"), size=(100, 60), style=wx.SIMPLE_BORDER)


layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(s_text_01)
layout.Add(s_text_02)
layout.Add(s_text_03)
layout.Add(s_text_04)
layout.Add(s_text_05)
layout.Add(s_text_06)

layout.Add(wx.Size(20, 0))
layout.Add(bitmap01)

layout.Add(s_text_07)
layout.Add(s_text_08)
layout.Add(s_text_09)
layout.Add(s_text_10)


layout.Add(s_text_11)
layout.Add(s_text_12)
layout.Add(s_text_13)
layout.Add(s_text_14)
layout.Add(s_text_15)
layout.Add(s_text_16)
layout.Add(s_text_17)
layout.Add(s_text_18)
layout.Add(s_text_19)
layout.Add(s_text_20)

panel.SetSizer(layout)

frame.Show()
application.MainLoop()