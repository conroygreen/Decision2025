from flask import Flask, request, jsonify
from obsws_python import ReqClient
import json
import os

app = Flask(__name__)

# Load config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../config.json')
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

OBS_IP = config.get("obs_ip", "127.0.0.1")
OBS_PORT = config.get("obs_port", 4455)
OBS_PASSWORD = config.get("obs_password", "")
OBS_SOURCES = {
    "CONSTITUENCY": "ConstituencyTxt",
    "PARISH": "parishTxt",
    "JLP": "JLP_votes",
    "PNP": "PNP_votes",
    "#OF_BOXES": "CountedTxt",
    "BOX_COUNT": "totalBOX",
    "COUNT%": "TotalPercent",
}

client = None


@app.route("/connect", methods=["POST"])
def connect_obs():
    global client
    try:
        client = ReqClient(host=OBS_IP, port=OBS_PORT, password=OBS_PASSWORD)
        return jsonify({"status": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/disconnect", methods=["POST"])
def disconnect_obs():
    global client
    try:
        if client:
            client.ws.close()
        client = None
        return jsonify({"status": "disconnected"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/status", methods=["GET"])
def status():
    if client:
        return jsonify({"status": "connected"})
    return jsonify({"status": "disconnected"})


@app.route("/update", methods=["POST"])
def update_text():
    global client
    data = request.json
    if not client:
        return jsonify({"status": "error", "message": "Not connected to OBS"}), 400

    try:
        for key, source in OBS_SOURCES.items():
            if key in data:
                value = str(data[key])
                client.set_input_settings(source, {"text": value}, overlay=True)
        return jsonify({"status": "updated"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/config", methods=["GET", "POST"])
def update_config():
    global OBS_IP, OBS_PORT, OBS_PASSWORD
    if request.method == "POST":
        new_config = request.json
        OBS_IP = new_config.get("obs_ip", OBS_IP)
        OBS_PORT = new_config.get("obs_port", OBS_PORT)
        OBS_PASSWORD = new_config.get("obs_password", OBS_PASSWORD)
        with open(CONFIG_PATH, "w") as f:
            json.dump(new_config, f, indent=2)
        return jsonify({"status": "saved"})
    else:
        return jsonify({
            "obs_ip": OBS_IP,
            "obs_port": OBS_PORT,
            "obs_password": OBS_PASSWORD
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
