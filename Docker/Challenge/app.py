from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to the Redis container
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

# Welcome page
@app.route("/")
def home():
    return "Welcome to my Docker Containers Challenge!"

# Visit counter
@app.route("/count")
def count():
    visits = redis_client.incr("visits")
    return f"Visit count: {visits}"

# Start Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)