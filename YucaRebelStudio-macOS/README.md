# YucaRebel Studio

**YucaRebel Studio** is a pro-grade production controller for OBS (Open Broadcaster Software), designed for fast-paced, high-quality live content. Built on Electron with a Flask backend, YucaRebel Studio enables real-time control of your OBS scenes, sources, and media with seamless LAN integration.

---

## 🚀 Features

- 🎛️ Intuitive Desktop App (Electron-based)
- 🔒 IP and Password Settings Panel (Persistent between sessions)
- 🧠 Built-in Flask Backend (Auto-runs with the app)
- 📡 Works over LAN (No Internet Required)
- 🎯 Auto-docks and smart UI scaling
- 🖥️ macOS (M1/M2/M3/M4) compatible `.dmg` installer

---

## 📦 Installation

### macOS

1. Download the latest `.dmg` release from [Releases](#).
2. Open the `.dmg` file and drag **YucaRebel Studio** into your Applications folder.
3. Open the app. (You may need to allow it under **System Preferences > Security & Privacy** the first time.)

> ⚠️ Flask backend starts automatically in the background. No additional configuration required.

---

## 🔧 Configuration

### OBS WebSocket Setup

1. Open OBS and go to **Tools > WebSocket Server Settings**.
2. Enable the server.
3. Note your **IP address**, **Port** (default: `4455`), and **Password**.
4. Enter these values in YucaRebel Studio’s **Settings Panel** and click **Connect**.

---

## 📁 File Structure (Developer Edition)

