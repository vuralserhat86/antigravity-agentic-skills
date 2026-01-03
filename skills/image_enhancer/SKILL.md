---
name: image_enhancer
router_kit: AIKit
description: AI-powered image upscaling, restoration ve enhancement teknikleri.
metadata:
  skillport:
    category: creative
    tags: [ai image enhancement, algorithmic art, artificial intelligence, automation, canvas, color grading, computer vision, deep learning, digital art, enhancement, generative ai, image processing, image restoration, machine learning, neural networks, optimization, photography, post-processing, quality improvement, resolution, restoration, sharpening, upscaling, visualization]      - algorithmic-art
---

# 🖼️ Image Enhancer

> AI tabanlı görüntü iyileştirme, çözünürlük artırma (upscaling) ve restorasyon.

---

## 🚀 Key Techniques

### 1. Super Resolution (SR)
Düşük çözünürlüklü görselleri, detay ekleyerek 2x, 4x veya 8x büyütme.
- **Modeller**: ESRGAN, Real-ESRGAN, SwinIR.

### 2. Denoising & Deblurring
Görseldeki "noise" (kumlanma) ve bulanıklığı giderme.
- **Harc**: Grain removal, sharpening, edge enhancement.

### 3. Face Restoration
Eski veya bozuk fotoğraflardaki yüz detaylarını düzeltme.
- **Modeller**: GFPGAN, CodeFormer.

---

## 🛠️ Tool Palette

| Kategori | Araçlar |
|----------|---------|
| **Python Libs** | OpenCV, PyTorch, Diffusers |
| **CLI Tools** | Upscayl, Real-ESRGAN-ncnn-vulkan |
| **APIs** | Replicate, Hugging Face, Leonardo.ai |

---

## 🎨 Best Practices

- **Original Backup**: Her zaman orijinal görselin yedeğini tut.
- **Artifact Awareness**: Fazla keskinleştirme (over-sharpening) sonucu oluşan yapay detaylara dikkat et.
- **Aspect Ratio**: Büyütme işlemi sırasında en-boy oranını koru.
- **Format**: Çıktı için kayıpsız (PNG, TIFF) veya yüksek kaliteli (WebP) formatları tercih et.

---

*Image Enhancer v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Real-ESRGAN Documentation](https://github.com/xinntao/Real-ESRGAN) & [OpenCV Image Processing](https://docs.opencv.org/4.x/d7/dbd/group__imgproc.html)

### Aşama 1: Assessment
- [ ] **Analysis**: Görseldeki ana sorun ne? (Çözünürlük, Noise, Bulanıklık, Renk solması).
- [ ] **Target**: Çıktı nerede kullanılacak? (Baskı: 300 DPI, Web: 72 DPI).
- [ ] **Type**: Görsel tipi ne? (Fotoğraf, Çizim, Metin). Modeli buna göre seç.

### Aşama 2: Pre-Processing
- [ ] **Clean**: Gerekliyse manuel olarak büyük lekeleri temizle.
- [ ] **Resize**: Modelden en iyi verimi almak için bazen görseli önce 2x büyütmek gerekebilir.

### Aşama 3: Enhancement
- [ ] **Upscale**: `Real-ESRGAN` veya `Repaint` modellerini çalıştır.
- [ ] **Style**: Renk dengesi (White Balance) ve Kontrast ayarlarını AI sonrası manuel optimize et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Görselde "hallucination" (olmayan detaylar) oluştu mu? |
| 2 | Metinler hala okunabilir mi? |
| 3 | Dosya boyutu gereksiz yere devasa mı? |
