# 🚀 S3 Bucket Cleaner

Este script foi criado para **remover delete markers e versões antigas** de um bucket S3 de maneira eficiente, garantindo melhor gerenciamento de armazenamento.

## 📌 Descrição
Buckets S3 versionados podem acumular grandes quantidades de delete markers e versões obsoletas, aumentando custos e complexidade. Este script **automatiza a remoção desses itens**, melhorando a eficiência do armazenamento.

## 🚀 Pré-requisitos
Antes de rodar o script, certifique-se de ter:
- **Python 3.x** instalado
- **Boto3** instalado (`pip install boto3`)
- Permissões adequadas na AWS para deletar objetos do S3

## 🔧 Como usar
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/yurikrat/s3-bucket-cleaner.git
   cd s3-bucket-cleaner
   ```
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure suas credenciais AWS** (caso não estejam configuradas):
   ```bash
   aws configure
   ```
4. **Edite o script para definir o bucket correto:**
   Abra `semlimitacao_2025.py` e edite `BUCKET_NAME` com o nome do bucket desejado.

5. **Execute o script:**
   ```bash
   python semlimitacao_2025.py
   ```

## ⚡ Otimizações implementadas
✅ **Uso de deleção em lote (`delete_objects`)** – reduz chamadas para API da AWS
✅ **Paralelismo com `ThreadPoolExecutor`** – melhora a eficiência
✅ **Paginação eficiente** – garante que todos os objetos sejam processados
✅ **Retry com exponencial backoff** – evita falhas por throttling

## 🤝 Contribuições
Sinta-se à vontade para **abrir issues** e enviar **pull requests**. Melhorias são sempre bem-vindas!

## 📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
💡 Criado para simplificar o gerenciamento de buckets S3! 🚀

