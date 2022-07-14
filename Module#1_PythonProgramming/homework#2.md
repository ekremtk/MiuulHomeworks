* Görev 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.</b>
  * conda create -n etkenv python=3
    * etkenv burada env ismidir değişiklik gösterilebilir.
    * python=3 ile python versiyonu belirtildi. Mecburi değildir. 

<p align="center">
<img height=50 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G1.png"/>
<img height=350 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G1_2.png"/>
<img height=250 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G1_3.png"/>
</p>


* Görev 2: Oluşturduğunuz environment'ı aktif ediniz.
  * conda activate etkenv 

<p align="center">
<img height=100 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G2.png"/>
</p>


* Görev 3: Yüklü paketleri listeleyiniz.
  * conda list
 
<p align="center">
<img height=350 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G3.png"/>
</p>

* Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın1.2.1 versiyonunu aynı anda indiriniz.
  * conda install numpy pandas=1.2.1

<p align="center">
<img height=50 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G4_1.png"/>
<img height=350 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G4_2.png"/>
<img height=350 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G4_3.png"/>
</p>

* Görev 5: İndirilen Numpy'ın versiyonu nedir?
  * conda list numpy

<p align="center">
<img height=150 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G5.png"/>
</p>

* Görev 6: Pandas'ı upgrade ediniz. Yeni versiyonu nedir?
  * conda update pandas

<p align="center">
<img height=50 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G6_1.png"/>
<img height=300 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G6_2.png"/>
<img height=100 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G6_3.png"/>
</p>

* Görev 7: Numpy'ı environment'tan siliniz.
  * conda remove numpy

<p align="center">
<img height=50 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G7_1.png"/>
<img height=350 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G7_2.png"/>
</p>

* Görev 8: Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.
  * conda install seaborn matplotlib

<p align="center">
<img height=50 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G8_1.png"/>
<img height=350 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G8_2.png"/>
</p>

* Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
  * conda env export > etkenv.yaml
    * etkenv.yaml kısmında bulunan etkenv değiştirilebilir
    * yaml dosyası ile bütün yüklü kütüphane bilgileri çekilir 

<p align="center">
<img height=50 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G9_1.png"/>
<img height=350 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G9_2.png"/>
</p>

* Görev 10: Oluşturduğunuz environment'i siliniz. Önce environment'i deactivate ediniz.
  * conda deactive ==> ile ilgili environment deaktif hale getilir
  * conda remove --name etkenv --all
  
<p align="center">
<img height=50 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G10_1.png"/>
<img height=250 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G10_2.png"/>
<img height=150 src="https://github.com/ekremtk/MiuulHomeworks/blob/master/figures/HW2-G10_3.png"/>
</p> 
