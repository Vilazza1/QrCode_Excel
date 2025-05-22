import pandas as pd
import qrcode
import os
import json

# Arquivo original
ARQUIVO_EXCEL = "GERAR_QRCODE (1).xlsx"
PASTA_SAIDA = "qrcodes"

# Garante que a pasta exista
os.makedirs(PASTA_SAIDA, exist_ok=True)

# Lê o arquivo
df = pd.read_excel(ARQUIVO_EXCEL)

# Loop nas linhas 
for _, row in df.iterrows():
    nome_convidado = str(row["NOME COMPLETO"]).strip()
    cnpj = str(row.get("CNPJ", "")).strip()
    razao_social = str(row.get("RAZÃO SOCIAL", "")).strip()
    qtd_acompanhantes = int(row.get("QTD. ACOMPANHANTE", 0))

    # Dados do titular em formato JSON
    dados_titular = {
        "tipo": "titular",
        "nome": nome_convidado,
        "cnpj": cnpj,
        "razao_social": razao_social
    }
    dados_titular_json = json.dumps(dados_titular, ensure_ascii=False)

    # Nome do arquivo baseado no nome do titular
    id_convidado = nome_convidado.lower().replace(" ", "_")
    qr = qrcode.make(dados_titular_json)
    qr.save(os.path.join(PASTA_SAIDA, f"{id_convidado}.png"))
    print(f"QR gerado para titular: {nome_convidado}")

    for i in range(qtd_acompanhantes):
        # Coluna dos acompanhantes, trata caso existam várias colunas para acompanhantes
        coluna = "NOME DO ACOMPANHETE" if i == 0 else f"NOME DO ACOMPANHETE.{i}"
        nome_acomp = row.get(coluna)

        if pd.isna(nome_acomp):
            nome_acomp = "[Sem nome]"

        nome_acomp = str(nome_acomp).strip()

        # Dados do acompanhante, incluindo nome do titular para referência
        dados_acomp = {
            "tipo": "acompanhante",
            "nome_acompanhante": nome_acomp,
            "nome_titular": nome_convidado
        }
        dados_acomp_json = json.dumps(dados_acomp, ensure_ascii=False)

        id_acomp = nome_acomp.lower().replace(" ", "_") if nome_acomp != "[Sem nome]" else f"{id_convidado}_acompanhante_{i+1}"
        qr_acomp = qrcode.make(dados_acomp_json)
        qr_acomp.save(os.path.join(PASTA_SAIDA, f"{id_acomp}.png"))
        print(f"QR gerado para acompanhante {i+1} de {nome_convidado}: {nome_acomp}")
