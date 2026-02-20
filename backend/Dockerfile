# ── Stage: Runtime ──────────────────────────────────────────────────────────
FROM python:3.12-slim

# Keeps Python from buffering stdout/stderr (nice for Docker logs)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

# Expose the FastAPI port
EXPOSE 8000

# Start Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
