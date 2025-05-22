import pandas as pd
import qrcode
import os

#Arquivo original
ARQUIVO_EXCEL = "GERAR_QRCODE (1).xlsx"
PASTA_SAIDA = "qrcodes"

#Garante que a pasta exista
os.makedirs(PASTA_SAIDA, exist_ok=True)

#Lê o arquivo
df = pd.read_excel(ARQUIVO_EXCEL)

#Loop nas linhas 
for _, row in df.iterrows():
    nome_convidado = str(row["NOME COMPLETO"]).strip()
    qtd_acompanhantes = int(row.get("QTD. ACOMPANHANTE", 0))

    id_convidado = nome_convidado.lower().replace(" ", "_")
    qr = qrcode.make(id_convidado)
    qr.save(os.path.join(PASTA_SAIDA, f"{id_convidado}.png"))
    print(f"QR gerado para: {nome_convidado}")

    for i in range(qtd_acompanhantes):
        coluna = "NOME DO ACOMPANHETE" if i == 0 else f"NOME DO ACOMPANHETE.{i}"
        nome_acomp = row.get(coluna)

        if pd.isna(nome_acomp):
            id_acomp = f"{id_convidado}_acompanhante_{i+1}"
            label = "[Sem nome]"
        else:
            nome_acomp = str(nome_acomp).strip()
            id_acomp = nome_acomp.lower().replace(" ", "_")
            label = nome_acomp

        qr_acomp = qrcode.make(id_acomp)
        qr_acomp.save(os.path.join(PASTA_SAIDA, f"{id_acomp}.png"))
        print(f"QR gerado para acompanhante {i+1} de {nome_convidado}: {label}")