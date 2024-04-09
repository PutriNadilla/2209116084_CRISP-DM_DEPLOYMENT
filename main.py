import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.title('Video Game Sales Analysis')

url = 'Data_Cleaning.csv'
df = pd.read_csv(url)

st.subheader("Dataset")
st.write(df.head())

df['Total_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales']
total_sales = df['Total_Sales'].sum()
sales_by_region = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
sales_percentages = (sales_by_region / total_sales) * 100

# Create a single bar plot to compare sales across regions
st.subheader('Penjualan Berdasarkan Lokasi')
plt.figure(figsize=(10, 6))

sales_by_region.plot(kind='bar')
plt.title('Penjualan Berdasarkan Lokasi')
plt.xlabel('Lokasi')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)  # Show plot

st.write('Presentase Penjualan Berdasarkan lokasi')
st.write("- NA Sales: {:.2f}%".format(sales_percentages['NA_Sales']))
st.write("- EU Sales: {:.2f}%".format(sales_percentages['EU_Sales']))
st.write("- JP Sales: {:.2f}%".format(sales_percentages['JP_Sales']))
st.write("- Other Sales: {:.2f}%".format(sales_percentages['Other_Sales']))

st.write("Penjualan di wilayah NA (North America) memiliki kontribusi terbesar, mencapai 46.07%. Ini menunjukkan pentingnya fokus pemasaran dan penjualan di Amerika Utara untuk mencapai target penjualan.")
st.write("Penjualan di wilayah EU (Europe) menyumbang sekitar 26.28%, menunjukkan potensi yang signifikan untuk meningkatkan kehadiran pasar di Eropa dengan strategi pemasaran yang tepat.")
st.write('Penjualan di wilayah JP (Jepang) mencapai 21.38%, menunjukkan pentingnya memperhatikan preferensi dan tren lokal serta bermitra dengan penerbit lokal untuk meningkatkan penjualan di pasar Jepang.')
st.write('Penjualan di wilayah lain (Other Sales) memiliki kontribusi sekitar 6.27%. Meskipun lebih kecil, tetap penting untuk mengeksplorasi peluang di wilayah-wilayah ini, seperti pasar Asia Pasifik, untuk meningkatkan distribusi produk secara global.')
 
    # Bar plot of Sales by Genre
genre_cols = ['Genre_Action', 'Genre_Adventure', 'Genre_Fighting', 'Genre_Misc', 'Genre_Platform',
              'Genre_Puzzle', 'Genre_Racing', 'Genre_Role-Playing', 'Genre_Shooter', 'Genre_Simulation',
              'Genre_Sports', 'Genre_Strategy']
sales_by_genre = df[genre_cols].sum()

# Create bar plot of total sales by genre
st.subheader('Penjualan Berdasarkan Genre Game')
plt.figure(figsize=(12, 6))
sales_by_genre.plot(kind='bar')
plt.title('Penjualan Berdasarkan Genre Game')
plt.xlabel('Genre')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.tight_layout()
genre_plot = plt.gcf()
st.pyplot(genre_plot)  # Show plot

# Calculate and display sales percentages by genre
st.write("Presentase Penjualan Berdasarkan Genre:")
total_sales = sales_by_genre.sum()
for genre in genre_cols:
    percentage = (sales_by_genre[genre] / total_sales) * 100
    st.write(f"- {genre}: {percentage:.2f}%")

st.write('Genre Misc (Miscellaneous) memiliki kontribusi tertinggi dengan 15.83%, menunjukkan bahwa game dengan genre yang beragam dan sulit untuk dikategorikan memiliki daya tarik yang signifikan di pasar. Genre Role-Playing menyumbang sekitar 14.97%, menunjukkan popularitas yang kuat bagi game dengan fokus pada cerita, karakter, dan pengembangan karakter. Genre Platform dan Action juga memiliki kontribusi yang signifikan, masing-masing sekitar 12.27% dan 11.41%, menunjukkan bahwa game dengan aksi dan petualangan yang kuat masih sangat diminati oleh pemain.Sementara itu, genre Fighting, Racing, dan Shooter memiliki kontribusi yang lebih rendah, masing-masing sekitar 2.58%, 6.26%, dan 6.01%. Ini mungkin menunjukkan perluasan potensi pasar dan peningkatan fokus pada genre-genre ini untuk meningkatkan penjualan.')
st.write ('1. Dengan kontribusi penjualan tertinggi, fokus pada pengembangan dan pemasaran game dengan genre Misc dan Role-Playing dapat menjadi strategi yang baik untuk meningkatkan pendapatan.')
st.write('2. Dengan popularitas yang kuat, upaya pemasaran yang lebih besar dan pengembangan konten berkualitas tinggi dalam genre Platform dan Action dapat meningkatkan penjualan lebih lanjut.')
st.write('3. Meskipun memiliki kontribusi penjualan yang lebih rendah, memperhatikan tren dan preferensi pasar serta inovasi dalam pengembangan game dalam genre-genre ini dapat membuka peluang baru untuk meningkatkan penjualan di masa depan.')

platform_cols = ['Platform_3DS', 'Platform_DS', 'Platform_GB', 'Platform_GBA', 'Platform_GC', 'Platform_N64',
                 'Platform_NES', 'Platform_PC', 'Platform_SNES', 'Platform_Wii', 'Platform_WiiU', 'Platform_X360',
                 'Platform_XB', 'Platform_XOne']

# Total sales by platform
sales_by_platform = df[platform_cols].sum()

