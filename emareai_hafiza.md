# 🤖 Emare AI — Custom Yapay Zeka Motoru

> 🔗 **Ortak Hafıza:** [`EMARE_ORTAK_HAFIZA.md`](/Users/emre/Desktop/Emare/EMARE_ORTAK_HAFIZA.md) — Tüm Emare ekosistemi, sunucu bilgileri, standartlar ve proje envanteri için bak.

## 📋 Proje Kimliği

- **Proje Adı:** Emare AI
- **Kategori:** Core Engine / AI Platform
- **Durum:** 🔵 Development (Araştırma & Planlama)
- **Kod Deposu:** `/Users/emre/Desktop/Emare/emareai`
- **İkon:** 🤖
- **Renk Kodu:** `#8b5cf6`

## 🎯 Amaç ve Vizyon

**Kendi yapay zeka motorumuzu yazacağız!**

Emare ekosistemi için özelleştirilmiş, kendi altyapınızda çalışan, privacy-first AI motoru.

### Neden Kendi AI'mız?

1. **🔐 Privacy:** Tüm data kendi sunucularımızda (KVKK/GDPR uyumlu)
2. **💰 Maliyet:** GPT-4o/Gemini API maliyetini azalt (özellikle yüksek volume'da)
3. **🎛️ Control:** Model fine-tuning, özel domain knowledge
4. **⚡ Latency:** Local inference daha hızlı
5. **🌐 Offline:** İnternet bağlantısı olmadan da çalışabilir

## 🏗️ Teknoloji Stack

### AI Framework & Model
- **PyTorch** veya **TensorFlow** (deep learning framework)
- **Hugging Face Transformers** (model hub)
- **Ollama** (local LLM serving) veya **vLLM** (high-performance inference)
- **LangChain** veya **LlamaIndex** (RAG, chain orchestration)

### Model Seçenekleri

#### Option 1: Open Source LLM (Fine-tune)
- **LLaMA 3.1** (8B, 70B, 405B variants) - Meta
- **Mistral 7B / Mixtral 8x7B** - Mistral AI
- **Qwen 2.5** - Alibaba (Türkçe desteği iyi)
- **Gemma 2** - Google (9B, 27B)

#### Option 2: Small Language Model (From Scratch)
- **Transformer architecture** (GPT-like)
- **Training data:** Turkish + English corpus
- **Model size:** 1B-7B parameters (feasible to train)
- **Training:** 4-8x A100 GPU, 2-4 weeks

#### Option 3: Hybrid (Best of Both Worlds)
- Büyük model (LLaMA 70B) → reasoning, complex tasks
- Küçük model (custom 3B) → simple queries, fast response
- Router model → hangi modele yönlendireceğini karar verir

### Infrastructure
```
emareai/
├── models/                  # Model weights
│   ├── llama-3.1-8b/
│   ├── mistral-7b/
│   └── emare-custom-3b/
├── data/                    # Training/fine-tuning data
│   ├── raw/
│   ├── processed/
│   └── embeddings/
├── training/
│   ├── train.py             # Training script
│   ├── finetune.py          # Fine-tuning script
│   └── config.yaml
├── inference/
│   ├── server.py            # FastAPI inference server
│   ├── ollama_wrapper.py    # Ollama integration
│   └── vllm_wrapper.py      # vLLM integration
├── evaluation/
│   ├── benchmarks/
│   └── test_cases/
└── api/
    ├── main.py              # API endpoint
    ├── models.py
    └── prompts/
```

## 🚀 API Design

### Endpoint Structure
```python
# FastAPI server
POST /v1/chat/completions      # OpenAI-compatible endpoint
POST /v1/embeddings            # Text embeddings
POST /v1/completions           # Text completion
GET  /v1/models                # List available models

# Emare-specific
POST /v1/emare/analyze         # Domain-specific analysis
POST /v1/emare/summarize       # Summarization
POST /v1/emare/translate       # TR ↔ EN translation
```

### Example Request
```bash
curl -X POST http://127.0.0.1:8888/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer emare_ai_key" \
  -d '{
    "model": "emare-custom-3b",
    "messages": [
      {"role": "user", "content": "Merhaba, nasılsın?"}
    ],
    "temperature": 0.7,
    "max_tokens": 150
  }'
```

## 🔌 Diğer Projelerle Entegrasyon

### → Emare Asistan
- WhatsApp cevapları Emare AI ile üretilsin (Gemini yerine)
- Maliyet: $0.50/1M token → $0.00/1M token (self-hosted)

### → Emare Finance
- Fatura açıklamaları, özet raporlar (AI generated)
- Müşteri soruları (chatbot)

### → Emare POS
- Menü önerileri (AI-based)
- Sipariş analizi ve tahminleme

### → SiberEmare
- Pentest raporlarını Emare AI ile üret
- Vulnerability analysis

### → Emare Makale
- İçerik üretimi (GPT-4o yerine Emare AI)
- Türkçe kalitesi daha iyi olabilir (fine-tuned model)

### → Emare Ads (emareads)
- Sayfa içeriği analizi (AI-powered)
- Akıllı öneriler

## 📊 Model Training Pipeline

### 1. Data Collection
```python
# Türkçe corpus
- Turkish Wikipedia dump
- OSCAR (Open Super-large Crawled Aggregated corpus)
- Turkish news articles (scraping)
- Emare internal data (anonymized)
```

### 2. Preprocessing
```python
# Tokenization
- SentencePiece tokenizer (BPE)
- Vocab size: 50K-100K tokens
- Special tokens: <BOS>, <EOS>, <PAD>, <UNK>
```

### 3. Training
```python
# Hyperparameters (örnek)
model_size = "3B"  # 3 billion parameters
batch_size = 32
learning_rate = 1e-4
num_epochs = 3-5
sequence_length = 2048
optimizer = "AdamW"
lr_scheduler = "cosine"
```

### 4. Fine-tuning
```python
# Domain-specific fine-tuning
- Customer support conversations (Emare Asistan data)
- Finance documents (Emare Finance)
- Technical docs (code, API references)
```

### 5. Evaluation
```python
# Metrics
- Perplexity
- BLEU score (translation)
- ROUGE score (summarization)
- Human evaluation (A/B testing)
```

## 💰 Maliyet Analizi

### GPU Training Cost
- **Cloud (AWS p4d.24xlarge):** $32/hour (8x A100 GPU)
- **Training time:** 2-4 weeks → ~$20K-$40K
- **Alternative:** Spot instances (70% cheaper) → $6K-$12K

### Inference Cost
- **Self-hosted (dedicated server):** $500-$2000/month (1x A100, 1x H100)
- **Break-even:** ~10M requests/month (GPT-4o comparison)

### ROI (Return on Investment)
```
Emare Asistan current cost: $500/month (Gemini API)
Emare AI cost: $100/month (1x RTX 4090, smaller model)
Savings: $400/month = $4.8K/year

Training cost: $10K (one-time)
Break-even: 25 months (2+ years)
```

## 🔐 Güvenlik ve Privacy

- **Data encryption:** At rest (LUKS) ve in transit (TLS 1.3)
- **Model access control:** JWT authentication
- **Rate limiting:** 100 req/min per user
- **Audit logging:** Tüm API çağrıları loglanır
- **No data retention:** User queries 24 saat sonra silinir (KVKK uyumlu)

## 🎯 Roadmap

### Phase 1: Research (Q1 2026 - Mart-Nisan)
- [x] Proje planlama (DONE - bu dosya)
- [ ] Model seçimi (LLaMA vs Mistral vs Qwen)
- [ ] Infrastructure setup (GPU sunucu kiralamak)
- [ ] Baseline benchmark (GPT-4o, Gemini, Claude karşılaştırması)

### Phase 2: Fine-tuning (Q2 2026 - Mayıs-Haziran)
- [ ] Data collection (Turkish corpus)
- [ ] Fine-tune LLaMA 3.1-8B (Emare domain)
- [ ] API server (FastAPI + vLLM)
- [ ] Internal testing (Emare Asistan'a entegre)

### Phase 3: Custom Training (Q3 2026 - Temmuz-Ağustos-Eylül)
- [ ] Decision: sıfırdan model train edelim mi?
- [ ] Training pipeline (PyTorch Lightning)
- [ ] Custom model training (3B parameters)
- [ ] Evaluation ve comparison

### Phase 4: Production (Q4 2026 - Ekim-Kasım-Aralık)
- [ ] Multi-model serving (küçük + büyük model)
- [ ] Auto-scaling (Kubernetes + GPU nodes)
- [ ] Monitoring (Prometheus + Grafana)
- [ ] Cost optimization

## 📚 Kaynaklar

### Model Training
- **Hugging Face Course:** https://huggingface.co/course
- **LLaMA 3.1:** https://ai.meta.com/llama/
- **Mistral 7B:** https://mistral.ai/
- **Qwen 2.5:** https://qwenlm.github.io/

### Inference Serving
- **Ollama:** https://ollama.ai/
- **vLLM:** https://github.com/vllm-project/vllm
- **TGI (Text Generation Inference):** https://github.com/huggingface/text-generation-inference

### Fine-tuning
- **LoRA (Low-Rank Adaptation):** https://arxiv.org/abs/2106.09685
- **QLoRA (Quantized LoRA):** https://arxiv.org/abs/2305.14314
- **PEFT (Parameter-Efficient Fine-Tuning):** https://github.com/huggingface/peft

## 🔄 Son Güncelleme

**Tarih:** 4 Mart 2026  
**Durum:** Araştırma & planlama aşaması  
**Next Action:** Model seçimi, GPU sunucu araştırması, baseline benchmark

---

**Vizyon:** Emare ekosistemi için tam bağımsız, kendi AI altyapımız. GPT-4o/Gemini'ye bağımlılıktan kurtulmak ve privacy-first, cost-effective, özelleştirilmiş AI çözümü.

**Hedef:** 2027'de tüm Emare projeleri kendi AI'mızı kullansın! 🚀
