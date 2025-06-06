"""'q0': 'İlk #'ı ara',
'q1': 'İlk PIN karakterini X ile işaretle',
'q2': 'İkinci #'e git',
'q3': 'Sistem PIN\'inde eşleşen karakteri Y ile işaretle',
'q4': 'İkinci #'a kadar geri dön',
'q5': 'İkinci #'ten geçerken geri dön',
'q6': 'Tüm karakterler Y ile işaretlendi mi kontrolü',
'q7': 'PIN doğru',
'q8': 'PIN yanlış' """

def make_transitions():
    transitions = {}
    digits = '0123456789'

    transitions[('q0', '#')] = ('q1', '#', 'R') # İlk # karakterini bulma

    for d in digits:
        transitions[('q1', d)] = ('q2', 'X', 'R') # PIN karakterini X ile işaretleme
    transitions[('q1', '#')] = ('q6', '#', 'R') # İkinci # karakteri bulunduğunda tüm karakterler işaretlendi mi?
    transitions[('q1', 'X')] = ('q1', 'X', 'R') # Zaten işaretlenmiş X karakterini atlama

    for d in digits:
        transitions[('q2', d)] = ('q2', d, 'R') # İkinci # karakterine kadar sağa gitme
    transitions[('q2', 'X')] = ('q2', 'X', 'R') # Zaten işaretlenmiş X karakterini atlama
    transitions[('q2', '#')] = ('q3', '#', 'R') # İkinci # karakterine ulaşıldı şimdi sistem PIN'ini işaretlemeye geçiş

    for d in digits:
        transitions[('q3', d)] = ('q4', 'Y', 'L') # Sistem PIN'inde eşleşen karakteri Y ile işaretleme
    transitions[('q3', 'Y')] = ('q3', 'Y', 'R') # Zaten işaretlenmiş Y karakterini atlayarak sağa gitme
    transitions[('q3', '#')] = ('q8', '#', 'R') # PIN yanlış durumu, çünkü sistem PIN'inde işaretlenmemiş karakter kaldı 3. #'a geldik

    transitions[('q4', 'Y')] = ('q4', 'Y', 'L') # 2. # karakterine kadar geri dönme
    transitions[('q4', '#')] = ('q5', '#', 'L') # İkinci # karakterine ulaşıldı şimdi ilk # karakterine geri dönme

    for d in digits:
        transitions[('q5', d)] = ('q5', d, 'L') # İlk # karakterine kadar geri dönme
    transitions[('q5', 'X')] = ('q5', 'X', 'L') # Zaten işaretlenmiş X karakterini atlayarak geri dönme
    transitions[('q5', '#')] = ('q1', '#', 'R') # İlk # karakterine ulaşıldı, şimdi tekrar PIN karakterlerini X ile işaretleme adımına geçiş

    transitions[('q6', 'Y')] = ('q6', 'Y', 'R') # Tüm karakterler Y ile işaretlendi mi kontrolü
    transitions[('q6', '#')] = ('q7', '#', 'R') # Başarı durumu, çünkü tüm karakterler Y ile işaretlendi
    for d in digits:
        transitions[('q6', d)] = ('q8', d, 'R') # İşaretlenmemiş karakter kaldı PIN yanlış

    return transitions

def display_tape(tape, head_position): # Her adımda bandın durumunu gösteren fonksiyon
    display = ""
    for i, char in enumerate(tape):
        if i == head_position:
            display += f"[{char}]"
        else:
            display += f" {char} "
    return display.strip()

def run_turing_machine(input_string):
    transitions = make_transitions() # Turing makinesi geçiş adımlarını oluşturma
    current_state = 'q0' # Başlangıç durumu
    head_position = 0  # Başlangıç pozisyonu
    tape = list(input_string) # Makine bandı liste olarak hazırlanıyor
    saved_char = None # Kullanıcı ve Sistem PIN'leri arasında karşılaştırma için geçici karakter saklama

    print(f"\nBaşlangıç: {display_tape(tape, head_position)}")

    step_num = 1 # Adım sayacı
    while current_state not in ['q7', 'q8']: # Başarılı veya başarısız durumuna gelene kadar döngü devam eder
        if head_position >= len(tape):    # #KullanıcıPIN#SistemPIN# formatındaki bandın sonuna ulaşana kadar bant B ile genişletilir
            tape.append('B')

        current_char = tape[head_position] # Mevcut karakteri al
        transition_key = (current_state, current_char) # Geçiş anahtarını oluştur

        if transition_key in transitions: # Geçiş anahtarının geçerli olup olmadığını kontrol et
            new_state, write_char, direction = transitions[transition_key] # Geçiş bilgilerini al

            if current_state == 'q1' and current_char in '0123456789': # Okunan PIN karakterini kaydetme
                saved_char = current_char

            elif current_state == 'q3' and current_char in '0123456789':
                if saved_char is None or saved_char != current_char: # Kullanıcı PIN karakteri ile sistem PIN karakteri eşleşmiyorsa başarısız duruma geç
                    current_state = 'q8'
                    break
                else:
                    saved_char = None # Eşleşme başarılı ise kaydedilen karakteri sıfırla

            tape[head_position] = write_char # Bandın mevcut pozisyonundaki karakter yerine  geçişte belirtilen karakteri yaz
            current_state = new_state # Yeni duruma geç

            if direction == 'R': # Bandın başını sağa kaydır
                head_position += 1
            elif direction == 'L': # Bandın başını sola kaydır (- indise dikkat ederek)
                head_position = max(0, head_position - 1)

            print(f"Adım {step_num}: {display_tape(tape, head_position)} | {current_state}") # Adım ve durumu gösterme
            step_num += 1
        else:
            current_state = 'q8' # Geçiş anahtarı bulunamazsa başarısız duruma geç
            break

    print(f"Sonuç: {current_state}") # Son durumu gösterme

    return current_state == 'q7' # Başarılı durum ise True, başarısız durum ise False döndürme

def validate_pin(user_pin, system_pin):
    tape_input = f"#{user_pin}#{system_pin}#" # PIN değerini #PIN#SistemPIN# formatında hazırlama

    print(f"\nKullanıcının girdiği pin: '{user_pin}', Sistemde kayıtlı olan pin: '{system_pin}'") # Kullanıcı ve sistem PIN'lerini gösterme
    print(f"Giriş: {tape_input}")   

    result = run_turing_machine(tape_input) # Turing makinesini çalıştırma (Hazırlanan formatta değişken ile)
    return result # True veya False olarak sonucu döndürme

def main():
    SYSTEM_PIN = "1234" # Sistemde kayıtlı PIN (Basit olması için sabit bir değer)

    while True:
        print("1. PIN Doğrulama") 
        print("2. Çıkış")
        choice = input("\nSeçim (1-2): ").strip()  # Pin doğrulama veya çıkış için seçim

        if choice == "1":
            user_pin = input("4 haneli PIN: ").strip() # Kullanıcıdan 4 haneli PIN girişi

            if len(user_pin) != 4 or not user_pin.isdigit(): # PIN değerinin 4 haneli ve rakamlardan oluşup oluşmadığını kontrol etme
                print("PIN 4 rakamdan oluşmalıdır!")
                continue

            result = validate_pin(user_pin, SYSTEM_PIN) # Doğrulama işlemi başlatma

            if result:                # Doğrulama sonucuna göre mesaj verme
                print("Şifre doğru")
            else:
                print("Şifre hatalı")

        elif choice == "2": # Çıkış seçeneği
            break

        else:
            print("Geçersiz seçim!") # Geçersiz seçim kontrolü

if __name__ == "__main__":
    main()