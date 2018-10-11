const { app, BrowserWindow } = require("electron");

function createWindow() {
  // Create the browser window.
  win = new BrowserWindow();

  // and load the index.html of the app.
  win.loadFile("public/index.html");
}

app.on("ready", createWindow);
