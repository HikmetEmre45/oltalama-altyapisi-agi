# Oltalama Altyapısı Ağı (Phishing Infrastructure Network)
**Ders:** Sosyal Ağ Analizi · Dönem Ödevi  
**Öğrenci:** Hikmet Emre Gültekin (2516016024)  
**Öğretim Elemanı:** Öğr. Gör. Osman Can Çetlenbik  


---

### 🌐 Canlı Etkileşimli Ağ Bileşeni
* **Canlı Görselleştirme:** [Etkileşimli Cytoscape.js Ağ Grafiği](https://hikmetemre45.github.io/oltalama-altyapisi-agi/ag_gorsel.html)

---

### 📊 Temel Ağ İstatistikleri ve Metrikler
* **Düğüm Sayısı (Nodes):** 642 (Alan Adı, IP ve Barındırıcı Otonom Sistemler)
* **Kenar Sayısı (Edges):** 788 bağlantı
* **Ağ Yoğunluğu (Density):** 0.0038 (Seyrek, hedefe yönelik kümelenmiş yapı)
* **Bağlı Bileşen Sayısı (Connected Components):** 3 ana izole saldırı kümesi
* **Modülerlik Değeri (Modularity):** 0.6412 (Yüksek kümelenme ve ayrışma)
* **Null Model Doğrulaması:** Rastgele Erdös-Rényi ağına göre Z-Skoru **4.82** (Altyapı paylaşımının bilinçli ve organize olduğunu kanıtlar).

---

### 📂 Depo İçeriği
* `edge_list.csv`: Alan adı, IP ve ASN bağlantılarını içeren zorunlu kenar listesi.
* `oltalama_agi.graphml`: Gephi ve ağ görselleştirme araçları için standart ağ formatı.
* `ag_analiz.py`: Veri işleme ve temel metrik hesaplama betiği.
* `tam_analiz.py`: Louvain topluluk tespiti, merkeziyetler ve Null Model z-skoru motoru.
* `ag_gorsel.html`: Düğüm arama, filtreleme ve detay paneli sunan Cytoscape.js arayüzü.

---

### 🤖 Yapay Zekâ Beyanı
Bu çalışmada veri işleme betiklerinin optimizasyonu ve Cytoscape.js görselleştirme iskeletinin yapılandırılmasında üretken yapay zekâ araçlarından (LLM) yararlanılmıştır. Tüm analiz sonuçları, ağ modelleri ve metrik yorumları bağımsız olarak doğrulanmıştır.
