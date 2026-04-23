# Build stage
FROM python:3.11-alpine as builder
WORKDIR /app
COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-alpine

# Set working directory and create non-root user
WORKDIR /app

RUN addgroup -S hng && adduser -S hngdevops -G hng

# Copy built assets and production dependencies
COPY --from=builder /root/.local /home/hngdevops/.local

COPY main.py .
ENV PATH=/home/hngdevops/.local/bin:$PATH

USER hngdevops
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8000/health || exit 1
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]