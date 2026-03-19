# TeamSpeak Spoofer

A lightweight Windows utility that resets your TeamSpeak 3 identity by wiping local configuration files and randomizing your Windows Product ID — effectively removing your fingerprint from TeamSpeak servers.

---

## What It Does

TeamSpeak 3 identifies clients using a combination of local configuration data and the Windows Product ID. This tool removes both traces in three steps:

1. **Closes TeamSpeak** — Detects if `ts3client_win64.exe` is running and force-closes it before making changes.
2. **Deletes TS3 config** — Removes the `%APPDATA%\TS3Client` folder, which contains your unique identity, bookmarks, cache, and settings.
3. **Randomizes Product ID** — Generates a new random Windows Product ID and writes it to the registry at `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProductId`.

After spoofing, TeamSpeak will generate a fresh identity on the next launch — making you appear as an entirely new client.

---

## Screenshot

The tool has a simple Tkinter GUI with a single "Spoof" button and a color-coded log output:

- 🟢 **Green** — Success messages
- 🔴 **Red** — Errors
- 🔵 **Blue** — Info / status updates

---

## Requirements

- **Windows** (uses `winreg`, `taskkill`, and `ctypes.windll`)
- **Python 3.6+**
- **Administrator privileges** (required to modify the registry)

No external dependencies — the script uses only Python standard library modules.

---

## Usage

Right-click and **Run as Administrator**, or launch from an elevated terminal:

```bash
python spoofer.py
```

Click the **Spoof** button in the GUI and wait for the process to complete. 

Note: If anyone were to use this to avoid any bans, they would also need a VPN (since private teamspeak servers keep the identity AND the IP in their ban logs)

---

## Project Structure

```
Teamspeak-Spoofer/
├── spoofer.py      # Main script with GUI and spoofing logic
├── LICENSE          # MIT License
└── README.md
```

---

## Disclaimer

This tool is provided for educational purposes. The author is not responsible for any misuse or violations of any service's terms of use.

---

## AI Use

This README was written with the assistance of [Claude](https://claude.ai) by Anthropic and revised by the author. The project code was written by the author.

---

## License

This project is licensed under the [MIT License](LICENSE).

```
MIT License

Copyright (c) 2026 Alcachofo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
