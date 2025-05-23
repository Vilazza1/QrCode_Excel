# 🎟️ Gerador de QR Code para Lista de Convidados

Um sistema em Python que lê um arquivo Excel com dados de convidados, gera QR Codes personalizados com base no nome de cada um e considera a presença de acompanhantes. Ideal para eventos, festas ou conferências.

---

## ✅ Funcionalidades

- 📥 Leitura de arquivo Excel (`.xlsx`) como base de dados.
- 🧾 Geração de QR Code usando o **nome do convidado** como identificador único.
- 👥 Geração automática de QR Code para **acompanhantes**, se existirem.
- 📁 Armazenamento dos QR Codes em pastas locais organizadas.
- 🌐 Preparado para deploy em servidores como **Render** (em breve).
- 🧪 Testável localmente com dados reais.

---

## 🛠️ Stack utilizada

| Categoria           | Tecnologia/Lib           |
|--------------------|--------------------------|
| Linguagem          | Python 3.10+             |
| Leitura Excel      | `pandas`, `openpyxl`     |
| Geração de QR Code | `qrcode[pil]`            |
| Ambiente virtual   | `venv`                   |
| IDE recomendada    | Visual Studio Code       |
| Hospedagem (futuro)| Render.com               |

---

## 📦 Instalação e uso local

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/qrconvidados.git
cd qrconvidados

2. Crie e ative um ambiente virtual:

python -m venv venv
# Ativando:
# Windows:
.\venv\Scripts\activate

3. Instale as dependências:

pip install -r requirements.txt

4. Adicione seu arquivo Excel na raiz do projeto:

O arquivo deve se chamar convidados.xlsx e conter ao menos as colunas:

Nome

Acompanhante (opcional: Sim ou Não)

5. Execute o script:

python gerar_qrcodes.py

🗂️ Estrutura do projeto

qrconvidados/
│
├── convidados.xlsx          # Base de dados
├── gerar_qrcodes.py         # Script principal
├── /qrcodes/                # QR Codes gerados
│   ├── nome_sobrenome.png
│   ├── acompanhante_nome.png
│   └── ...
├── requirements.txt
└── README.md


🔁 Lógica de funcionamento

Leitura do Excel:

Usamos pandas para carregar o arquivo convidados.xlsx.

Processamento de convidados:

Para cada linha da planilha:

Pegamos o valor da coluna Nome.

Verificamos se há acompanhante (coluna Acompanhante = "Sim").

Geração do QR Code:

Criamos um QR Code com base no nome do convidado.

Ex: João Silva → QR com ID "joao_silva"

Se houver acompanhante, criamos outro QR Code com nome do acompanhante derivado (ex: joao_silva_acompanhante).

Armazenamento:

Os QR Codes são salvos em arquivos .png na pasta /qrcodes/.

🛰️ Deploy na Render (futuro)

Planejamos transformar o script em uma API Flask ou uma interface web com Streamlit, e então hospedar na Render.

Assim, o usuário poderá subir o Excel diretamente no navegador e baixar os QR Codes prontos.

✍️ Contribuição

Ideias ou melhorias? Fique à vontade para abrir uma issue ou pull request.

📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

📄 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.






