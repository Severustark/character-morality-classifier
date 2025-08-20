# 🎭 Character Morality Classifier – Dizi Karakteri Analizi  

Bu proje, bir karakter açıklamasına dayanarak karakterin **İyi / Kötü / Karma** olup olmadığını sınıflandırır.  
Kullanıcı, opsiyonel olarak film/dizi adını da girebilir.  

Projede:  
- 🤗 **Hugging Face Transformers** (`facebook/bart-large-mnli` modeli)  
- 🎨 **Gradio arayüzü**  
kullanılmıştır.  

📄 Ayrıntılı rapor için: [`llm-3.pdf`](./llm-3.pdf)  

---

## 🚀 Özellikler
- Karakter açıklamasını girerek sınıflandırma yapar  
- İyi / Kötü / Karma etiketi ile skorları gösterir  
- Film/dizi adını opsiyonel olarak alır  
- Kullanıcı dostu **Gradio arayüzü** sunar  

---

## ⚙️ Kurulum
Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz:  

```bash
# Depoyu klonla
git clone https://github.com/<kullanici-adi>/character-morality-classifier.git
cd character-morality-classifier

# Bağımlılıkları yükle
pip install -r requirements.txt

```
## ▶️ Çalıştırma
Projeyi çalıştırmak için:

```bash
python main.py
```

## 🖼️ Örnek Kullanım

### 🧑 Karakter Açıklaması ile
**Girdi**  
- Karakter açıklaması: `"Güç için her şeyi yapar, acımasız biridir."`  
- Dizi/Film adı: `Game of Thrones`  

**Çıktı**  
Film/Dizi: Game of Thrones

Karakter Sınıfı: Kötü

Skorlar: {'Kötü': 0.85, 'Karma': 0.10, 'İyi': 0.05}

### 🎭 Karakter İsmi ile
**Girdi**  
- Karakter açıklaması: `"Darth Vader"`  
- Dizi/Film adı:   

**Çıktı**  

Film/Dizi: Star Wars

Karakter Sınıfı: Kötü

Skorlar: {'Kötü': 0.78, 'Karma': 0.18, 'İyi': 0.04}

## 📂 Proje Yapısı
character-morality-classifier/

├── main.py                
├── requirements.txt        
├── llm-3.pdf           
└── README.md                



## 📜 Not

Bu proje, **Kairu Bootcamp Eğitimleri** kapsamında bir ödev/proje olarak geliştirilmiştir.
.
