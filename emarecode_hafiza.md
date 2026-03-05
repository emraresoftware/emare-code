# 💻 Emare Code — Proje Hafıza Dosyası

> 🔗 **Ortak Hafıza:** [`EMARE_ORTAK_HAFIZA.md`](EMARE_ORTAK_HAFIZA.md) — Tüm Emare ekosistemi, sunucu bilgileri, standartlar ve proje envanteri için bak.

---

## 🧪 Son Test Özeti (4 Mart 2026)

| Özellik | Durum | Detay |
|---------|-------|-------|
| **Template Sistemi** | ✅ Başarılı | 360 byte Python kod üretildi |
| **Proje Oluşturma** | ✅ Başarılı | `projects/demo_app/` çalıştı |
| **AI Router** | ✅ Aktif | Google Gemini bağlantısı OK |
| **Platform Detection** | ✅ Çalışıyor | macOS 14.x algılandı |
| **AI Performance** | ⚠️ Yavaş | 30+ saniye (timeout gerekli) |
| **Python Version** | ⚠️ Uyarı | 3.9 EOL (3.11+ upgrade önerilir) |
| **SSL Library** | ⚠️ Uyarı | LibreSSL 2.8.3 (fonksiyonel) |

**Sonuç:** Sistem fonksiyonel ✅ | Optimizasyon gerekli ⚠️

---

## 📋 Proje Kimliği

- **Proje Adı:** Emare Code
- **Kategori:** Infrastructure / Code Generation Tool
- **Durum:** 🟢 Development (v1.0.0)
- **Test Durumu:** ✅ macOS Tested | ⚠️ AI Timeout Issue | 🟡 Windows Pending
- **Kod Deposu:** `/Users/emre/Desktop/Emare/emare code`
- **İkon:** 💻
- **Renk Kodu:** `#00d9ff`

## 🎯 Amaç ve Vizyon

**Cross-platform kod yazma programı**

Linux, macOS ve Windows'ta sorunsuz çalışan kod üretimi. AI destekli, doğal dil ile proje oluşturma.

### Neden Emare Code?

1. **🌍 Cross-Platform:** Tek komutla 3 işletim sisteminde çalışan kod
2. **🤖 AI Destekli:** Gemini, OpenAI, Azure otomatik failover
3. **💡 Doğal Dil:** "create file backup tool" → tam proje
4. **🎨 Çoklu Dil:** Python, JS, Go, Rust, PHP, Bash
5. **🔌 EmareSetup Tabanlı:** Kanıtlanmış mimari

## 🏗️ Teknoloji Stack

### Backend
- **Python 3.9+** - Ana dil
- **SQLAlchemy** - ORM + SQLite
- **python-dotenv** - Environment yönetimi
- **Pydantic** - Type validation

### AI Providers
- **Google Gemini** (birincil) - gemini-2.0-flash
- **OpenAI** (yedek) - gpt-4o-mini
- **Azure OpenAI** (opsiyonel) - gpt-4o

### CLI
- **Rich** (opsiyonel) - Güzel terminal UI
- **argparse** - Komut satırı parsing

## 📂 Dosya Yapısı

```
emare-code/
├── core/                          # Çekirdek modüller
│   ├── __init__.py
│   ├── provider_router.py         # Multi-AI router (211 satır)
│   ├── code_generator.py          # Kod üretim motoru (150+ satır)
│   └── smart_factory.py           # Doğal dil işleme (100+ satır)
├── data/                          # Veritabanı katmanı
│   ├── __init__.py
│   ├── database.py                # SQLAlchemy modelleri
│   ├── repository.py              # CRUD işlemleri
│   └── emare_code.db              # SQLite (auto-generated)
├── templates/                     # Fallback şablonları
│   └── __init__.py                # 6 dil şablonu
├── projects/                      # Üretilen projeler (gitignore)
│   └── demo_app/                  # Test projesi (360 bytes)
│       └── main.py
├── test_simple.py                 # Template test ✅
├── test_full.py                   # Full generation test ⚠️
├── test_quick.py                  # Quick test
├── main.py                        # Ana CLI (200+ satır)
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
├── .gitignore
├── README.md
├── EMARE_ORTAK_HAFIZA.md         # Ekosistem hafızası
├── EMARE_AI_COLLECTIVE.md        # 18 AI perspektifi
├── emareai_hafiza.md             # Emare AI projesi
└── emarecode_hafiza.md           # ← ← ← BU DOSYA
```

