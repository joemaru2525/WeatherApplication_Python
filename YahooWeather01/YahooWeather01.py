# -*- coding: utf-8 -*- 

import wx
import re
import urllib.request
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"
 
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
 
title_tag = soup.title
#print(title_tag.string)
 
announce = soup.find("p", class_="yjSt yjw_note_h2")
#print(announce.string)
 
weatherdate = soup.find("p", class_="date")
#print(weatherdate.string)
 
highTemp = soup.find("li", class_="high")
highTemp1 = str(highTemp).replace('<li class="high"><em>', '').replace('</em>', '').replace('</li>', '')
#print("最高気温：" + highTemp1)
 
lowTemp = soup.find("li", class_="low")
lowTemp1 = str(lowTemp).replace('<li class="low"><em>', '').replace('</em>', '').replace('</li>', '')
#print("最低気温：" + lowTemp1)
 
precip = soup.find("tr", class_="precip")
# print(precip)
precipAll = str(precip)
 
precipList = []
pointSerch = 0
 
for num in range(4):
    pointFirst = precipAll.find("<td>",pointSerch)
    pointLast = precipAll.find("</td>",pointSerch)
    precipList.append(precipAll[pointFirst+4:pointLast])
    pointSerch = pointLast + 4
#print("降水確率：")
#print(precipList)
#print("")

divPic = soup.find('div', class_="forecastCity")
pPic = divPic.find('p', class_="pict")
imgPic = pPic.find('img')
weather = imgPic['alt']
#print("天候：" + weather)
imgUrl = imgPic['src']
#print("天気画像URL：")
#print(imgUrl)
#print("")
 

#--------------------------------------
#    トップレベルウィンドウクラス
#--------------------------------------
class RootFrame(wx.Frame):

    def __init__(self):
        
        wx.Frame.__init__(self, None,wx.ID_ANY, u"Yahoo! Japan 天気予報", size=(300,350))

        #    ステータスバーの初期化
        self.CreateStatusBar()
        self.SetStatusText("https://weather.yahoo.co.jp/weather/")
        self.GetStatusBar().SetBackgroundColour(None)

        #    メニューバーの初期化
        self.SetMenuBar(WeatherMenu())
        
        #    本体部分の構築
        root_panel = wx.Panel(self, wx.ID_ANY)

        weather_panel = WeatherPanel(root_panel)
        precip_panel1 = PrecipPanel1(root_panel)
        precip_panel2 = PrecipPanel2(root_panel)

        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(weather_panel, 0, wx.GROW | wx.ALL, border=5)
        root_layout.Add(precip_panel1, 0, wx.GROW | wx.LEFT, border=5)
        root_layout.Add(precip_panel2, 0, wx.GROW | wx.LEFT, border=5)
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)

#--------------------------------------
#    メニューバークラス
#--------------------------------------
class WeatherMenu(wx.MenuBar):

    def __init__(self):

        wx.MenuBar.__init__(self)
        
        menu_file = wx.Menu()
        menu_file.Append(wx.ID_ANY, u"保存")
        menu_file.Append(wx.ID_ANY, u"終了")
        menu_edit = wx.Menu()
        menu_edit.Append(wx.ID_ANY, u"コピー")
        menu_edit.Append(wx.ID_ANY, u"ペースト")
        
        self.Append(menu_file, u"ファイル")
        self.Append(menu_edit, u"編集")

#--------------------------------------
#    Weather部に表示されるテキスト部分
#--------------------------------------
class WeatherPanel(wx.Panel):

    def __init__(self,parent):
    
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        
        s_text_01 = wx.StaticText(self, wx.ID_ANY, u"")
        s_text_02 = wx.StaticText(self, wx.ID_ANY, u"天気予報の対象地域")
        s_text_03 = wx.StaticText(self, wx.ID_ANY, u"")
        s_text_04 = wx.StaticText(self, wx.ID_ANY, u"発表日時")
        s_text_05 = wx.StaticText(self, wx.ID_ANY, u"対象日")
        s_text_06 = wx.StaticText(self, wx.ID_ANY, u"天気予報")
        s_text_07 = wx.StaticText(self, wx.ID_ANY, u"")
        s_text_08 = wx.StaticText(self, wx.ID_ANY, u"最高気温")
        s_text_09 = wx.StaticText(self, wx.ID_ANY, u"最低気温")
        s_text_10 = wx.StaticText(self, wx.ID_ANY, u"")

        bitmap01 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("sun_clouds_st.gif"), size=(100, 60), style=wx.SIMPLE_BORDER)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(s_text_01)
        layout.Add(s_text_02)
        layout.Add(s_text_03)
        layout.Add(s_text_04)
        layout.Add(s_text_05)
        layout.Add(s_text_06)
        s_text_02.SetLabel(title_tag.string)    #地域
        s_text_04.SetLabel(announce.string)     #発表日時
        s_text_05.SetLabel(weatherdate.string)  #対象日
        s_text_06.SetLabel(weather)             #天気予報
        s_text_08.SetLabel(highTemp1)           #最高気温
        s_text_09.SetLabel(lowTemp1)            #最低気温

        layout.Add(wx.Size(20, 0))
        layout.Add(bitmap01)

        layout.Add(s_text_07)
        layout.Add(s_text_08)
        layout.Add(s_text_09)
        
        self.SetSizer(layout)

#--------------------------------------
#    画面下部1に表示されるテキスト部分
#--------------------------------------
class PrecipPanel1(wx.Panel):

    def __init__(self,parent):

        wx.Panel.__init__(self, parent, wx.ID_ANY)

        s_text_11 = wx.StaticText(self, wx.ID_ANY, u"時間帯　：|")
        s_text_12 = wx.StaticText(self, wx.ID_ANY, u"  0- 6 |")
        s_text_13 = wx.StaticText(self, wx.ID_ANY, u"  6-12 |")
        s_text_14 = wx.StaticText(self, wx.ID_ANY, u" 12-18 |")
        s_text_15 = wx.StaticText(self, wx.ID_ANY, u" 18-24 |")

        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(s_text_11)
        layout.Add(s_text_12)
        layout.Add(s_text_13)
        layout.Add(s_text_14)
        layout.Add(s_text_15)

        self.SetSizer(layout)

#--------------------------------------
#    画面下部2に表示されるテキスト部分
#--------------------------------------
class PrecipPanel2(wx.Panel):

    def __init__(self,parent):

        wx.Panel.__init__(self, parent, wx.ID_ANY)

        s_text_16 = wx.StaticText(self, wx.ID_ANY, u"降水確率： | ")
        s_text_17 = wx.StaticText(self, wx.ID_ANY, u" ---   |")
        s_text_18 = wx.StaticText(self, wx.ID_ANY, u" 0%    |")
        s_text_19 = wx.StaticText(self, wx.ID_ANY, u" 50%   |")
        s_text_20 = wx.StaticText(self, wx.ID_ANY, u" 100%  |")

        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(s_text_16)
        layout.Add(s_text_17)
        layout.Add(s_text_18)
        layout.Add(s_text_19)
        layout.Add(s_text_20)

        s_text_17.SetLabel(precipList[0] + "   |  ")    #0-6
        s_text_18.SetLabel(precipList[1] + "   |  ")    #6-12
        s_text_19.SetLabel(precipList[2] + "   |  ")    #12-18
        s_text_20.SetLabel(precipList[3] + "   |  ")    #18-24

        self.SetSizer(layout)

#--------------------------------------
#    フレームを初期化してアプリを開始
#--------------------------------------
if __name__ == "__main__":

    application = wx.App()
    frame = RootFrame()
    frame.Show()
    application.MainLoop()