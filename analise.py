import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do campeonato brasileiro
df = pd.read_csv(r'C:\Users\Vinicius\OneDrive\Documentos\Projeto-Python-Futebol\brasileirao.csv')
# r foi utilizado para inverter as barras

# Filtrar os dados para o time Fortaleza e os anos de interesse
years = [2003, 2005, 2006, 2019, 2020, 2021, 2022, 2023]
fortaleza_data = df[(df['team'] == 'Fortaleza') & (df['season'].isin(years))]

# Ordenar os dados por ano para garantir a ordem cronológica
fortaleza_data = fortaleza_data.sort_values(by='season')

# Melhorando o gráfico de evolução dos pontos
plt.figure(figsize=(10, 6))

# Plotar a linha e os pontos
plt.plot(fortaleza_data['season'], fortaleza_data['points'], marker='o', linestyle='-', color='blue', markersize=8, linewidth=2)

# Adicionar rótulos aos pontos
for i, row in fortaleza_data.iterrows():
    plt.text(row['season'], row['points'] + 0.5, f"{row['points']}", ha='center', fontsize=10)

# Adicionar título e rótulos aos eixos
plt.title('Evolução dos Pontos do Fortaleza no Brasileirão (2003-2023)', fontsize=16, fontweight='bold')
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Pontos', fontsize=12)

# Ajustar limites do eixo X para mostrar os anos exatos
plt.xticks(fortaleza_data['season'], rotation=45)

# Adicionar uma grade para facilitar a leitura dos dados
plt.grid(True, linestyle='--', alpha=0.6)

# Exibir o gráfico
plt.tight_layout()  # Ajusta o layout para que os rótulos não se sobreponham
plt.show()
