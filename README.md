# 💻 Emare Code — Cross-Platform Code Generator

> Linux, macOS ve Windows'ta sorunsuz çalışan kod yazma programı

**Versiyon:** 1.0.0  
**Tarih:** 4 Mart 2026  
**Proje:** Emare Ekosistemi

---

## 🎯 Özellikler

- ✅ **Multi-AI Desteği**: Gemini, OpenAI, Azure arasında otomatik failover
- ✅ **Cross-Platform**: Linux, macOS, Windows için kod üretimi
- ✅ **Çoklu Dil**: Python, JavaScript, Go, Rust, PHP, Bash
- ✅ **Doğal Dil**: "create file backup tool" gibi komutlarla proje üret
- ✅ **Template Fallback**: AI yoksa hazır şablonlar
- ✅ **SQLite Veritabanı**: Üretilen projeleri kaydet
- ✅ **CLI & Interactive Mode**: Hem komut satırı hem menü

---

## 🚀 Kurulum

### 1. Repository'yi Klonla

```bash
cd "/Users/emre/Desktop/Emare/emare code"
```

### 2. Python Virtual Environment Oluştur

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# veya
venv\Scripts\activate  # Windows
```

### 3. Bağımlılıkları Yükle

```bash
pip install -r requirements.txt
```

### 4. Environment Variables Ayarla

```bash
cp .env.example .env
# .env dosyasını düzenle ve API anahtarlarını ekle
```

**Minimum:** Sadece `GOOGLE_API_KEY` yeterli (Gemini AI)

---

## 📖 Kullanım

### İnteraktif Mod

```bash
python main.py
```

Komutlar:
- `create` - Yeni proje oluştur (adım adım)
- `smart` - Doğal dil ile proje üret
- `list` - Üretilen projeleri listele
- `help` - Yardım menüsü
- `exit` - Çıkış

### Komut Satırı Mod

```bash
# Yeni proje oluştur
python main.py create

# Doğal dil ile üret
python main.py smart "create rest api for todo app"

# Projeleri listele
python main.py list
```

---

## 💡 Örnek Kullanımlar

### Örnek 1: Python File Backup Tool

```bash
python main.py smart "python file backup tool with compression"
```

**Üretir:**
- `projects/python_file_backup_tool/`
  - `main.py` - Cross-platform Python kodu
  - `manifest.json` - Proje metadata
  - `README.md` - Kullanım kılavuzu

### Örnek 2: JavaScript REST API

```bash
python main.py smart "nodejs rest api for user management"
```

### Örnek 3: Go CLI Tool

```bash
python main.py smart "go cli tool for system monitoring"
```

---

## 🏗️ Mimari

```
emare-code/
├── core/                      # Çekirdek modüller
│   ├── provider_router.py    # Multi-AI router (Gemini/OpenAI/Azure)
│   ├── code_generator.py     # Kod üretim motoru
│   └── smart_factory.py      # Doğal dil işleme
├── data/                      # Veritabanı
│   ├── database.py           # SQLAlchemy modelleri
│   ├── repository.py         # CRUD işlemleri
│   └── emare_code.db         # SQLite database
├── templates/                 # Fallback şablonlar
│   └── __init__.py           # 6 dil için şablon
├── projects/                  # Üretilen projeler (gitignore)
├── main.py                    # Ana CLI
├── requirements.txt           # Python dependencies
├── .env.example              # Environment şablonu
└── README.md                 # Bu dosya
```

---

## 🔧 Teknoloji Stack

| Kategori | Teknoloji |
|----------|-----------|
| **Dil** | Python 3.9+ |
| **AI** | Google Gemini, OpenAI, Azure OpenAI |
| **Database** | SQLite + SQLAlchemy |
| **CLI** | Rich (optional) |
| **Config** | python-dotenv |

---

## 🌍 Desteklenen Diller

1. **Python** - Cross-platform scripts
2. **JavaScript** - Node.js apps
3. **Go** - Compiled binaries
4. **Rust** - Systems programming
5. **PHP** - Web scripts
6. **Bash** - Shell scripts

---

## 🧪 Test

```bash
# Test ortamı oluştur
python -m venv test_env
source test_env/bin/activate
pip install pytest

# Testleri çalıştır (yakında)
pytest
```

---

## 📚 EmareSetup'tan Alınan Özellikler

Bu proje **EmareSetup**'tan şu komponentleri kullanır:

✅ **provider_router.py** - Multi-AI failover sistemi  
✅ **factory_worker.py** → **code_generator.py** - Kod üretim motoru  
✅ **smart_factory.py** - Doğal dil işleme  
✅ **templates/__init__.py** - Template sistemi  
✅ **data/database.py** - SQLAlchemy veritabanı  
✅ **data/repository.py** - CRUD katmanı  

---

## 🔗 Emare Ekosistemi Entegrasyonu

### → EmareSetup
- Modül üretimi aynı AI router'ı paylaşıyor
- Template sistemi uyumlu

### → Emare Hub
- Proje yönetimi için Hub'a entegre edilebilir
- SQLite veritabanı Hub ile senkronize edilebilir

### → EmareCloud
- Üretilen projeleri LXD container'larında deploy et

---

## 🐛 Bilinen Sorunlar

- [ ] Windows'ta path handling testleri eksik
- [ ] Büyük dosyalar için streaming response yok
- [ ] Multi-file proje desteği sınırlı

---

## 📝 TODO

- [ ] Web UI (React + Monaco Editor)
- [ ] GitHub entegrasyonu (direkt push)
- [ ] Docker export
- [ ] Multi-file proje yapısı
- [ ] Package.json / requirements.txt auto-generation
- [ ] CI/CD pipeline şablonları

---

## 📄 Lisans

MIT License - Emare Ekosistemi  
© 2026 Emre

---

## 🤝 Katkıda Bulunma

1. Fork et
2. Feature branch oluştur (`git checkout -b feature/amazing`)
3. Commit yap (`git commit -m 'Add amazing feature'`)
4. Push yap (`git push origin feature/amazing`)
5. Pull Request aç

---

## 📞 İletişim

**Proje:** Emare Code  
**Ekosistem:** Emare (18 proje)  
**Ortak Hafıza:** [EMARE_ORTAK_HAFIZA.md](EMARE_ORTAK_HAFIZA.md)

---

*Linux, macOS ve Windows'ta sorunsuz çalışan kod yazma deneyimi! 🚀*
