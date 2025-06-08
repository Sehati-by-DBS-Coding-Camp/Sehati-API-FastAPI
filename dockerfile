# Dockerfile

# 1. Gunakan base image resmi Python
FROM python:3.10-slim

# 2. Set working directory di dalam container
WORKDIR /code

# 3. Copy file requirements terlebih dahulu untuk caching layer
COPY ./requirements.txt /code/requirements.txt

# 4. Install semua dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Copy seluruh isi folder app ke dalam container
COPY ./app /code/app

# 6. Jalankan aplikasi menggunakan Uvicorn
#    Gunicorn sering digunakan sebagai process manager di produksi
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]