**Toplam kod:** ~800 satır

## 🚀 Kurulum ve Kullanım

### 1. Virtual Environment

```bash
cd "/Users/emre/Desktop/Emare/emare code"
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

### 2. Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment

```bash
cp .env.example .env
# .env'de GOOGLE_API_KEY ayarla
```

### 4. Çalıştır

```bash
# İnteraktif mod
python main.py

# Komut satırı
python main.py create
python main.py smart "create rest api"
python main.py list
```

## 📖 Komutlar

| Komut | Açıklama |
|-------|----------|
| `create` | Yeni proje oluştur (interaktif) |
| `smart "text"` | Doğal dil ile proje üret |
| `list` | Üretilen projeleri listele |
| `help` | Yardım menüsü |
| `exit` | Çıkış |

## 💡 Örnek Kullanımlar

### Örnek 1: Python Backup Tool

```bash
python main.py smart "python file backup with compression"
```

**Üretir:**
```
projects/python_file_backup_with_compression/
├── main.py          # Cross-platform Python kod
├── manifest.json    # Metadata
└── README.md        # Kullanım kılavuzu
```

### Örnek 2: JavaScript REST API

```bash
python main.py smart "nodejs express api for todo management"
```

### Örnek 3: Go CLI Tool

```bash
python main.py smart "go command line tool for system monitoring"
```

## 🔌 EmareSetup'tan Devraldığı Özellikler

| Dosya | Kaynak | Adaptasyon |
|-------|--------|------------|
| `provider_router.py` | EmareSetup | ✅ Birebir kopyalandı |
| `code_generator.py` | `factory_worker.py` | 🔧 Projeler için adapt edildi |
| `smart_factory.py` | EmareSetup | 🔧 Proje üretimi için güncellendi |
| `templates/__init__.py` | EmareSetup | 🔧 6 dil için yeniden yazıldı |
| `database.py` | EmareSetup | 🔧 Project modeli eklendi |
| `repository.py` | EmareSetup | 🔧 Project CRUD eklendi |

## 🎨 Desteklenen Diller

1. **Python** - pathlib, platform.system()
2. **JavaScript** - os module, cross-platform
3. **Go** - runtime.GOOS detection
4. **Rust** - std::env::consts::OS
5. **PHP** - PHP_OS constant
6. **Bash** - uname -s detection

## 🌍 Platform Desteği

| Platform | Test Durumu | Notlar |
|----------|-------------|--------|
| **Linux** | ✅ Destekleniyor | POSIX komutlar |
| **macOS** | ✅ Test Edildi | Python 3.9, demo_app çalıştı |
| **Windows** | 🟡 Test edilmedi | pathlib kullanımı |

## 🔄 EmareSetup Karşılaştırması

| Özellik | EmareSetup | Emare Code |
|---------|------------|------------|
| **Amaç** | Python modül üretimi | Cross-platform kod üretimi |
| **Diller** | Python only | 6 dil (Python, JS, Go, Rust, PHP, Bash) |
| **Platform** | macOS/Linux | Linux/macOS/Windows |
| **Template** | 5 tip | 6 dil |
| **Web UI** | React 19 + FastAPI | Yok (TODO) |
| **Database** | SQLite (Module tablosu) | SQLite (Project tablosu) |
| **Test** | pytest + AI üretimi | Yok (TODO) |

## 🛣️ Roadmap

### Faz 1: Core (✅ Tamamlandı - 4 Mart 2026)
- [x] Multi-AI router (Gemini/OpenAI/Azure)
- [x] Code generator engine
- [x] Smart factory (doğal dil)
- [x] 6 dil şablonu
- [x] SQLite database
- [x] CLI interface
- [x] **macOS testleri** (Template ✅, Proje oluşturma ✅, AI Router ✅)

### Faz 1.5: Stabilizasyon (⏳ Devam Ediyor)
- [ ] AI timeout mekanizması (30s limit)
- [ ] Python 3.11+ upgrade
- [ ] Error handling iyileştirmeleri
- [ ] Logging system
- [ ] Windows testleri

### Faz 2: Enhancement (Q1 2026)
- [ ] Web UI (React + Monaco Editor)
- [ ] Multi-file proje desteği
- [ ] Package manager integration (pip, npm, go mod)
- [ ] README auto-generation improvement
- [ ] Dockerfile for projects

### Faz 3: Export & Deploy (Q2 2026)
- [ ] GitHub push integration
- [ ] ZIP export
- [ ] EmareCloud deploy (LXD container)
- [ ] CI/CD template generation

### Faz 4: Advanced (Q3 2026)
- [ ] Code refactoring AI
- [ ] Dependency analyzer
- [ ] Security scanner
- [ ] Performance profiler

## 🔗 Diğer Projelerle Entegrasyon

### → EmareSetup
- Aynı AI router'ı paylaşıyor
- Template sistemi uyumlu
- Database structure benzer

### → Emare Hub
- Proje listesi Hub'a entegre edilebilir
- SQLite senkronizasyonu
- Merkezi yönetim

### → EmareCloud
- Üretilen projeleri LXD container'da deploy
- Otomatik environment kurulumu
- Remote execution

### → Emare AI
- Kendi AI motorumuz hazır olunca geçiş
- Maliyet sıfır (self-hosted)
- Privacy-first

## 📊 İstatistikler

**Oluşturma Tarihi:** 4 Mart 2026  
**Versiyon:** 1.0.0  
**Satır Sayısı:** ~800 satır  
**Dosya Sayısı:** 13 dosya (+ 3 test dosyası)  
**Test Coverage:** %0 (TODO)

### Test Sonuçları (4 Mart 2026)
- ✅ Template sistemi: 360 byte Python kod üretildi
- ✅ Proje oluşturma: `projects/demo_app/` başarıyla oluşturuldu
- ✅ AI Router: 1 provider (Google Gemini) aktif
- ✅ Platform detection: macOS 14.x doğru algılandı
- ⚠️ AI performans: 30+ saniye (timeout gerekli)
- ⚠️ Python 3.9 EOL: FutureWarning (fonksiyonel)
- ⚠️ LibreSSL 2.8.3: urllib3 uyarısı (fonksiyonel)

## 🐛 Bilinen Sorunlar

### Kritik
1. **AI Timeout:** Google Gemini çağrıları 30+ saniye sürebiliyor (timeout mekanizması gerekli)
2. **Python 3.9 EOL:** FutureWarning from google-auth (Python 3.11+ upgrade önerilir)
3. **LibreSSL Uyarısı:** urllib3 v2 OpenSSL 1.1.1+ bekliyor, macOS LibreSSL 2.8.3 kullanıyor

### Normal
4. **Windows Path Handling:** Test edilmedi
5. **Large File Generation:** Streaming response yok
6. **Multi-file Projects:** Sınırlı destek
7. **Error Recovery:** AI başarısız olursa sadece template

## 🧪 Test Senaryoları

### Senaryo 1: Template Sistemi ✅
```bash
python test_simple.py
# Sonuç: 344 karakter Python kod, başarılı
```

### Senaryo 2: Proje Oluşturma ✅
```bash
python -c "from templates import get_template; ..."
# Sonuç: projects/demo_app/ oluşturuldu, çalıştırıldı
```

### Senaryo 3: AI Router ✅
```bash
python -c "from core.provider_router import router; ..."
# Sonuç: 1 provider available (Google Gemini)
```

### Senaryo 4: Full Generation ⚠️
```bash
python test_full.py
# Sonuç: AI timeout (30+ saniye), fallback başarılı
```

### Test Edilmesi Gerekenler
```bash
# JavaScript API
python main.py smart "nodejs rest api"

