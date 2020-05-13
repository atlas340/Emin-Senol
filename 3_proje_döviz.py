import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display_html
import numpy as np
import sched,time
import requests
import json

print("Yapılabilecek işlemler\n"
      "1-> Borsa\n"
      "2->Altın Bilgileri\n"
      "3->Döviz Kurları\n"
      "4->Genel Bilgi\n"
      "5->Döviz Çevirme\n"
      "q->Programı Sonlandır.")
url =  "https://www.foreks.com/borsa" # Site linkimiz

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.


degerler = soup.find_all("div",{"class":"marketTicker"})

def deger_oku():
    url = "https://www.doviz.com/"  # Site linkimiz

    response = requests.get(url)  # Web sayfamızı çekiyoruz.

    html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

    soup = BeautifulSoup(html_icerigi, "html.parser")  # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

    degerler = soup.find_all("div", {"class": "market-data"})


    for deger in degerler:#raating ve başlıkları zip ettik.Yanin aynı boyuttaki iki listeyi birbirine birleştirmiş olduk.
        deger = deger.text#.text olanları almış olduk.


        deger = deger.strip()#Baştaki ve sondaki boşlukları siler
        deger = deger.replace("\n","")#\n yerine boşluk koşmuş olduk.

        print( "Genel  Değerler: {}".format(deger))