# Create bar plot of total sales by platform
st.subheader('Penjualan Berdasarkan Platform')
plt.figure(figsize=(12, 6))
sales_by_platform.plot(kind='bar')
plt.title('Penjualan Berdasarkan Platform')
plt.xlabel('Platform')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.tight_layout()
platform_plot = plt.gcf()
st.pyplot(platform_plot)  # Show plot

# Calculate and display sales percentages by platform
st.write("Presentase Penjualan Berdasarkan Platform:")
total_sales = sales_by_platform.sum()
for platform in platform_cols:
    percentage = (sales_by_platform[platform] / total_sales) * 100
    st.write(f"- {platform}: {percentage:.2f}%")

st.write('Platform DS (Nintendo DS) adalah yang paling diminati dengan 18.53%, menandakan pangsa pasar yang kuat. GBA (Game Boy Advance) dan 3DS (Nintendo 3DS) juga populer, masing-masing sekitar 11.17% dan 10.06%. Meskipun Xbox 360 hanya mencapai 8.71%, masih memiliki pangsa pasar yang signifikan di antara konsol. Platform NES (Nintendo Entertainment System) hanya berkontribusi 0.25%, kemungkinan karena usia platform yang tua dan ketersediaan game yang terbatas dalam dataset.')
st.write('1.Fokus pada Pengembangan Game untuk Platform Populer: Mengingat kontribusi penjualan yang signifikan dari platform seperti Nintendo DS, Game Boy Advance, dan Nintendo 3DS, fokus pada pengembangan game untuk platform-platform ini bisa menjadi strategi yang baik untuk mencapai audiens yang lebih luas.')
st.write('2.Eksplorasi Potensi Pasar Xbox: Meskipun tidak sepopuler platform Nintendo, Xbox 360 masih memiliki pangsa pasar yang cukup besar. Eksplorasi potensi pasar untuk game-game Xbox dan peningkatan fokus pada platform ini bisa membantu meningkatkan penjualan di segmen konsol.')


df = df[df['Year'] != 2006.4064433147544]
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Year')
plt.title('Count of Games Released Each Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
year_plot = plt.gcf()

total_games = df.shape[0]
year_counts = df['Year'].value_counts()
year_percentages = (year_counts / total_games) * 100

# Tampilkan presentase di luar plot
st.pyplot(year_plot)  # Show plot
st.subheader('Percentage of Games Released Each Year')
for year, percentage in year_percentages.items():
    st.write(f"- {year}: {percentage:.2f}%")

st.write('Tahun 2004 adalah puncak kontribusi penjualan dengan 8.66%, menunjukkan bahwa game-game yang dirilis pada tahun tersebut masih memiliki daya tarik yang kuat di pasar. Sementara itu, tahun 2006 dan 2007 juga menonjol dengan kontribusi penjualan sekitar 7.67% dan 7.55% secara berturut-turut, menunjukkan bahwa game-game yang dirilis pada periode ini juga masih memiliki dampak yang signifikan dalam penjualan. Namun, penjualan mulai menurun secara bertahap pada tahun-tahun berikutnya, terutama pada tahun 2016 yang hanya mencapai 1.73%, menandakan pergeseran tren atau preferensi pasar yang perlu dipertimbangkan oleh pengembang game.')
st.write('1.Eksplorasi Potensi Game Retro: Mengingat bahwa tahun-tahun awal, seperti 2004, 2006, dan 2007, memiliki kontribusi penjualan yang signifikan, mungkin ada potensi untuk memperkenalkan ulang atau membuat game yang terinspirasi oleh game-game retro dari periode ini.')
st.write('2.Evaluasi Strategi Rilis Game: Memperhatikan tren penjualan berdasarkan tahun rilis dapat membantu pengembang dan penerbit untuk mengevaluasi strategi rilis game mereka. Ini termasuk menentukan waktu rilis yang optimal untuk memaksimalkan dampak dan penjualan game.')



st.subheader("K-Means Clustering")


n_clusters = st.sidebar.slider("Select number of clusters", 2, 10)

# Preprocessing the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Calculate inertia values
inertia_values = []
k_range = range(2, 11)  # Range of clusters from 2 to 10

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia_values.append(kmeans.inertia_)

# Plotting the elbow method
st.subheader("Elbow Method for Optimal K")
fig, ax = plt.subplots()
ax.plot(k_range, inertia_values, marker='o')
ax.set_xlabel('Number of clusters (K)')
ax.set_ylabel('Inertia')
ax.set_title('Elbow Method for Optimal K')
elbow_plot = plt.gcf()
st.pyplot(elbow_plot)
st.write("Disini kita bisa menentukan berapa cluster yang optimal untuk diterapkan pada model kita")

# PCA for dimensionality reduction
pca = PCA(n_components=2)  # Reduce to 2 dimensions
X_pca = pca.fit_transform(X_scaled)

# KMeans clustering
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X_pca)
df['Cluster'] = kmeans.labels_

# Display the dataset with cluster labels
st.write(f"Hasil Clusters dengan jumlah {n_clusters} Clusters:")
st.write(df)

# Add noise to cluster points
def add_noise(data, noise_level=0.05):
    return data + np.random.randn(*data.shape) * noise_level

# Plotting the clusters with noise
plt.figure(figsize=(10, 8))
for cluster_num in range(n_clusters):
    cluster_data = df[df['Cluster'] == cluster_num]
    noisy_data = add_noise(cluster_data.iloc[:, 0:2])
    plt.scatter(noisy_data.iloc[:, 0], noisy_data.iloc[:, 1], label=f'Cluster {cluster_num}', alpha=0.7)

plt.title('Visualisasi Klustering')
plt.legend()
cluster_plot = plt.gcf()  
st.pyplot(cluster_plot) 