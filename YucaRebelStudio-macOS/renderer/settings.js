document.addEventListener("DOMContentLoaded", () => {
  const config = JSON.parse(localStorage.getItem("config")) || {};
  document.getElementById("ip").value = config.obs_ip || "127.0.0.1";
  document.getElementById("port").value = config.obs_port || 4455;
  document.getElementById("password").value = config.obs_password || "";

  if (config.theme === "dark") document.body.classList.add("dark");
});

function saveSettings() {
  const config = {
    obs_ip: document.getElementById("ip").value,
    obs_port: parseInt(document.getElementById("port").value),
    obs_password: document.getElementById("password").value,
    theme: document.body.classList.contains("dark") ? "dark" : "light"
  };
  fetch("/config", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(config)
  });
  localStorage.setItem("config", JSON.stringify(config));
  alert("Settings saved");
}

function connect() {
  fetch("/connect", { method: "POST" })
    .then(res => res.json())
    .then(res => alert(res.status));
}

function disconnect() {
  fetch("/disconnect", { method: "POST" })
    .then(res => res.json())
    .then(res => alert(res.status));
}

function updateOBS() {
  const data = {
    "CONSTITUENCY": document.getElementById("const").value,
    "PARISH": document.getElementById("parish").value,
    "JLP": document.getElementById("jlp").value,
    "PNP": document.getElementById("pnp").value,
    "#OF_BOXES": document.getElementById("boxes").value,
    "BOX_COUNT": document.getElementById("box_count").value,
    "COUNT%": document.getElementById("percent").value
  };
  fetch("/update", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  }).then(res => res.json()).then(res => alert(res.status));
}

function toggleTheme() {
  document.body.classList.toggle("dark");
  saveSettings();
}
