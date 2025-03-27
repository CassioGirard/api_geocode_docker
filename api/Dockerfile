# Use uma imagem base com Python
FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o container
COPY app.py .

# Instala as dependências
RUN pip install flask requests

# Expõe a porta 5000
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
