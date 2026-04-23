# Build stage
FROM node:18-alpine as builder

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY . .


# Production stage
FROM node:18-alpine

WORKDIR /app

# Create non-root user
RUN addgroup -S hng && adduser -S hngdevops -G hng

# Copy built assets and production dependencies
COPY --from=builder /app .

USER hngdevops

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:3000/health || exit 1

CMD ["node", "app.js"]