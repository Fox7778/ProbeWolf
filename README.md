# 🐺 ProbeWolf

**ProbeWolf** is a simple, lightweight TCP port scanner written in Python. It checks which ports on a target host are open and shows the name of the service that usually runs on them.

It uses only the Python standard library, so there is nothing to install besides Python itself.

> ⚠️ **Use responsibly.** Only scan your own devices, your own network, or hosts you have explicit permission to test (for example `scanme.nmap.org`, which the Nmap project allows for testing). Scanning systems without permission may be illegal.

---

## Features

- TCP connect scan of a single port or a range of ports
- Service name detection for open ports (e.g. `22/tcp ssh`)
- IPv4 and IPv6 support
- Adjustable connection timeout
- Command-line flags **or** an interactive mode that asks for missing information
- Built-in help (`-h`)
- No external dependencies

---

## Requirements

- Python **3.6** or newer
- Works on Linux, macOS and Windows

---

## Installation

Clone or download the repository:

```bash
git clone https://github.com/Fox7778/ProbeWolf.git
cd ProbeWolf
```

You can now run it with:

```bash
python3 probewolf.py
```

### Run it as a command (Linux / macOS)

To run ProbeWolf from anywhere just by typing `probewolf`, like `nmap`:

1. Make sure the first line of `probewolf.py` is:
   ```python
   #!/usr/bin/env python3
   ```
2. Make the file executable:
   ```bash
   chmod +x probewolf.py
   ```
3. Link it into a folder in your `PATH`:
   ```bash
   mkdir -p ~/.local/bin
   ln -s "$(pwd)/probewolf.py" ~/.local/bin/probewolf
   ```

If you get `command not found`, add this line to your `~/.bashrc` (or `~/.zshrc`) and open a new terminal:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

## Usage

```
probewolf [target] [-p PORT] [-s START] [-e END] [-t TIMEOUT] [-6]
```

| Argument | Description | Default |
|---|---|---|
| `target` | Target IP address | asked interactively if missing |
| `-p`, `--port` | Scan only one specific port | – |
| `-s`, `--start` | First port of the range | `1` |
| `-e`, `--end` | Last port of the range | `1024` |
| `-t`, `--timeout` | Time to wait for a response, in seconds | `0.5` |
| `-6`, `--ipv6` | Use IPv6 instead of IPv4 | off |
| `-h`, `--help` | Show help and exit | – |

### Examples

Scan the default range (ports 1–1024) on your own computer:

```bash
probewolf 127.0.0.1
```

Scan a single port:

```bash
probewolf 127.0.0.1 -p 8080
```

Scan a custom range with a shorter timeout:

```bash
probewolf 192.168.1.10 -s 1 -e 10000 -t 0.2
```

Scan over IPv6:

```bash
probewolf ::1 -6 -p 8080
```

### Interactive mode

Run ProbeWolf without a target and it will ask for what it needs:

```
$ probewolf
IPv4 or IPv6? [IPv4/ipv6]:
Target address: 127.0.0.1
Specific port? [y/N]: y
Port: 8080
Port: 8080/tcp http-alt OPENED
```

### Example output

```
Port: 22/tcp ssh OPENED
Port: 80/tcp http OPENED
Port: 8000/tcp unknown OPENED
```

---

## Try it out

Want to see ProbeWolf find something? Start a small web server in a second terminal:

```bash
python3 -m http.server 8080
```

Then scan it:

```bash
probewolf 127.0.0.1 -p 8080
```

---

## Tips

- Scanning hosts behind a firewall can be slow, because ProbeWolf waits the full timeout on every filtered port. Scanning all 65535 ports with a 0.5 s timeout can take hours, so start with a smaller range or a lower timeout (`-t 0.1` is usually fine in a local network).
- Service names come from your operating system's service list, so ports without a well-known service are shown as `unknown`.

---

## Roadmap

- [ ] Multithreaded scanning for much faster scans
- [ ] Scanning IP ranges in CIDR notation (e.g. `192.168.1.0/24`)
- [ ] Banner grabbing to detect the exact service and version
- [x] Hostname support (e.g. `example.com`)
- [ ] UDP scanning
- [ ] Saving results to a file

---

## Author

**Filip Novák**, 2026
