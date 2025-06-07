# Turing_Machine
Kullanıcıdan alınan bir PIN kodunun sistemde kayıtlı olan PIN koduyla eşleşip eşleşmediğini kontrol eden bir Turing makinesi tasarımı.

# Program Nasıl Çalışır ?

Program öncelikle kullanıcıdan 4 haneli bir PIN alır ve bu değeri sistemde tanımlı olan PIN ile birlikte #KullanıcıPIN#SistemPIN# formatına getirir ve sonrasında turing makinesi çalışmaya başlar. Turing makinesi öncelikli olarak q0 durumundadır ve bu durum ilk # karakterini okur, okuma kafası sağa kayar ve sistem q1 durumuna geçer q1 ise kullanıcı PIN değerindeki işaretlemeyen ilk rakamı "X" ile işaretler, ayrıca sistem daha önce işaretlediği rakamları atlar ve atladığı sırada ikinci # karakterine denk gelirse tüm sistem PIN değerlerinin de işaretlenip işaretlenmediğini kontrol eden q6 durumuna geçer.Ancak sistem daha önce tüm PIN değerlerini işaretlemediyse sistem q2 durumuna geçer. q2 durumu ise ikinici # karakterine kadar gidilmesini sağlar ve # karakteri bulunduğu zaman sistem q3 durumuna geçer. q3 durumunda ise kullanıcı PIN değeri ile eşleşen rakam "Y" ile işaretlenir, okuma kafası sola geçer ve sistem q4 durumuna geçer. q4 durumu ikinci # karakterine kadar okuma kafasını sırasıyla sol tarafa kaydırır. İkinci # karakteri bulunduğu zaman ise q5 durumuna geçilir ve q5 durumunda ise ilk # karakterine kadar okuma kafası sola kaydırılır.Birinci # karakterine ulaşıldığında ise sistem tekrardan kullanıcı PIN'i üzerinde bir işaretleme yapması gerekiyorsa yapar ve sonrasında ise önceki işlemleri tekrarlar. Tüm PIN değerlerinin işaretlenme ve eşitlik durumuna göre ise q7 aksi takdirde ise q8 durumuna geçerek kullanıcıya PIN değerlerinin eşleşiğ eşleşmediği bilgisini verir.

# Program Nasıl Çalıştırılır ? 

Konsol üzerinden py turing_proje.py ya da herhangi bir ide üzerinden çalıştırabilirsiniz. Program çalıştırıldığında kullanıcıya turing makinesinin çalıştırılması ya da çıkış yapılması üzerine seçim yapılması istenecektir. (Sırasıyla 1,2 girebilirsiniz) Sonrasında ise program kullanıcıya kullanıcının girdiği PIN değerini ve sistemde kayıtlı olan PIN değerini gösterecek ve PIN formatlamasını yapacaktır ardından ise turing makinesi bandı adım adım gösterilecek ve her adımda makinenin hangi durumda olduğu da yanında gösterilecekitr. Sistem PIN değerlerinin eşleşip eşleşmemesine göre kullanıcıya "Şifre doğru" veya "Şifre yanlış" mesajlarını gösterecektir ve böylelikle kullanıcının girdiği pin değerine göre makine çalışmasını tamamlayacaktır. Ardından seçim ekranı kullanıcı çıkış yapmak isteyene kadar kullanıcıya gösterilecektir.

# Örnek Testler

## TEST 1
<pre>
1. PIN Doğrulama
2. Çıkış

Seçim (1-2): 1 
4 haneli PIN: 1223

Kullanıcının girdiği pin: '1223', Sistemde kayıtlı olan pin: '1234'
Giriş: #1223#1234#

