from flask import Flask, jsonify
import os
import psutil
import platform

app = Flask(__name__)


@APP.get("/metrics")
def metrics():
    cpu = psutil.cpu_percent(percpu=True)
    mem = f"{psutil.virtual_memory().used // 1024**2} MB"
    pid = os.getpid()
    so = platform.platform()

    return jsonify([
        {
            'Metricas': {
                "cpu_por_nucleo": cpu,
                "memoria": mem,
                "id": pid,
                "so": so
            }
        }
    ])

@APP.get("/info")
def info():
    return jsonify([
        {
            'integrantes': [
                'Gustavo Viana do Nascimento'
            ]
        }
    ])

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=5000)