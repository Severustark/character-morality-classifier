from transformers import pipeline
import gradio as gr

# Zero-shot classification pipeline (İyi/kötü/karma sınıflandırma)
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

labels = ["İyi", "Kötü", "Karma"]
print("Program başladı.")
def karakter_yorumla(karakter_aciklama, dizi_film_adi):
    # Sınıflandırma
    result = classifier(karakter_aciklama, labels)

    # Basit film/dizi adı kontrolü
    if dizi_film_adi.strip():
        film_bilgi = dizi_film_adi.strip()
    else:
        # Film/dizi adı yoksa basit tahmin yap (burayı geliştirebilirsin)
        film_bilgi = "Bilinmiyor"

    # Sonuç metni oluştur
    yorum = f"Film/Dizi: {film_bilgi}\nKarakter Sınıfı: {result['labels'][0]}\nSkorlar: {dict(zip(result['labels'], result['scores']))}"
    return yorum
print("Program başladı.")
# Gradio arayüzü
gr.Interface(
    fn=karakter_yorumla,
    inputs=[
        gr.Textbox(lines=2, placeholder="Karakter açıklamasını yazın..."),
        gr.Textbox(lines=1, placeholder="Film veya dizi adı (opsiyonel)...")
    ],
    outputs="text",
    title="Dizi Karakteri Analizi",
    description="Karakter açıklaması ve film/dizi adı girin. Karakterin iyi/kötü/karma olduğunu analiz edip film bilgisini gösterir."
).launch()
print("Program başladı.")