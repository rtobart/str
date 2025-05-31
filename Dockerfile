FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY main.py ./

# expose port
EXPOSE 8000

# start the service
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]