while True:
    a = input("Yapmak İstediğiniz İşlemi Seçiniz: ")
    if(a == "1"):
        html_table ="""
            <table>
            <thead>
            <tr>
                <th>Sembol</th>
                <th>Son</th>
                <th>Fark</th>
                <th>Fark%</th>
                <th>Günlük İşlem</th>
                <th>Saat</th>
            </tr>
            </thead>
            <tbody>
            <tr class="down">
                    <td class="symbol"><span class="icon"></span>GSRAY</td>
                    <td class="last">2,54</td>
                    <td class="change">-0,09</td>
                    <td class="change">-3,42</td>
                    <td class="last">247.102.310,00</td>
                    <td class="time">18:09:54</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>YKBNK</td>
                    <td class="last">2,06</td>
                    <td class="change">0,03</td>
                    <td class="change">1,48</td>
                    <td class="last">246.816.627,00</td>
                    <td class="time">18:09:54</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>GARAN</td>
                    <td class="last">8,63</td>
                    <td class="change">0,14</td>
                    <td class="change">1,65</td>
                    <td class="last">214.479.452,00</td>
                    <td class="time">18:09:59</td>
                </tr>
            <tr class="down">
                    <td class="symbol"><span class="icon"></span>PETKM</td>
                    <td class="last">3,43</td>
                    <td class="change">-0,01</td>
                    <td class="change">-0,29</td>
                    <td class="last">140.706.374,00</td>
                    <td class="time">18:09:52</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>CEMAS</td>
                    <td class="last">0,94</td>
                    <td class="change">0,05</td>
                    <td class="change">5,62</td>
                    <td class="last">133.750.954,00</td>
                    <td class="time">18:09:39</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>ISFIN</td>
                    <td class="last">3,15</td>
                    <td class="change">0,09</td>
                    <td class="change">2,94</td>
                    <td class="last">133.145.678,00</td>
                    <td class="time">18:09:23</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>TSPOR</td>
                    <td class="last">4,30</td>
                    <td class="change">0,23</td>
                    <td class="change">5,65</td>
                    <td class="last">117.162.161,00</td>
                    <td class="time">18:10:00</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>IHLGM</td>
                    <td class="last">1,05</td>
                    <td class="change">0,01</td>
                    <td class="change">0,96</td>
                    <td class="last">111.761.468,00</td>
                    <td class="time">18:09:47</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>VAKBN</td>
                    <td class="last">4,68</td>
                    <td class="change">0,05</td>
                    <td class="change">1,08</td>
                    <td class="last">109.952.759,00</td>
                    <td class="time">18:09:57</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>GUSGR</td>
                    <td class="last">2,34</td>
                    <td class="change">0,10</td>
                    <td class="change">4,46</td>
                    <td class="last">95.450.515,00</td>
                    <td class="time">18:09:48</td>
                </tr>
            <tr class="down">
                    <td class="symbol"><span class="icon"></span>TSKB</td>
                    <td class="last">0,97</td>
                    <td class="change">0,00</td>
                    <td class="change">0,00</td>
                    <td class="last">82.695.518,00</td>
                    <td class="time">18:09:25</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>THYAO</td>
                    <td class="last">9,80</td>
                    <td class="change">0,06</td>
                    <td class="change">0,62</td>
                    <td class="last">76.226.290,00</td>
                    <td class="time">18:09:58</td>
                </tr>
            <tr class="down">
                    <td class="symbol"><span class="icon"></span>EKGYO</td>
                    <td class="last">1,22</td>
                    <td class="change">0,00</td>
                    <td class="change">0,00</td>
                    <td class="last">66.778.265,00</td>
                    <td class="time">18:09:59</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>AKBNK</td>
                    <td class="last">6,12</td>
                    <td class="change">0,09</td>
                    <td class="change">1,49</td>
                    <td class="last">66.498.867,00</td>
                    <td class="time">18:09:54</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>ISCTR</td>
                    <td class="last">5,09</td>
                    <td class="change">0,06</td>
                    <td class="change">1,19</td>
                    <td class="last">64.716.381,00</td>
                    <td class="time">18:09:57</td>
                </tr>
            <tr class="down">
                    <td class="symbol"><span class="icon"></span>ODAS</td>
                    <td class="last">1,43</td>
                    <td class="change">-0,02</td>
                    <td class="change">-1,38</td>
                    <td class="last">59.144.894,00</td>
                    <td class="time">18:09:53</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>ZOREN</td>
                    <td class="last">1,18</td>
                    <td class="change">0,01</td>
                    <td class="change">0,85</td>
                    <td class="last">58.960.833,00</td>
                    <td class="time">18:09:52</td>
                </tr>
            <tr class="up">
                    <td class="symbol"><span class="icon"></span>IHLAS</td>
                    <td class="last">0,62</td>
                    <td class="change">0,03</td>
                    <td class="change">5,08</td>
                    <td class="last">56.822.772,00</td>
                    <td class="time">18:09:57</td>
                </tr>
            <tr class="down">
                    <td class="symbol"><span class="icon"></span>KARSN</td>
                    <td class="last">1,38</td>
                    <td class="change">0,00</td>
                    <td class="change">0,00</td>
                    <td class="last">56.791.113,00</td>
                    <td class="time">18:09:52</td>
                </tr>
            <tr class="down">
                    <td class="symbol"><span class="icon"></span>ALBRK</td>
                    <td class="last">1,19</td>
                    <td class="change">0,00</td>
                    <td class="change">0,00</td>
                    <td class="last">52.537.439,00</td>
                    <td class="time">18:09:55</td>
                </tr>
            </tbody>
        </table>
            """

        display_html(html_table,raw=True)
        df =pd.read_html(html_table)
        df = df[0]
        df = df.set_index('Sembol')
        print(df)

    elif ( a == "2"):
        html_table2="""
        <table>
                        <thead>
                            <tr>
                                <th>Altın Cinsi</th>
                                <th></th>
                                <th>Alış</th>
                                <th>Satış</th>
                                <th>Fark</th>
                                <th>Fark %</th>
                                <th>Saat</th>
                                </tr>
                        </thead>
                        <tbody>
                            <tr>
                                    <td class="symbol"><span class="icon up"></span> Gram Altın</td>
                                                    <td></td>
                                            <td class="last">362,50</td>
                                            <td class="last">363,48</td>
                                            <td class="percentage up">2,569</td>
                                            <td class="percentage up">%0,71</td>
                                            <td class="text-right">23:59:59</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="icon "></span> 22 Ayar Bilezik Gram</td>
                                                    <td></td>
                                            <td class="last">290,46</td>
                                            <td class="last">290,85</td>
                                            <td class="percentage ">0</td>
                                            <td class="percentage ">%0,00</td>
                                            <td class="text-right">12:47:33</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="icon up"></span> Cumhuriyet</td>
                                                    <td></td>
                                            <td class="last">2.110,00</td>
                                            <td class="last">2.142,00</td>
                                            <td class="percentage up">10</td>
                                            <td class="percentage up">%0,47</td>
                                            <td class="text-right">12:47:36</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="icon "></span> Yarım Altın</td>
                                                    <td></td>
                                            <td class="last">1.015,96</td>
                                            <td class="last">1.042,84</td>
                                            <td class="percentage ">0</td>
                                            <td class="percentage ">%0,00</td>
                                            <td class="text-right">12:47:33</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="icon "></span> Çeyrek Altın</td>
                                                    <td></td>
                                            <td class="last">509,57</td>
                                            <td class="last">521,42</td>
                                            <td class="percentage ">0</td>
                                            <td class="percentage ">%0,00</td>
                                            <td class="text-right">12:47:33</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="icon "></span> Ata Altın</td>
                                                    <td></td>
                                            <td class="last">2.101,98</td>
                                            <td class="last">2.155,83</td>
                                            <td class="percentage ">0</td>
                                            <td class="percentage ">%0,00</td>
                                            <td class="text-right">12:47:33</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="icon up"></span> Ons Altın/Dolar</td>
                                                    <td></td>
                                            <td class="last">1.683,53</td>
                                            <td class="last">1.688,12</td>
                                            <td class="percentage up">1,93</td>
                                            <td class="percentage up">%0,11</td>
                                            <td class="text-right">23:55:00</td>
                                            </tr>
                            </tbody>
                    </table>
        """


        display_html(html_table2,raw=True)
        dt =pd.read_html(html_table2)
        dt = dt[0]
        dt = dt.loc[:, ~dt.columns.str.contains('^Unnamed')]
        dt = dt.set_index('Altın Cinsi')


        print(dt)
    elif(a=="3"):
        html_table3="""<table>
                        <thead>
                            <tr>
                                <th>Sembol</th>
                                <th>Alış</th>
                                <th>Satış</th>
                                <th>Fark</th>
                                <th>Fark %</th>
                                <th>Saat</th>
                                </tr>
                        </thead>
                        <tbody>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SUSD.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> ABD Doları</td>
                                                    <td class="last">6,5950</td>
                                            <td class="last">6,5970</td>
                                            <td class="percentage up">0,093</td>
                                            <td class="percentage up">%1,43</td>
                                            <td class="time">12:18:31</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SEUR.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> Euro</td>
                                                    <td class="last">7,0500</td>
                                            <td class="last">7,0520</td>
                                            <td class="percentage up">0,07</td>
                                            <td class="percentage up">%1,00</td>
                                            <td class="time">12:22:26</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SGBP.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> İngiliz Sterlini</td>
                                                    <td class="last">8,3156</td>
                                            <td class="last">8,3573</td>
                                            <td class="percentage up">0,034</td>
                                            <td class="percentage up">%0,41</td>
                                            <td class="time">23:59:59</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SCHF.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> İsviçre Frangı</td>
                                                    <td class="last">6,9062</td>
                                            <td class="last">6,9478</td>
                                            <td class="percentage up">0,039</td>
                                            <td class="percentage up">%0,57</td>
                                            <td class="time">23:59:59</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SJPY.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> 100 Japon Yeni</td>
                                                    <td class="last">6,1515</td>
                                            <td class="last">6,1885</td>
                                            <td class="percentage up">0,036</td>
                                            <td class="percentage up">%0,58</td>
                                            <td class="time">23:59:59</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SRUB.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> Rus Rublesi</td>
                                                    <td class="last">0,0905</td>
                                            <td class="last">0,0910</td>
                                            <td class="percentage up">0,001</td>
                                            <td class="percentage up">%1,26</td>
                                            <td class="time">23:59:59</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SCNY.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> Çin Yuanı</td>
                                                    <td class="last">0,9484</td>
                                            <td class="last">0,9542</td>
                                            <td class="percentage up">0,006</td>
                                            <td class="percentage up">%0,68</td>
                                            <td class="time">23:59:59</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SHUF.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> Macaristan Forinti</td>
                                                    <td class="last">0,0206</td>
                                            <td class="last">0,0208</td>
                                            <td class="percentage up">0</td>
                                            <td class="percentage up">%0,68</td>
                                            <td class="time">23:59:52</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SCAD.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> Kanada Doları</td>
                                                    <td class="last">4,7804</td>
                                            <td class="last">4,8092</td>
                                            <td class="percentage up">0,031</td>
                                            <td class="percentage up">%0,66</td>
                                            <td class="time">23:59:59</td>
                                            </tr>
                            <tr>
                                    <td class="symbol"><span class="flags"><img src="/assets/currency/flags/SBRL.png" alt=""></span>
                                                        <span class="icon up"></span>
                                                        <span class="description"></span> Brezilya Reali</td>
                                                    <td class="last">1,3061</td>
                                            <td class="last">1,3140</td>
                                            <td class="percentage up">0,007</td>
                                            <td class="percentage up">%0,50</td>
                                            <td class="time">23:59:59</td>
                                            </tr>
                            </tbody>
                    </table>
        """

        display_html(html_table3, raw=True)
        df = pd.read_html(html_table3)
        df = df[0]
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df = df.set_index('Sembol')
        print(df)
    elif(a=="4"):
        deger_oku()
    elif (a == "5"):
        base = input("Convert From: ")
        to = input("Convert to: ")
        amount = float(input("Amount: "))
        url = "https://api.exchangeratesapi.io/latest?symbols=" + base

        response = requests.get(url)
        data = response.text
        parsed = json.loads((data))
        rates = parsed["rates"]
        for currency, rate in rates.items():
            if currency == to:
                conversion = rate * amount
                print("1", base, "=", currency, rate)
                print(amount, base, "=", currency, conversion)
    elif(a=="q"):
        print("Programdn çıkılıyor...")
        break
    else:
        print("Hatalı işlem!Lütfen Yukarda Belirtilen İşlemleri Giriniz")
        continue




