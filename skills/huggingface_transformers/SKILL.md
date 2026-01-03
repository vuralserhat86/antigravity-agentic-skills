---
name: huggingface_transformers
router_kit: AIKit
description: Hugging Face Transformers library usage, model selection, fine-tuning ve deployment rehberi.
metadata:
  skillport:
    category: ai
    tags: [agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, huggingface transformers, inference, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - prompt-engineering
---

# 🤗 Hugging Face Transformers

> Transformer modellerini (NLP, Vision, Audio) kullanma ve ince ayar (fine-tuning) rehberi.

---

## 🏗️ Core components

### 1. Pipelines (Quick Start)
En basit kullanım yolu. Model ve tokenizer otomatik yüklenir.

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love using Hugging Face!")[0]
print(f"Label: {result['label']}, Score: {result['score']}")
```

### 2. AutoClasses (Manual Control)
Model ve tokenizer'ı manuel seçmek için:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
```

---

## 🎨 Common Tasks

| Görev | Pipeline Adı |
|-------|--------------|
| Text Classification | `text-classification` |
| Text Generation | `text-generation` |
| Summarization | `summarization` |
| Translation | `translation` |
| Object Detection | `object-detection` |

---

## 🔧 Optimization & Deployment

- **Quantization**: 4-bit/8-bit yükleme (BitsAndBytes) ile RAM kullanımı azaltma.
- **ONNX/TensorRT**: Üretim ortamında hızlandırma.
- **PEFT/LoRA**: Çok daha az parametre ile verimli ince ayar (fine-tuning).

---

*Hugging Face Transformers v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Hugging Face Course](https://huggingface.co/course) & [Production Guide](https://huggingface.co/docs/transformers/performance)

### Aşama 1: Model Selection
- [ ] **Task**: Görevine en uygun mimariyi seç (Encoder: classification, Decoder: generation).
- [ ] **License**: Modelin ticari kullanım izni (Apache 2.0 vs Llama Community) var mı?
- [ ] **Size**: Parametre sayısı vs performans dengesini kur (7B genellikle yeterli).

### Aşama 2: Optimization pipeline
- [ ] **Quantization**: Inference için 4-bit / 8-bit quantization (BitsAndBytes) kullan.
- [ ] **Batching**: Tek tek değil, batch halinde process et (GPU verimi).
- [ ] **Format**: Production için ONNX veya TensorRT formatına çevir.

### Aşama 3: Deployment
- [ ] **Cache**: Model ağırlıklarını ve tokenizer'ı docker image içine bake etme, volume kullan.
- [ ] **Token Limits**: Context window sınırını aşan inputlar için strateji belirle (chunking).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Model GPU hafızasına sığıyor mu (OOM hatası)? |
| 2 | Inference süresi (Latency) hedefin altında mı? |
| 3 | Tokenizer ile Model uyumlu mu (aynı vocab)? |
