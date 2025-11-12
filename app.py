from flask import Flask
import os
import psutil
import json
import platform

app = Flask(__name__)

@app.get("/metrics")
def metrics():

    #uso de cpu
    cpu = psutil.cpu_percent(percpu=True)

    #memória
    mem = psutil.virtual_memory().used //1024**2, "MB"

    #PID do processo
    pid = os.getpid()

    # S.O.
    so = platform.platform()

    return json.dumps([
        {
            'Metricas': {
                "cpu_por_nucleo": cpu,
                "memoria": mem,
                "id": pid,
                "so": so,
            }
        }
    ])

@app.get("/info")
def info():
    return json.dumps([
        {
            'integrantes': [
                'Gustavo Viana do Nascimento'
            ]
        }
    ])