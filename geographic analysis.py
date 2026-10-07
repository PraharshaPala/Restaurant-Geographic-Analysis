
import pandas as pd
import folium

# Load dataset
df = pd.read_csv("Dataset .csv", encoding='latin-1')

# Create map centered on average coordinates
m = folium.Map(
    location=[df['Latitude'].mean(), df['Longitude'].mean()],
    zoom_start=5
)

# Add restaurant markers
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=2,
        popup=row['Restaurant Name'],
        fill=True
    ).add_to(m)

# Save map
m.save("restaurant_locations.html")

print("Map saved as restaurant_locations.html")
