# Django CV Web Uygulaması - Proje Açıklaması

Bu döküman, Django CV Web Uygulamasının kurulum adımlarını ve ön yüz bileşenlerini açıklamaktadır.

## Kurulum Aşamaları

### Docker ile Kurulum (Önerilen)

1. **Gereksinimleri Karşılayın:**
   - Docker ve Docker Compose yüklü olmalıdır
   - Git (projeyi klonlamak için)

2. **Projeyi Çalıştırın:**
   ```bash
   # Docker konteynerini oluşturun ve başlatın
   docker-compose up --build
   ```

3. **Erişim:**
   - Web sitesi: http://localhost:8000
   - Admin paneli: http://localhost:8000/admin
   - Giriş bilgileri: kullanıcı adı: admin, şifre: adminpassword123

### Manuel Kurulum

1. **Gereksinimleri Karşılayın:**
   - Python 3.9+ yüklü olmalıdır
   - pip (Python paket yöneticisi)

2. **Bağımlılıkları Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Veritabanını Oluşturun:**
   ```bash
   python manage.py migrate
   ```

4. **Admin Kullanıcısını Oluşturun:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Geliştirme Sunucusunu Başlatın:**
   ```bash
   python manage.py runserver
   ```

6. **Erişim:**
   - Web sitesi: http://localhost:8000
   - Admin paneli: http://localhost:8000/admin

## Ön Yüz Bileşenleri ve Dosyaları

### 1. Ana Şablon (Base Template)

**Dosya:** `cv_app/templates/cv_app/base.html`

Bu dosya, sitenin ana iskeletini oluşturur. Tüm ortak HTML yapısını, CSS bağlantılarını ve JavaScript dosyalarını içerir. Diğer şablonlar bu ana şablonu genişletir.

Önemli Özellikler:
- Siyah tema renk şeması tanımları
- Duyarlı (responsive) tasarım için meta etiketleri
- Sayfa yapısı (header, main content, footer)

### 2. Ana Sayfa (CV Görünümü)

**Dosya:** `cv_app/templates/cv_app/home.html`

Bu dosya, ziyaretçilerin gördüğü CV sayfasını oluşturur. Kişisel bilgiler, eğitim, iş deneyimi ve yetenekler bölümlerini içerir.

Nasıl Çalışır:
- `base.html` şablonunu genişletir
- Django template dilini kullanarak veritabanından CV verilerini gösterir
- Bilgileri profesyonel bir düzende organize eder

### 3. Admin Paneli (CV Yönetimi)

**Dosya:** `cv_app/templates/cv_app/cv_admin.html`

Bu dosya, özel CV yönetim panelini oluşturur. Tüm CV içeriğini tek bir sayfada alt alta düzenlemeyi sağlar.

Nasıl Çalışır:
- Bootstrap CSS framework kullanır
- Tüm form alanlarını tek sayfada düzenler
- POST istekleriyle verileri kaydeder/günceller/siler

### 4. CSS Stil Dosyaları

**Dosya:** `cv_app/static/cv_app/css/style.css`

Bu dosya, CV websitesinin görsel stilini tanımlar:
- Siyah tema renkleri ve tipografi
- Düzen ve boşluklar
- Duyarlı tasarım kuralları

**Dosya:** `static/css/main.css`

Proje seviyesinde paylaşılan CSS stilleri.

## Çalışma Prensibi

1. **URL Yönlendirmesi:**
   - `cv_project/urls.py` - Ana URL yönlendirme yapılandırması
   - `cv_app/urls.py` - CV uygulaması URL yönlendirmeleri

2. **Veri Akışı:**
   - `views.py` - Veritabanından verileri alıp şablonlara aktaran görünüm fonksiyonları
   - `models.py` - CV verilerinin yapısını ve ilişkilerini tanımlayan veritabanı modelleri

3. **Kullanıcı Etkileşimi:**
   - Ziyaretçiler `/` URL'inde CV'yi görüntüler
   - Yönetici `/admin/` URL'inde otomatik olarak CV yönetim paneline yönlendirilir
   - Panel, tüm CV bölümlerini alt alta tek sayfada düzenleme imkanı sunar
