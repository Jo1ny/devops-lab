from flask import Flask
import redis
import os

app = Flask(__name__)

# Имя хоста берем из окружения, по умолчанию 'redis'
redis_host = os.environ.get('REDIS_HOST', 'redis')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    try:
        visits = r.incr('counter')
    except redis.exceptions.ConnectionError:
        visits = "База недоступна"
    return f"<h1>Привет из Docker!</h1><p>Количество просмотров: <b>{visits}</b></p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)