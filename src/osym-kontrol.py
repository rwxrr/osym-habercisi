#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import smtplib
from bs4 import BeautifulSoup

url = 'https://sonuc.osym.gov.tr/'
page = urllib2.urlopen(url)
sonuclar = BeautifulSoup(page.read())
#OSYM'nin sonuc sayfasindan tüm adresleri cekiyoruz, zaten sadece sinav linkleri var sayfada.
aciklananlar = sonuclar.findAll('a')

for aciklananadres in aciklananlar[0:1]:
	#Adreslerin son 4 haneleri sinavlarin IDlerini iceriyor, son aciklanan sinavin IDsine bakip kodu ona gore yazdim; son sinav ID: 1959
	sonsinavid = aciklananadres['href'][19:23]
	#Beklenenin aksine aciklanan son sonuc OSYS sonucu olmazsa diye, isimizi garentiye alalım
	if int(sonsinavid) > 1659 and aciklananadres.text == u'2014-ÖSYS Sonuçları':
		print 'Açıklanan sınav ID: ' + str(sonsinavid)
		kimden = 'kaanklky@gmail.com'
		#Sonuclar aciklandiginda bana da e-posta at diyen arkadaşlariniz e-posta adreslerini ',' ile ayirarak yazabilirsiniz. Asagida 3 kisiye yolladik mesela
		kime  = ['kaanklky@gmail.com','kaanklky@gmail.com', 'kaanklky@gmail.com']
		#E-posta iletimizin icerigi, burayi dogru doldurmak size kalmis.
		ileti = '\r\n'.join([
  			'From: kaanklky@gmai.com',
  			'To: kaanklky@gmai.com, kaanklky@gmail.com, kaanklky@gmail.com',
  			'Subject: ÖSYM Habercisi',
  			'',
  			'ÖSYM sonuçları açıklandı la! Kalk bir bak hele.'
  		])
		kullaniciadi = 'kaanklky@gmail.com'
		parola = '********'
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(kullaniciadi,parola)
		server.sendmail(kimden, kime, ileti)
		server.quit()
		print 'E-posta Gönderildi!'
	else:
		print 'Açıklanan sınav yok.'