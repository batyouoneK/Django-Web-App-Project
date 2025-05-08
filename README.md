# CV Web Sitesi Projesi - Detaylı Anlatım
## Batuhan Kızıltaş Django Web App Projesi

## Projeyi Başlatma Adımları

### Gereksinimler
- [Docker](https://www.docker.com/products/docker-desktop) (Docker Desktop'ı indirip kurmalısınız)
- [Git](https://git-scm.com/downloads) (İsteğe bağlı, eğer projeyi klonlamak istiyorsanız)

### Adım Adım Kurulum

1. **Projeyi bilgisayarınıza indirin**
   ```bash
   git clone <repository_url>
   cd proje_klasörü
   ```

2. **Docker konteynerlerini başlatın**
   ```bash
   docker-compose up -d
   ```
   Bu komut, web uygulaması ve PostgreSQL veritabanı konteynerlerini başlatacaktır.

3. **Admin paneli için süper kullanıcı oluşturun**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
   İstenilen bilgileri girin (kullanıcı adı, e-posta, şifre).

4. **Uygulamaya erişim**
   - Web sitesi: http://localhost:8000
   - Admin paneli: http://localhost:8000/admin

5. **Admin panelinden CV içeriğini ekleyin**
   - Giriş yaptıktan sonra, kişisel bilgiler, eğitim geçmişi, iş deneyimleri, beceriler, projeler ve sertifikalar ekleyebilirsiniz.

6. **Konteynerları durdurmak için**
   ```bash
   docker-compose down
   ```

## Django Nedir?

Django, Python programlama diliyle yazılmış, hızlı geliştirme, temiz ve pragmatik tasarımı teşvik eden bir web framework'üdür. 2005 yılında yayınlanan Django, "pil dahil" felsefesine sahiptir - yani bir web uygulaması geliştirmek için ihtiyaç duyacağınız birçok bileşen Django ile birlikte gelir.

### Django'nun Ana Özellikleri

1. **MVT (Model-View-Template) Mimarisi**
   - **Model**: Veritabanı yapısını tanımlar ve veri manipülasyonu sağlar.
   - **View**: Kullanıcı isteklerini işler ve uygun yanıtları döndürür.
   - **Template**: HTML sayfalarının nasıl render edileceğini tanımlar.

2. **ORM (Object-Relational Mapping)**
   - Veritabanı işlemlerini SQL yazmadan Python sınıfları üzerinden yapmanızı sağlar.
   - Farklı veritabanı sistemleri arasında geçiş yapmanızı kolaylaştırır.

3. **Admin Paneli**
   - Otomatik olarak oluşturulan, özelleştirilebilir bir yönetim arayüzü sunar.
   - Modelleri kaydetme, güncelleme, silme işlemlerini kolaylaştırır.

4. **URL Routing**
   - URL şablonlarını Python fonksiyonlarına bağlamanızı sağlar.
   - Temiz ve SEO dostu URL'ler oluşturmanıza yardımcı olur.

5. **Form İşleme**
   - HTML formlarının oluşturulması, doğrulanması ve işlenmesi için araçlar sunar.

6. **Kimlik Doğrulama ve Yetkilendirme**
   - Kullanıcı hesapları, gruplar, izinler ve oturum yönetimi için hazır sistemler.

7. **Güvenlik**
   - CSRF koruması, SQL enjeksiyon koruması, XSS koruması gibi güvenlik önlemleri.

8. **Şablon Sistemi**
   - Güçlü bir şablon dili ile dinamik HTML sayfaları oluşturmanızı sağlar.
   - Şablon kalıtımı, filtreler, etiketler gibi özellikler sunar.

### Django Proje Yapısı

Tipik bir Django projesi şu şekilde organize edilir:

```
project_name/
├── manage.py            # Proje yönetim betiği
├── project_name/        # Proje çekirdek klasörü
│   ├── __init__.py      # Python paketi olduğunu belirtir
│   ├── settings.py      # Proje ayarları
│   ├── urls.py          # Ana URL yönlendirmeleri
│   ├── asgi.py          # ASGI uyumlu web sunucuları için
│   └── wsgi.py          # WSGI uyumlu web sunucuları için
├── app_name/            # Uygulama klasörü
│   ├── __init__.py
│   ├── admin.py         # Admin paneli konfigürasyonu
│   ├── apps.py          # Uygulama konfigürasyonu
│   ├── models.py        # Veritabanı modelleri
│   ├── views.py         # İstek işleyicileri
│   ├── urls.py          # Uygulama URL yönlendirmeleri
│   ├── tests.py         # Testler
│   └── migrations/      # Veritabanı şema değişiklikleri
├── templates/           # HTML şablonları
└── static/              # CSS, JavaScript, resimler
```

### Django'nun Çalışma Prensibi

1. **İstek-Yanıt Döngüsü**
   - Kullanıcı bir URL'yi ziyaret eder.
   - Django, urls.py dosyasındaki URL şablonlarını kontrol eder.
   - Eşleşen URL şablonu bulunursa, ilgili view fonksiyonu çağrılır.
   - View fonksiyonu, modeller aracılığıyla veritabanından veri alabilir.
   - View, bir şablon kullanarak HTML oluşturur ve HTTP yanıtı olarak döndürür.

2. **Veritabanı İşlemleri**
   - Modeller, veritabanı tablolarını temsil eden Python sınıflarıdır.
   - ORM sayesinde, karmaşık SQL sorguları yazmak yerine Python kodu yazarsınız.
   - Örnek: `Person.objects.filter(first_name="John").order_by("-birth_date")`

3. **Şablonlar ile HTML Oluşturma**
   - Şablonlar, dinamik içerikle doldurulan HTML dosyalarıdır.
   - Django şablon dili sayesinde döngüler, koşullar, filtreler kullanabilirsiniz.
   - Örnek: `{% for item in items %} {{ item.name }} {% endfor %}`

## Docker Nedir?

Docker, uygulamaları geliştirmek, dağıtmak ve çalıştırmak için kullanılan açık kaynaklı bir platformdur. Docker, uygulamaları "konteynerler" olarak adlandırılan izole ortamlarda paketlemenizi sağlar. Bu konteynerler, uygulamanızın tüm bağımlılıklarını ve konfigürasyonlarını içerir.

### Docker'ın Temel Kavramları

1. **Konteyner**
   - Uygulamanın çalışması için gereken her şeyi (kod, runtime, sistem araçları, kütüphaneler) içeren standart bir yazılım birimi.
   - İzole edilmiş, hafif ve taşınabilir.
   - Her konteyner kendi CPU, bellek, blok I/O ve ağ kaynaklarını kullanır.
   - Sanal makinelerden farklı olarak, konteynerler işletim sistemi çekirdeğini paylaşır.

2. **İmaj (Image)**
   - Konteynerler için taşınabilir bir şablondur.
   - Uygulamanızın çalışması için gereken tüm dosyaları, bağımlılıkları ve konfigürasyonları içerir.
   - Katmanlı dosya sistemi kullanır, her katman bir değişikliği temsil eder.
   - İmajlar, Dockerfile adı verilen talimat dosyalarından oluşturulur.

3. **Dockerfile**
   - Bir Docker imajı oluşturmak için gereken adımları içeren metin dosyası.
   - Örnek talimatlar: FROM (temel imaj), RUN (komut çalıştırma), COPY (dosya kopyalama), ENV (ortam değişkeni).

4. **Docker Hub**
   - Docker imajlarını saklayabileceğiniz, paylaşabileceğiniz ve indirebileceğiniz bir bulut registry hizmetidir.
   - Resmi imajlar (Python, Node.js, PostgreSQL vb.) ve topluluk imajları bulunur.

5. **Docker Compose**
   - Çoklu konteyner uygulamalarını tanımlamak ve çalıştırmak için kullanılan bir araç.
   - YAML dosyası formatında servisler, ağlar ve hacimler tanımlanır.
   - Tek bir komutla birden fazla konteyneri başlatabilir ve yönetebilirsiniz.

### Docker'ın Avantajları

1. **Tutarlı Ortamlar**
   - "Benim bilgisayarımda çalışıyor" sorununu ortadan kaldırır.
   - Geliştirme, test ve üretim ortamları arasındaki farkları minimuma indirir.

2. **İzolasyon**
   - Uygulamalar, birbirlerini veya host sistemini etkilemeden çalışır.
   - Güvenliği artırır ve çakışmaları önler.

3. **Verimlilik**
   - Konteynerler saniyeler içinde başlatılır ve durdurulur.
   - Disk alanı ve sistem kaynakları verimli kullanılır.

4. **Ölçeklenebilirlik**
   - Aynı imajdan birden çok konteyner oluşturarak uygulamanızı kolayca ölçeklendirebilirsiniz.
   - Konteyner orkestrasyon araçları (Docker Swarm, Kubernetes) ile otomatik ölçeklendirme.

5. **Sürüm Kontrolü**
   - İmajlar sürümlendirilebilir ve eski sürümlere hızlıca dönülebilir.
   - Değişiklikler katmanlar halinde saklanır, bu da verimliliği artırır.

### Docker Komutları

1. **Temel Komutlar**
   - `docker run`: Konteyner çalıştırma
   - `docker ps`: Çalışan konteynerleri listeleme
   - `docker images`: İmajları listeleme
   - `docker build`: Dockerfile'dan imaj oluşturma
   - `docker stop`: Konteyneri durdurma
   - `docker rm`: Konteyneri silme
   - `docker rmi`: İmajı silme

2. **Docker Compose Komutları**
   - `docker-compose up`: Servisleri başlatma
   - `docker-compose down`: Servisleri durdurma ve konteynerleri silme
   - `docker-compose logs`: Servislerin loglarını görüntüleme
   - `docker-compose exec`: Çalışan bir konteynerde komut çalıştırma

## Bu Proje Hakkında Detaylı Bilgiler

Bu proje, Django web framework'ü kullanılarak geliştirilmiş ve Docker ile konteynerize edilmiş bir CV/Özgeçmiş web sitesidir. Proje, kişisel bilgiler, iş deneyimi, eğitim geçmişi, beceriler, projeler ve sertifikalar gibi özgeçmiş bölümlerini içeren modern ve responsive bir web arayüzü sunar.

### Proje Mimarisi

#### Django Uygulaması (cv_app)

Bu proje, bir ana Django projesi (`cv_project`) ve bir uygulama (`cv_app`) içerir. Uygulama, CV verilerini yönetmek ve görüntülemek için gerekli tüm bileşenleri içerir.

#### Veri Modelleri

`models.py` dosyasında tanımlanan ana veri modelleri şunlardır:

1. **PersonalInfo (Kişisel Bilgiler)**
   - Ad-soyad, profesyonel unvan, profil resmi, özet
   - İletişim bilgileri (e-posta, telefon, adres)
   - Sosyal medya bağlantıları (LinkedIn, GitHub, kişisel web sitesi)

2. **Education (Eğitim)**
   - Kurum adı, derece/sertifika, çalışma alanı
   - Başlangıç ve bitiş tarihleri
   - Açıklama ve konum

3. **WorkExperience (İş Deneyimi)**
   - Şirket adı, pozisyon
   - Başlangıç ve bitiş tarihleri
   - İş açıklaması ve konum

4. **Skill (Beceriler)**
   - Beceri adı ve kategorisi (teknik, kişisel, dil, diğer)
   - Yeterlilik seviyesi (1-100)
   - Görüntüleme sırası

5. **Project (Projeler)**
   - Proje başlığı, açıklaması, resmi
   - Kullanılan teknolojiler
   - Proje ve kaynak kodu bağlantıları
   - Öne çıkan proje göstergesi

6. **Certification (Sertifikalar)**
   - Sertifika adı, veren kuruluş
   - Veriliş ve geçerlilik tarihleri
   - Kimlik bilgisi ve bağlantı

#### Görünümler (Views)

`views.py` dosyasında tanımlanan görünümler:

1. **HomeView**
   - Ana CV sayfasını görüntüler
   - Tüm CV bölümlerini (kişisel bilgiler, eğitim, iş deneyimi, beceriler, öne çıkan projeler, sertifikalar) içerir

2. **ProjectDetailView**
   - Belirli bir projenin detaylarını görüntüler

3. **AllProjectsView**
   - Tüm projeleri listeler

4. **download_cv**
   - Yazdırılabilir/indirilebilir CV sürümünü oluşturur

#### Şablonlar (Templates)

Proje, Bootstrap 5 kullanarak modern ve responsive bir tasarım sunar. Ana şablonlar:

1. **base.html**
   - Tüm sayfaların temel yapısını ve ortak öğelerini içerir
   - Header, footer, meta etiketleri, CSS ve JavaScript dahil edilir

2. **home.html**
   - Ana CV sayfası
   - Tüm CV bölümlerini bölümler halinde gösterir

3. **project_detail.html**
   - Bir projenin detaylı görünümü

4. **all_projects.html**
   - Tüm projelerin listelendiği sayfa

5. **download_cv.html**
   - Yazdırma/indirme için optimize edilmiş CV formatı

#### URL Yönlendirme

`urls.py` dosyasında tanımlanan URL yönlendirmeleri:

1. `/` - Ana sayfa (CV ana sayfası)
2. `/project/<id>/` - Proje detay sayfası
3. `/projects/` - Tüm projeler sayfası
4. `/download-cv/` - CV indirme/yazdırma sayfası
5. `/admin/` - Django admin paneli

### Docker Yapılandırması

#### Dockerfile

`Dockerfile`, Django uygulamasını konteynerize etmek için gerekli adımları tanımlar:

1. Python 3.11 temel imajı kullanır
2. Ortam değişkenlerini ayarlar
3. Bağımlılıkları yükler
4. Proje dosyalarını kopyalar
5. Gunicorn web sunucusunu kullanarak uygulamayı çalıştırır

#### docker-compose.yml

`docker-compose.yml` dosyası, iki servis tanımlar:

1. **web**: Django uygulaması
   - Dockerfile'dan oluşturulur
   - PostgreSQL veritabanına bağlanır
   - Statik ve medya dosyaları için Docker hacimleri kullanır
   - Veritabanı göçlerini ve statik dosya toplama işlemlerini otomatik olarak gerçekleştirir

2. **db**: PostgreSQL veritabanı
   - Resmi PostgreSQL 15 imajını kullanır
   - Veri kalıcılığı için Docker hacmi kullanır

#### Docker Hacimleri

Üç Docker hacmi kullanılır:

1. **postgres_data**: Veritabanı verilerinin kalıcılığını sağlar
2. **static_volume**: Statik dosyaları (CSS, JavaScript, vb.) saklar
3. **media_volume**: Kullanıcı tarafından yüklenen dosyaları (profil resimleri, proje resimleri) saklar

### Özellikler ve Fonksiyonalite

1. **Responsive Tasarım**
   - Bootstrap 5 kullanılarak geliştirilen responsive tasarım
   - Mobil, tablet ve masaüstü cihazlarda düzgün görüntülenir

2. **Admin Paneli**
   - Django'nun otomatik oluşturulan admin paneli
   - CV içeriğini kolayca yönetme imkanı

3. **Animasyonlar**
   - AOS (Animate On Scroll) kütüphanesi ile sayfa animasyonları

4. **Sosyal Medya Entegrasyonu**
   - LinkedIn, GitHub ve kişisel web sitesi bağlantıları

5. **Yazdırılabilir CV**
   - Yazdırma için optimize edilmiş CV sürümü

6. **Proje Portföyü**
   - Projeleri detaylı açıklamalar, resimler ve bağlantılarla sergileme

7. **Beceri Göstergeleri**
   - Becerileri kategorilere ayırma ve yeterlilik seviyelerini görsel olarak gösterme

### Veritabanı Şeması

Veritabanı şeması, `models.py` dosyasında tanımlanan modellere dayanır. PostgreSQL veritabanı kullanılır ve veritabanı bağlantısı `settings.py` dosyasında yapılandırılır.

Django ORM, veritabanı tabloları ile Python nesneleri arasında bir soyutlama katmanı sağlar. Bu sayede, karmaşık SQL sorguları yazmak yerine Python kodu kullanarak veritabanı işlemleri gerçekleştirebilirsiniz.

