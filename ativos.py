import csv

ativos_ibovespa = [
    ["Código", "Nome do Ativo", "Setor", "Preço Atual (R$)", "Preço Médio (R$)", "Total de Ações"],
    ["ABEV3", "Ambev S.A.", "Bebidas", 15.50, 14.80, 100],
    ["PETR4", "Petrobras S.A.", "Petróleo, Gás e Biocombustíveis", 28.30, 27.50, 150],
    ["VALE3", "Vale S.A.", "Mineração", 85.20, 80.00, 200],
    ["ITUB4", "Itaú Unibanco Holding S.A.", "Bancos", 22.10, 21.50, 120],
    ["BBDC4", "Bradesco S.A.", "Bancos", 18.75, 17.80, 130],
    ["MGLU3", "Magazine Luiza S.A.", "Varejo", 3.50, 3.20, 250],
    ["GGBR4", "Gerdau S.A.", "Siderurgia", 12.40, 11.90, 180],
    ["LREN3", "Lojas Renner S.A.", "Varejo", 25.60, 24.00, 90],
    ["WEGE3", "WEG S.A.", "Bens de Capital", 30.80, 29.50, 110]
]

file_path = "ativos.csv"
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(ativos_ibovespa)