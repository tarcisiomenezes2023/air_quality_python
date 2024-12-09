import pandas as pd
import matplotlib.pyplot as plt
import os

# Filepaths
file_path_budapest = r'C:\Users\Tarci\OneDrive\Documentos\chart_contents\budapest_air_quality_july.xlsx'
file_path_sao_paulo = r'C:\Users\Tarci\OneDrive\Documentos\chart_contents\sao_paulo_air_quality_july.xlsx'

# Output directory
output_dir = r'C:\Users\Tarci\OneDrive\Documentos\chart_contents\charts'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'air_quality_comparison.png')

# Read data from xlsx files
df_budapest = pd.read_excel(file_path_budapest, skiprows=0)
df_sao_paulo = pd.read_excel(file_path_sao_paulo, skiprows=0)

# Convert the date values to datetime
df_budapest['Date'] = pd.to_datetime(df_budapest['Date'], errors='coerce')
df_sao_paulo['Date'] = pd.to_datetime(df_sao_paulo['Date'], errors='coerce')

# Remove invalid data
df_budapest = df_budapest.dropna(subset=['Date'])
df_sao_paulo = df_sao_paulo.dropna(subset=['Date'])

# Set Date as the index
df_budapest.set_index('Date', inplace=True)
df_sao_paulo.set_index('Date', inplace=True)

# Plotting
plt.figure(figsize=(14, 8))
plt.gcf().patch.set_facecolor('#F0F8FF')  # Light blue background

# Bar charts for Budapest
plt.bar(df_budapest.index - pd.Timedelta(days=0.2), df_budapest['O3'], width=0.4, color='skyblue', label='O₃ Budapest', alpha=0.8)
plt.bar(df_budapest.index + pd.Timedelta(days=0.2), df_budapest['CO'], width=0.4, color='orange', label='CO Budapest', alpha=0.8)

# Bar charts for São Paulo
plt.bar(df_sao_paulo.index - pd.Timedelta(days=0.2), df_sao_paulo['O3'], width=0.4, color='green', label='O₃ São Paulo', alpha=0.8)
plt.bar(df_sao_paulo.index + pd.Timedelta(days=0.2), df_sao_paulo['CO'], width=0.4, color='red', label='CO São Paulo', alpha=0.8)

# Customizing the chart
plt.title('Air Quality Comparison: Budapest vs São Paulo (July)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Concentration (µg/m³)', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Save the chart
plt.tight_layout()
plt.savefig(output_path)
plt.show()

print(f"Chart saved to {output_path}")