# Go CLI
python main.py smart "go cli tool"

# Cross-platform script
python main.py smart "cross-platform disk usage analyzer"
```

## 📚 Kod Örnekleri

### Provider Router Kullanımı

```python
from core.provider_router import router

result = router.generate("Write a Python hello world")
if result.success:
    print(result.text)
    print(f"Provider: {result.provider}")
```

### Code Generator Kullanımı

```python
from core.code_generator import generator

project_path = generator.create_project(
    name="my_tool",
    language="python",
    description="File backup tool",
    platform="all"
)
print(f"Proje oluşturuldu: {project_path}")
```

### Smart Factory Kullanımı

```python
from core.smart_factory import smart_factory

results = smart_factory.build_from_request(
    "create rest api for user management"
)
for r in results:
    print(f"{r['name']}: {r['status']}")
```

## 🔐 Güvenlik

- **API Keys:** `.env` dosyasında, git'e commit edilmez
- **Database:** SQLite (local only, network exposure yok)
- **Generated Code:** Sandbox environment önerilir
- **AI Output:** Her zaman review et

## 💰 Maliyet

### API Kullanımı (Gemini)
- **Free Tier:** 15 req/min, 1500 req/day
- **Paid Tier:** $0.50/1M token (input), $1.50/1M token (output)

### Ortalama Kullanım
- **Tek proje:** ~2000 token (input) + ~1000 token (output)
- **Maliyet:** ~$0.0025 per project
- **100 proje:** ~$0.25

**Sonuç:** Çok ucuz! 🎉

## 📝 Changelog

### v1.0.0 (4 Mart 2026)
- ✅ İlk release
- ✅ Multi-AI provider router
- ✅ 6 dil desteği (Python, JS, Go, Rust, PHP, Bash)
- ✅ Cross-platform kod üretimi
- ✅ Doğal dil işleme
- ✅ SQLite database
- ✅ CLI interface (interactive + command mode)
- ✅ EmareSetup'tan core components ported
- ✅ **macOS testleri tamamlandı** (4 Mart 2026)
  - Template sistemi: 360 byte kod üretimi ✅
  - Proje oluşturma: demo_app başarılı ✅
  - AI Router: Gemini bağlantısı çalışıyor ✅
  - Platform detection: macOS 14.x algılama ✅
- ⚠️ **Bilinen limitasyonlar:**
  - AI response süreleri uzun (30+ saniye)
  - Python 3.9 EOL uyarıları (fonksiyonel)
  - LibreSSL compatibility uyarıları (fonksiyonel)

## 🤝 İlham Kaynakları

1. **EmareSetup** - Core architecture
2. **GitHub Copilot** - AI-powered coding
3. **Cursor** - AI code editor
4. **Replit** - Online code generation
5. **v0.dev** - Natural language to UI

## 📞 İletişim & Destek

**Proje:** Emare Code  
**Ekosistem:** Emare (18 proje)  
**GitHub:** (yakında)  
**Discord:** (yakında)

## 🎯 Vizyon

> "Her geliştirici, her platformda, doğal dilde kod yazabilmeli."

Emare Code, kod yazmanın AI ile nasıl demokratikleşebileceğini gösteriyor. Linux, macOS, Windows ayrımı yok. Sadece fikir → kod → çalıştır.

---

**Son Güncelleme:** 4 Mart 2026 (Test tamamlandı)  
**Durum:** 🟢 Development (v1.0.0 - macOS tested)  
**Test Durumu:**
  - ✅ Template system
  - ✅ Project creation
  - ✅ AI Router (Gemini)
  - ⚠️ AI performance (timeout needed)
  
**Next Actions:**
  1. AI timeout mekanizması ekle (öncelik: yüksek)
  2. Python 3.11+ upgrade (öncelik: orta)
  3. Web UI başlat (öncelik: orta)
  4. Windows testleri (öncelik: düşük)

---

*Cross-platform kod üretimi artık bir komut uzağınızda! 💻🚀*
