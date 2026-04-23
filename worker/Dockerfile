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

COPY . .
ENV PATH=/home/appuser/.local/bin:$PATH

USER hngdevops

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import redis; r=redis.Redis(host='${REDIS_HOST:-redis}'); r.ping()" || exit 1
CMD ["python", "worker.py"]