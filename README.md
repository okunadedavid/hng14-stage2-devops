# hng14-stage2-devops
# Job processing 
This repo contains:

✅ Frontend (Node.js + Express) — Submit and track jobs via browser
✅ API (Python + FastAPI) — Create jobs and serve status updates
✅ Worker (Python) — Background processor that handles jobs from Redis queue
✅ Redis — Shared in-memory data store for job queuing
✅ Docker Compose — Orchestrates all services locally
✅ CI/CD Pipeline — GitHub Actions: lint → test → build → scan → deploy

# Prerequisites
-Github account
-Docker
-Terminal

# Steps for startup
1. Clone Your Fork
In git hub, fork the repo, then run in terminal
- git clone https://github.com/okunadedavid/hng14-stage2-devops.git
then run:
- cd hng14-stage2-devops

2. Copy Environment File
cp .env.example

3. Start the Full Stack
run in terminal
docker compose up --build -d

4. Check if container is running
docker compose ps

5. Open in Browser
Visit these URLs:
Frontend UI:	http://localhost:3000
API Docs: http://localhost:8000/docs