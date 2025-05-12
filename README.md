# Django CV Web Uygulaması

Bu proje, Docker ile çalışan basit bir Django CV (özgeçmiş) web uygulamasıdır. Siyah bir tema kullanarak profesyonel bir özgeçmiş sitesi oluşturmak için tasarlanmıştır.

## Proje Hakkında

Bu uygulama, kullanıcıların özgeçmiş bilgilerini (kişisel bilgiler, eğitim, iş deneyimi ve yetenekler) yönetebilmesi ve bunları şık bir siyah tema ile görüntüleyebilmesi için tasarlanmıştır.

## Teknolojiler

- Python 3.11
- Django 4.2
- Docker
- SQLite (Geliştirme için)
- HTML/CSS

## Kurulum

### Ön Gereksinimler

- [Docker](https://www.docker.com/products/docker-desktop) yüklü olmalıdır
- [Docker Compose](https://docs.docker.com/compose/install/) yüklü olmalıdır

### Adımlar

1. Bu repository'yi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/kullanici/django-cv-projesi.git
cd django-cv-projesi
```

2. Docker ile uygulamayı başlatın:

```bash
docker-compose up --build
```

3. Tarayıcınızda [http://localhost:8000](http://localhost:8000) adresine giderek uygulamayı görüntüleyin.

## Veritabanı Kurulumu

İlk kez çalıştırıldığında, aşağıdaki komutları bir başka terminal penceresi açarak çalıştırmanız gerekiyor:

```bash
# Docker container'ı çalışırken başka bir terminal açın
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

`createsuperuser` komutu size kullanıcı adı, e-posta ve şifre sorarak bir admin kullanıcısı oluşturmanızı sağlar.

## Admin Paneline Erişim

1. Web tarayıcınızda [http://localhost:8000/admin](http://localhost:8000/admin) adresine gidin
2. Oluşturduğunuz süper kullanıcı bilgileriyle giriş yapın
3. Admin panelinden CV içeriğinizi yönetin:
   - Kişisel Bilgiler: Ad, başlık, özet, iletişim bilgileri
   - Eğitim: Okullar, dereceler, tarihler
   - İş Deneyimi: Şirketler, pozisyonlar, tarihler, açıklamalar
   - Yetenekler: Beceriler ve uzmanlık seviyeleri

## CV Sitenizi Özelleştirme

CV içeriğiniz admin panelinden eklendikten sonra, [http://localhost:8000](http://localhost:8000) adresinde otomatik olarak görüntülenecektir.

### İpuçları:

- Kişisel bilgilerinizi ekleyin (sadece bir tane oluşturun)
- Eğitim geçmişinizi ekleyin (birden fazla ekleyebilirsiniz)
- İş deneyimlerinizi ekleyin
- Yeteneklerinizi kategorilere ayırarak ekleyin (örn: Programlama Dilleri, Yazılım, Diller)

## Proje Yapısı

```
django-cv-projesi/
│
├── cv_project/             # Ana Django projesi
│   ├── __init__.py
│   ├── settings.py         # Proje ayarları
│   ├── urls.py             # Ana URL konfigürasyonu
│   ├── asgi.py
│   └── wsgi.py
│
├── cv_app/                 # CV uygulaması
│   ├── __init__.py
│   ├── admin.py            # Admin panel konfigürasyonu
│   ├── apps.py
│   ├── models.py           # Veri modelleri
│   ├── views.py            # Görünüm fonksiyonları
│   ├── urls.py             # URL yönlendirmeleri
│   └── templates/          # HTML şablonları
│       └── cv_app/
│           ├── base.html   # Ana şablon (siyah tema)
│           └── home.html   # CV ana sayfası
│
├── manage.py               # Django yönetim betiği
├── requirements.txt        # Python bağımlılıkları
├── Dockerfile              # Docker yapılandırması
├── docker-compose.yml      # Docker Compose yapılandırması
└── README.md               # Bu dosya
```

## Geliştirme

- Docker container'ı çalışırken yapılan değişiklikler otomatik olarak yenilenir
- Yeni modeller eklediğinizde veya mevcut modelleri değiştirdiğinizde, aşağıdaki komutları çalıştırmanız gerekir:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

## Daha Fazla Özellik Eklemek İçin Fikirler

- Sosyal medya bağlantıları ekleyin
- Projeler bölümü ekleyin
- CV'nizi PDF olarak indirme özelliği ekleyin
- Farklı temalar veya tema seçenekleri ekleyin


python manage.py runserver
admin
adminpassword123
---

Bu proje [Django](https://www.djangoproject.com/) kullanılarak oluşturulmuştur.