Başlangıç: [#] 1  2  2  3  #  1  2  3  4  #
Adım 1: # [1] 2  2  3  #  1  2  3  4  # | q1
Adım 2: #  X [2] 2  3  #  1  2  3  4  # | q2
Adım 3: #  X  2 [2] 3  #  1  2  3  4  # | q2
Adım 4: #  X  2  2 [3] #  1  2  3  4  # | q2
Adım 5: #  X  2  2  3 [#] 1  2  3  4  # | q2
Adım 6: #  X  2  2  3  # [1] 2  3  4  # | q3
Adım 7: #  X  2  2  3 [#] Y  2  3  4  # | q4
Adım 8: #  X  2  2 [3] #  Y  2  3  4  # | q5
Adım 9: #  X  2 [2] 3  #  Y  2  3  4  # | q5
Adım 10: #  X [2] 2  3  #  Y  2  3  4  # | q5
Adım 11: # [X] 2  2  3  #  Y  2  3  4  # | q5
Adım 12: [#] X  2  2  3  #  Y  2  3  4  # | q5
Adım 13: # [X] 2  2  3  #  Y  2  3  4  # | q1
Adım 14: #  X [2] 2  3  #  Y  2  3  4  # | q1
Adım 15: #  X  X [2] 3  #  Y  2  3  4  # | q2
Adım 16: #  X  X  2 [3] #  Y  2  3  4  # | q2
Adım 17: #  X  X  2  3 [#] Y  2  3  4  # | q2
Adım 18: #  X  X  2  3  # [Y] 2  3  4  # | q3
Adım 19: #  X  X  2  3  #  Y [2] 3  4  # | q3
Adım 20: #  X  X  2  3  # [Y] Y  3  4  # | q4
Adım 21: #  X  X  2  3 [#] Y  Y  3  4  # | q4
Adım 22: #  X  X  2 [3] #  Y  Y  3  4  # | q5
Adım 23: #  X  X [2] 3  #  Y  Y  3  4  # | q5
Adım 24: #  X [X] 2  3  #  Y  Y  3  4  # | q5
Adım 25: # [X] X  2  3  #  Y  Y  3  4  # | q5
Adım 26: [#] X  X  2  3  #  Y  Y  3  4  # | q5
Adım 27: # [X] X  2  3  #  Y  Y  3  4  # | q1
Adım 28: #  X [X] 2  3  #  Y  Y  3  4  # | q1
Adım 29: #  X  X [2] 3  #  Y  Y  3  4  # | q1
Adım 30: #  X  X  X [3] #  Y  Y  3  4  # | q2
Adım 31: #  X  X  X  3 [#] Y  Y  3  4  # | q2
Adım 32: #  X  X  X  3  # [Y] Y  3  4  # | q3
Adım 25: # [X] X  2  3  #  Y  Y  3  4  # | q5
Adım 26: [#] X  X  2  3  #  Y  Y  3  4  # | q5
Adım 27: # [X] X  2  3  #  Y  Y  3  4  # | q1
Adım 28: #  X [X] 2  3  #  Y  Y  3  4  # | q1
Adım 29: #  X  X [2] 3  #  Y  Y  3  4  # | q1
Adım 30: #  X  X  X [3] #  Y  Y  3  4  # | q2
Adım 31: #  X  X  X  3 [#] Y  Y  3  4  # | q2
Adım 32: #  X  X  X  3  # [Y] Y  3  4  # | q3
Adım 33: #  X  X  X  3  #  Y [Y] 3  4  # | q3
Adım 34: #  X  X  X  3  #  Y  Y [3] 4  # | q3
Sonuç: q8
Şifre hatalı
</pre>

## TEST 2
<pre>
1. PIN Doğrulama
2. Çıkış     

Seçim (1-2): 1
4 haneli PIN: 1234

Kullanıcının girdiği pin: '1234', Sistemde kayıtlı olan pin: '1234'
Giriş: #1234#1234#

Başlangıç: [#] 1  2  3  4  #  1  2  3  4  #
Adım 1: # [1] 2  3  4  #  1  2  3  4  # | q1
Adım 2: #  X [2] 3  4  #  1  2  3  4  # | q2
Adım 3: #  X  2 [3] 4  #  1  2  3  4  # | q2
Adım 4: #  X  2  3 [4] #  1  2  3  4  # | q2
Adım 5: #  X  2  3  4 [#] 1  2  3  4  # | q2
Adım 6: #  X  2  3  4  # [1] 2  3  4  # | q3
Adım 7: #  X  2  3  4 [#] Y  2  3  4  # | q4
Adım 8: #  X  2  3 [4] #  Y  2  3  4  # | q5
Adım 9: #  X  2 [3] 4  #  Y  2  3  4  # | q5
Adım 10: #  X [2] 3  4  #  Y  2  3  4  # | q5
Adım 11: # [X] 2  3  4  #  Y  2  3  4  # | q5
Adım 12: [#] X  2  3  4  #  Y  2  3  4  # | q5
Adım 13: # [X] 2  3  4  #  Y  2  3  4  # | q1
Adım 14: #  X [2] 3  4  #  Y  2  3  4  # | q1
Adım 15: #  X  X [3] 4  #  Y  2  3  4  # | q2
Adım 16: #  X  X  3 [4] #  Y  2  3  4  # | q2
Adım 17: #  X  X  3  4 [#] Y  2  3  4  # | q2
Adım 18: #  X  X  3  4  # [Y] 2  3  4  # | q3
Adım 19: #  X  X  3  4  #  Y [2] 3  4  # | q3
Adım 20: #  X  X  3  4  # [Y] Y  3  4  # | q4
Adım 21: #  X  X  3  4 [#] Y  Y  3  4  # | q4
Adım 22: #  X  X  3 [4] #  Y  Y  3  4  # | q5
Adım 23: #  X  X [3] 4  #  Y  Y  3  4  # | q5
Adım 24: #  X [X] 3  4  #  Y  Y  3  4  # | q5
Adım 25: # [X] X  3  4  #  Y  Y  3  4  # | q5
Adım 26: [#] X  X  3  4  #  Y  Y  3  4  # | q5
Adım 27: # [X] X  3  4  #  Y  Y  3  4  # | q1
Adım 28: #  X [X] 3  4  #  Y  Y  3  4  # | q1
Adım 29: #  X  X [3] 4  #  Y  Y  3  4  # | q1
Adım 30: #  X  X  X [4] #  Y  Y  3  4  # | q2
Adım 31: #  X  X  X  4 [#] Y  Y  3  4  # | q2
Adım 32: #  X  X  X  4  # [Y] Y  3  4  # | q3
Adım 33: #  X  X  X  4  #  Y [Y] 3  4  # | q3
Adım 34: #  X  X  X  4  #  Y  Y [3] 4  # | q3
Adım 35: #  X  X  X  4  #  Y [Y] Y  4  # | q4
Adım 36: #  X  X  X  4  # [Y] Y  Y  4  # | q4
Adım 37: #  X  X  X  4 [#] Y  Y  Y  4  # | q4
Adım 38: #  X  X  X [4] #  Y  Y  Y  4  # | q5
Adım 39: #  X  X [X] 4  #  Y  Y  Y  4  # | q5
Adım 40: #  X [X] X  4  #  Y  Y  Y  4  # | q5
Adım 41: # [X] X  X  4  #  Y  Y  Y  4  # | q5
Adım 42: [#] X  X  X  4  #  Y  Y  Y  4  # | q5
Adım 43: # [X] X  X  4  #  Y  Y  Y  4  # | q1
Adım 44: #  X [X] X  4  #  Y  Y  Y  4  # | q1
Adım 45: #  X  X [X] 4  #  Y  Y  Y  4  # | q1
Adım 46: #  X  X  X [4] #  Y  Y  Y  4  # | q1
Adım 47: #  X  X  X  X [#] Y  Y  Y  4  # | q2
Adım 48: #  X  X  X  X  # [Y] Y  Y  4  # | q3
Adım 49: #  X  X  X  X  #  Y [Y] Y  4  # | q3
Adım 50: #  X  X  X  X  #  Y  Y [Y] 4  # | q3
Adım 51: #  X  X  X  X  #  Y  Y  Y [4] # | q3
Adım 52: #  X  X  X  X  #  Y  Y [Y] Y  # | q4
Adım 53: #  X  X  X  X  #  Y [Y] Y  Y  # | q4
Adım 54: #  X  X  X  X  # [Y] Y  Y  Y  # | q4
Adım 55: #  X  X  X  X [#] Y  Y  Y  Y  # | q4
Adım 56: #  X  X  X [X] #  Y  Y  Y  Y  # | q5
Adım 57: #  X  X [X] X  #  Y  Y  Y  Y  # | q5
Adım 58: #  X [X] X  X  #  Y  Y  Y  Y  # | q5
Adım 59: # [X] X  X  X  #  Y  Y  Y  Y  # | q5
Adım 60: [#] X  X  X  X  #  Y  Y  Y  Y  # | q5
Adım 61: # [X] X  X  X  #  Y  Y  Y  Y  # | q1
Adım 62: #  X [X] X  X  #  Y  Y  Y  Y  # | q1
Adım 63: #  X  X [X] X  #  Y  Y  Y  Y  # | q1
Adım 64: #  X  X  X [X] #  Y  Y  Y  Y  # | q1
Adım 65: #  X  X  X  X [#] Y  Y  Y  Y  # | q1
Adım 66: #  X  X  X  X  # [Y] Y  Y  Y  # | q6
Adım 67: #  X  X  X  X  #  Y [Y] Y  Y  # | q6
Adım 68: #  X  X  X  X  #  Y  Y [Y] Y  # | q6
Adım 69: #  X  X  X  X  #  Y  Y  Y [Y] # | q6
Adım 70: #  X  X  X  X  #  Y  Y  Y  Y [#] | q6
Adım 71: #  X  X  X  X  #  Y  Y  Y  Y  # | q7
Sonuç: q7
Şifre doğru
</pre>

## TEST 3
<pre>
1. PIN Doğrulama
2. Çıkış     

Seçim (1-2): 1
4 haneli PIN: 1357

Kullanıcının girdiği pin: '1357', Sistemde kayıtlı olan pin: '1357'
Giriş: #1357#1357#

Başlangıç: [#] 1  3  5  7  #  1  3  5  7  #
Adım 1: # [1] 3  5  7  #  1  3  5  7  # | q1
Adım 2: #  X [3] 5  7  #  1  3  5  7  # | q2
Adım 3: #  X  3 [5] 7  #  1  3  5  7  # | q2
Adım 4: #  X  3  5 [7] #  1  3  5  7  # | q2
Adım 5: #  X  3  5  7 [#] 1  3  5  7  # | q2
Adım 6: #  X  3  5  7  # [1] 3  5  7  # | q3
Adım 7: #  X  3  5  7 [#] Y  3  5  7  # | q4
Adım 8: #  X  3  5 [7] #  Y  3  5  7  # | q5
Adım 9: #  X  3 [5] 7  #  Y  3  5  7  # | q5
Adım 10: #  X [3] 5  7  #  Y  3  5  7  # | q5
Adım 11: # [X] 3  5  7  #  Y  3  5  7  # | q5
Adım 12: [#] X  3  5  7  #  Y  3  5  7  # | q5
Adım 13: # [X] 3  5  7  #  Y  3  5  7  # | q1
Adım 14: #  X [3] 5  7  #  Y  3  5  7  # | q1
Adım 15: #  X  X [5] 7  #  Y  3  5  7  # | q2
Adım 16: #  X  X  5 [7] #  Y  3  5  7  # | q2
Adım 17: #  X  X  5  7 [#] Y  3  5  7  # | q2
Adım 18: #  X  X  5  7  # [Y] 3  5  7  # | q3
Adım 19: #  X  X  5  7  #  Y [3] 5  7  # | q3
Adım 20: #  X  X  5  7  # [Y] Y  5  7  # | q4
Adım 21: #  X  X  5  7 [#] Y  Y  5  7  # | q4
Adım 22: #  X  X  5 [7] #  Y  Y  5  7  # | q5
Adım 23: #  X  X [5] 7  #  Y  Y  5  7  # | q5
Adım 24: #  X [X] 5  7  #  Y  Y  5  7  # | q5
Adım 25: # [X] X  5  7  #  Y  Y  5  7  # | q5
Adım 26: [#] X  X  5  7  #  Y  Y  5  7  # | q5
Adım 27: # [X] X  5  7  #  Y  Y  5  7  # | q1
Adım 28: #  X [X] 5  7  #  Y  Y  5  7  # | q1
Adım 29: #  X  X [5] 7  #  Y  Y  5  7  # | q1
Adım 30: #  X  X  X [7] #  Y  Y  5  7  # | q2
Adım 31: #  X  X  X  7 [#] Y  Y  5  7  # | q2
Adım 32: #  X  X  X  7  # [Y] Y  5  7  # | q3
Adım 33: #  X  X  X  7  #  Y [Y] 5  7  # | q3
Adım 34: #  X  X  X  7  #  Y  Y [5] 7  # | q3
Adım 35: #  X  X  X  7  #  Y [Y] Y  7  # | q4
Adım 36: #  X  X  X  7  # [Y] Y  Y  7  # | q4
Adım 37: #  X  X  X  7 [#] Y  Y  Y  7  # | q4
Adım 38: #  X  X  X [7] #  Y  Y  Y  7  # | q5
Adım 39: #  X  X [X] 7  #  Y  Y  Y  7  # | q5
Adım 40: #  X [X] X  7  #  Y  Y  Y  7  # | q5
Adım 41: # [X] X  X  7  #  Y  Y  Y  7  # | q5
Adım 42: [#] X  X  X  7  #  Y  Y  Y  7  # | q5
Adım 43: # [X] X  X  7  #  Y  Y  Y  7  # | q1
Adım 44: #  X [X] X  7  #  Y  Y  Y  7  # | q1
Adım 45: #  X  X [X] 7  #  Y  Y  Y  7  # | q1
Adım 46: #  X  X  X [7] #  Y  Y  Y  7  # | q1
Adım 47: #  X  X  X  X [#] Y  Y  Y  7  # | q2
Adım 48: #  X  X  X  X  # [Y] Y  Y  7  # | q3
Adım 49: #  X  X  X  X  #  Y [Y] Y  7  # | q3
Adım 50: #  X  X  X  X  #  Y  Y [Y] 7  # | q3
Adım 51: #  X  X  X  X  #  Y  Y  Y [7] # | q3
Adım 52: #  X  X  X  X  #  Y  Y [Y] Y  # | q4
Adım 53: #  X  X  X  X  #  Y [Y] Y  Y  # | q4
Adım 54: #  X  X  X  X  # [Y] Y  Y  Y  # | q4
Adım 55: #  X  X  X  X [#] Y  Y  Y  Y  # | q4
Adım 56: #  X  X  X [X] #  Y  Y  Y  Y  # | q5
Adım 57: #  X  X [X] X  #  Y  Y  Y  Y  # | q5
Adım 58: #  X [X] X  X  #  Y  Y  Y  Y  # | q5
Adım 59: # [X] X  X  X  #  Y  Y  Y  Y  # | q5
Adım 60: [#] X  X  X  X  #  Y  Y  Y  Y  # | q5
Adım 61: # [X] X  X  X  #  Y  Y  Y  Y  # | q1
Adım 62: #  X [X] X  X  #  Y  Y  Y  Y  # | q1
Adım 63: #  X  X [X] X  #  Y  Y  Y  Y  # | q1
Adım 64: #  X  X  X [X] #  Y  Y  Y  Y  # | q1
Adım 65: #  X  X  X  X [#] Y  Y  Y  Y  # | q1
Adım 66: #  X  X  X  X  # [Y] Y  Y  Y  # | q6
Adım 67: #  X  X  X  X  #  Y [Y] Y  Y  # | q6
Adım 68: #  X  X  X  X  #  Y  Y [Y] Y  # | q6
Adım 69: #  X  X  X  X  #  Y  Y  Y [Y] # | q6
Adım 70: #  X  X  X  X  #  Y  Y  Y  Y [#] | q6
Adım 71: #  X  X  X  X  #  Y  Y  Y  Y  # | q7
Sonuç: q7
Şifre doğru
</pre>

## TEST 4
<pre>
1. PIN Doğrulama
2. Çıkış

Seçim (1-2): 1
4 haneli PIN: 2356

Kullanıcının girdiği pin: '2356', Sistemde kayıtlı olan pin: '1357'
Giriş: #2356#1357#

>Başlangıç: [#] 2  3  5  6  #  1  3  5  7  #
Adım 1: # [2] 3  5  6  #  1  3  5  7  # | q1
Adım 2: #  X [3] 5  6  #  1  3  5  7  # | q2
Adım 3: #  X  3 [5] 6  #  1  3  5  7  # | q2
Adım 4: #  X  3  5 [6] #  1  3  5  7  # | q2
Adım 5: #  X  3  5  6 [#] 1  3  5  7  # | q2
Adım 6: #  X  3  5  6  # [1] 3  5  7  # | q3
Sonuç: q8
Şifre hatalı
</pre>
