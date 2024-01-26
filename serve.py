from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def router():
    if request.method == "POST":
        subprocess.Popen(["python3", "stress_cpu.py"]) 
        
        return "stress_cpu.py started"
    elif request.method == "GET":
        priv_ip = socket.gethostbyname(socket.gethostname())
        
        return jsonify({"private_ip": priv_ip})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
