# ⚡ Emare Code — Hızlı Başlangıç Kılavuzu

> **İlk adımlar:** VSCode extension + Multi-file support (2-3 hafta)

---

## 🎯 En Kritik 3 Eksik

### 1. VSCode Extension 🔴
**Neden:** Hiçbir geliştirici CLI-only tool kullanmak istemiyor  
**Süre:** 2 hafta  
**Başlat:** Hemen

### 2. Multi-File Project 🔴
**Neden:** Gerçek projeler tek dosyalı değil  
**Süre:** 1 hafta  
**Başlat:** Extension ile paralel

### 3. Context Awareness 🔴
**Neden:** Akıllı completion için gerekli  
**Süre:** 1 hafta  
**Başlat:** Diğerleri bittikten sonra

---

## 🚀 Bu Haftanın Hedefi

### Gün 1-2: VSCode Extension Skeleton
```bash
# 1. Extension projesi oluştur
mkdir emarecode-vscode
cd emarecode-vscode
npm init -y
npm install @types/vscode vscode typescript

# 2. package.json düzenle
# 3. extension.js yaz (basic command)
# 4. Test et: F5 (VSCode içinde)
```

### Gün 3-4: API Server
```bash
# 1. FastAPI server oluştur
cd "/Users/emre/Desktop/Emare/emare code"
mkdir -p api
touch api/vscode_server.py

# 2. Endpoint ekle: /complete
# 3. WebSocket ekle: /stream
# 4. Test et: curl http://localhost:8765/complete
```

### Gün 5: Integration
```bash
# 1. Extension → API connection
# 2. Test: /emare generate
# 3. Demo video çek
# 4. GitHub push
```

---

## 📦 Hemen Kurulacak Paketler

```bash
# Backend
pip install fastapi[all] websockets chromadb sentence-transformers

# VSCode Extension (Node.js)
npm install -g yo generator-code
yo code  # VSCode extension scaffold
```

---

## 📖 Okuma Listesi (Sırayla)

1. [VSCode Extension API](https://code.visualstudio.com/api/get-started/your-first-extension) - 30dk
2. [Completion Provider](https://code.visualstudio.com/api/references/vscode-api#CompletionItemProvider) - 20dk
3. [FastAPI WebSocket](https://fastapi.tiangolo.com/advanced/websockets/) - 15dk
4. [ChromaDB Quick Start](https://docs.trychroma.com/getting-started) - 20dk

**Toplam okuma:** ~1.5 saat

---

## 🎬 İlk Demo Senaryosu

1. VSCode aç
2. Python dosyası oluştur
3. `/emare generate user authentication API` yaz
4. ⏎ Enter
5. Boom! 💥 Kod oluştu

**Target:** Bu senaryoyu 2 hafta içinde working demo yap

---

## 💡 Quick Wins (1-2 Gün)

Büyük işlere başlamadan önce bunları yap:

1. **Better CLI Output** (2 saat)
   - Colorful output
   - Progress bars
   - Better error messages

2. **More Templates** (3 saat)
   - TypeScript, Java, C++
   - 10 → 15 dil

3. **Export to ZIP** (2 saat)
   - Proje → .zip
   - One-click download

4. **GitHub Repo Public** (1 saat)
   - README polish
   - Screenshots
   - License (MIT)

---

## 🔥 Referans Projeler (İncelenecek)

### Open Source Copilot Alternatives

1. **TabNine** (closed source but similar)
   - Architecture blog: https://www.tabnine.com/blog

2. **Fauxpilot** (Open source Copilot)
   - GitHub: https://github.com/fauxpilot/fauxpilot
   - **İNCELE:** Model serving architecture

3. **Privy** (Self-hosted Copilot)
   - GitHub: https://github.com/srikanth235/privy
   - **İNCELE:** VSCode extension structure

4. **Codeium** (Free Copilot alternative)
   - Website: https://codeium.com
   - **TEST ET:** Nasıl çalışıyor

---

## 📊 İlerleme Takibi

```
Week 1: [░░░░░░░░░░] 0%  ← Şu an buradasın
Week 2: [██████░░░░] 60%  ← VSCode extension beta
Week 3: [█████████░] 90%  ← Multi-file + tests
Week 4: [██████████] 100% ← v0.1.0 release!
```

---

## 🎯 Başarı Kriterleri (4 Hafta Sonra)

- [ ] VSCode extension published
- [ ] 10+ test users
- [ ] 100+ code generations
- [ ] GitHub stars: 10+
- [ ] Demo video: 1000+ views

---

## 📞 Yardım Lazımsa

1. **Discord:** Emare Community (yakında)
2. **GitHub Issues:** Questions welcome
3. **Email:** emre@emare.dev (yakında)

---

**🚀 BAŞLA! İlk commit'i bugün at.**

```bash
git add .
git commit -m "feat: initial commit - Emare Code v1.0.0"
git push origin main
```
