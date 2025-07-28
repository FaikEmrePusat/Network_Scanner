# Network_Scanner

## Proje Amacı
Network_Scanner, yerel ağınızdaki cihazları tespit etmek, port taraması yapmak ve temel güvenlik kontrolleri gerçekleştirmek için geliştirilmiş bir Python tabanlı ağ analiz aracıdır. Proje, ağ yöneticileri ve siber güvenlik meraklıları için hızlı, esnek ve modüler bir çözüm sunar.

---

## Özellikler
- **Ağ Cihazı Keşfi:** Yerel ağdaki aktif cihazların IP ve MAC adreslerini tespit eder.
- **Port Taraması:** Belirli bir IP adresinde veya birden fazla cihazda, belirli port aralıklarında açık TCP portlarını hızlıca bulur. Paralel tarama için `concurrent.futures.ThreadPoolExecutor` kullanılır.
- **Vendor Bilgisi:** MAC adreslerinden üretici (vendor) bilgisini sorgular.
- **Güvenlik Kontrolleri:** Temel güvenlik açıklarını tespit etmeye yönelik modüller içerir (örn. port tarama, ARP analizi için altyapı).
- **Modüler Mimari:** Her işlev ayrı bir Python modülünde yer alır, kolayca genişletilebilir.

---

## Teknik Mimari

```
Network_Scanner/
├── main.py                # Ana uygulama, kullanıcı arayüzü ve akış kontrolü
├── inventory_scanner.py   # Ağ cihazı keşfi ve IP/MAC toplama
├── security_checks/
│   ├── port_scanner.py    # Paralel port tarama modülü
│   └── ...                # Diğer güvenlik modülleri
├── network/               # Ağ işlemleriyle ilgili yardımcı modüller
├── output/                # Sonuçların ve logların kaydedildiği klasör
├── requirements.txt       # Gerekli Python paketleri
└── README.md              # Proje dokümantasyonu
```

---

## Kullanım

### 1. Ortamı Hazırlama
Python 3.8+ gereklidir. Gerekli paketleri yüklemek için:
```bash
pip install -r requirements.txt
```

### 2. Programı Çalıştırma
```bash
python main.py
```
Konsolda, IP aralığı seçimi ve vendor bilgisi sorgulama gibi seçenekler sunulur.

### 3. Port Taraması
- Belirli bir IP veya cihaz listesi için port taraması yapılabilir.
- Port tarama işlemi, çoklu iş parçacığı ile hızlıca tamamlanır.

### 4. Sonuçlar
- Tespit edilen cihazlar, açık portlar ve vendor bilgileri ekrana ve/veya `output/` klasörüne kaydedilir.

---

## Teknik Detaylar

### Port Tarama (security_checks/port_scanner.py)
- `scan_ports(target_ip, start_port, end_port, max_workers)` fonksiyonu, ThreadPoolExecutor ile paralel port taraması yapar.
- Her port için ayrı bir iş parçacığı başlatılır, açık portlar anında ekrana ve listeye yazılır.
- Yüksek performans ve ölçeklenebilirlik sağlar.

### Cihaz Keşfi (inventory_scanner.py)
- Ağdaki aktif cihazlar ICMP ping ve/veya ARP sorguları ile tespit edilir.
- MAC adreslerinden vendor bilgisi alınabilir.

### Modülerlik
- Yeni güvenlik kontrolleri veya analizler eklemek için `security_checks/` klasörüne yeni modüller ekleyebilirsiniz.

---

## Gereksinimler
- Python 3.8 veya üzeri
- `scapy`, `concurrent.futures` (standart kütüphane), `requests` (vendor lookup için)
- Yönetici/root yetkisi (bazı ağ işlemleri için gerekebilir)

---

## Katkı ve Geliştirme
- Kodlar modüler ve okunabilir şekilde yazılmıştır.
- Pull request ve issue açarak katkıda bulunabilirsiniz.

---

## Lisans
MIT Lisansı ile lisanslanmıştır. 