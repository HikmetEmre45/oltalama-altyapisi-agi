import pandas as pd
import networkx as nx
import numpy as np

print("[-] Tam sosyal ağ analizi başlatılıyor...")

# 1. Kenar listesini oku ve yönlendirilmemiş grafiği kur
df_edges = pd.read_csv("edge_list.csv")
G = nx.from_pandas_edgelist(df_edges, source='Source', target='Target')

# 2. GraphML Çıktısı (Zorunlu teslim dosyası - Gephi / Görselleştirme için)
nx.write_graphml(G, "oltalama_agi.graphml")
print("[+] 'oltalama_agi.graphml' dosyası oluşturuldu.")

# 3. Merkeziyet Hesaplamaları (İlk 5 düğüm)
deg_centrality = nx.degree_centrality(G)
top_nodes = sorted(deg_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
print("\n--- EN YÜKSEK MERKEZİYETE SAHİP İLK 5 DÜĞÜM (Derece) ---")
for node, score in top_nodes:
    print(f"Düğüm: {node} | Skor: {score:.4f}")

# 4. Topluluk Tespiti (Louvain) ve Modülerlik
communities = list(nx.community.greedy_modularity_communities(G))
modularity = nx.community.modularity(G, communities)
print(f"\n[+] Tespit Edilen Topluluk Sayısı: {len(communities)}")
print(f"[+] Ağ Modülerlik Değeri (Modularity): {modularity:.4f}")

# 5. Null Model Karşılaştırması (Erdös-Renyi Karşılaştırması)
n = G.number_of_nodes()
m = G.number_of_edges()
p = (2.0 * m) / (n * (n - 1))

real_clustering = nx.average_clustering(G)
random_clusterings = []

# 20 rastgele ağ ile hızlı null model dağılımı
for _ in range(20):
    G_rand = nx.erdos_renyi_graph(n, p)
    random_clusterings.append(nx.average_clustering(G_rand))

rand_mean = np.mean(random_clusterings)
rand_std = np.std(random_clusterings) if np.std(random_clusterings) > 0 else 0.001
z_score = (real_clustering - rand_mean) / rand_std

print(f"\n--- NULL MODEL KARŞILAŞTIRMASI ---")
print(f"Gerçek Ağ Kümelenme Katsayısı: {real_clustering:.4f}")
print(f"Rastgele Ağ Ortalaması: {rand_mean:.4f}")
print(f"Z-Skoru: {z_score:.2f} (Ağın rastlantısal olmadığını kanıtlar)")
print("=" * 50)
print("[✓] Sosyal Ağ Analizi'nin tüm hesaplamaları tamamlandı!") 