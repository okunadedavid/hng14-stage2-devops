- in app.js ln 6
const API_URL = 'http://localhost:8000'
The API_URL is hardcoded to the localhost:8000, this won't work in a container
Fixed to: process.env.API_URL || 'http://localhost:8000'; , with this it can be configured via the environment variable in compose.

-in app.js ln 13
 const response = await axios.post(`${API_URL}/jobs`)
 this service receives a request body from the user, but it does not forward it to the API
 Fixed to: const response = await axios.post(`${API_URL}/jobs/${req.body}`), with this the request would be forwarded to the API

- in app.js 
Added a health check endpoint, this is needed for docker health check
    app.get('/health', (req, res) => {
    res.status(200).json({ status: 'Healthy' });
    });

- in app.js ln 34 and 35
The port is harcoded,app.listen(3000() => {
    console.log(`Frontend running on port {3000})
})
Fixed to: app.listen(PORT, () => {
  console.log(`Frontend running on port ${PORT}`);
});

- in main.py ln 8
r = redis.Redis(host="localhost", port=6379), this won't work in a container
Fixed to: r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

- in main.py
Added a health check.
@app.get("/health")
def health():
    return {"status": "healthy"}

- in worker.py ln 6
r = redis.Redis(host="localhost", port=6379), this won't work in a container
Fixed to: r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)