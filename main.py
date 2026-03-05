#!/usr/bin/env python3
"""Emare Code — Cross-Platform Code Generator

Linux, macOS ve Windows'ta sorunsuz çalışan kod yazma programı.
"""
import sys
from pathlib import Path

# Rich import kontrolü
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    RICH = True
except ImportError:
    RICH = False
    print("💡 İpucu: 'pip install rich' ile daha iyi görünüm")

from core.code_generator import generator
from core.smart_factory import smart_factory
from data.repository import list_projects


BANNER = r"""
╔════════════════════════════════════════════╗
║         💻 EMARE CODE GENERATOR           ║
║   Cross-Platform Code Generation Tool      ║
╚════════════════════════════════════════════╝
"""


def cmd_create():
    """Yeni proje oluştur."""
    print("\n── 🆕 Yeni Proje Oluştur ──")
    name = input("Proje adı (snake_case): ").strip()
    if not name:
        print("❌ Proje adı boş olamaz.")
        return

    print("\nDil seç:")
    languages = ["python", "javascript", "go", "rust", "php", "bash"]
    for i, lang in enumerate(languages, 1):
        print(f"  {i}) {lang}")
    choice = input("Seçim [1]: ").strip() or "1"
    try:
        language = languages[int(choice) - 1]
    except (ValueError, IndexError):
        language = "python"

    description = input("Açıklama: ").strip() or f"{name} projesi"

    print("\nPlatform:")
    print("  1) Linux")
    print("  2) macOS")
    print("  3) Windows")
    print("  4) Hepsi (cross-platform)")
    plat_choice = input("Seçim [4]: ").strip() or "4"
    platforms = {"1": "linux", "2": "macos", "3": "windows", "4": "all"}
    platform = platforms.get(plat_choice, "all")

    print()
    generator.create_project(name, language, description, platform)


def cmd_smart():
    """Doğal dil ile proje üret."""
    print("\n── 🧠 Akıllı Üretim (Doğal Dil) ──")
    request = input("Ne yapmak istiyorsun? (örn: 'file backup tool python'): ").strip()
    if not request:
        print("❌ İstek boş olamaz.")
        return

    print()
    smart_factory.build_from_request(request)


def cmd_list():
    """Üretilen projeleri listele."""
    projects = list_projects()

    if RICH:
        console = Console()
        table = Table(title="📦 Üretilen Projeler")
        table.add_column("#", style="cyan")
        table.add_column("Proje", style="green")
        table.add_column("Dil", style="yellow")
        table.add_column("Platform", style="magenta")
        table.add_column("Versiyon", style="blue")

        for i, proj in enumerate(projects, 1):
            table.add_row(
                str(i),
                proj["name"],
                proj["language"],
                proj.get("platform", "all"),
                proj.get("version", "1.0.0"),
            )
        console.print(table)
    else:
        print("\n── 📦 Üretilen Projeler ──")
        if not projects:
            print("Henüz proje yok.")
            return
        for i, proj in enumerate(projects, 1):
            print(f"{i}. {proj['name']} ({proj['language']} - {proj.get('platform', 'all')})")


def cmd_help():
    """Yardım menüsü."""
    help_text = """
Emare Code — Komutlar:

  create     Yeni proje oluştur (interaktif)
  smart      Doğal dil ile proje üret
  list       Üretilen projeleri listele
  help       Bu yardım menüsünü göster
  exit       Çıkış

Kısayol:
  python main.py create
  python main.py smart "create rest api for todo app"
"""
    if RICH:
        Console().print(Panel(help_text, title="📖 Yardım", border_style="blue"))
    else:
        print(help_text)


def interactive_menu():
    """İnteraktif menü."""
    print(BANNER)
    print("Komutlar: create, smart, list, help, exit")
    print()

    while True:
        try:
            cmd = input("emare-code> ").strip().lower()
            if not cmd:
                continue

            if cmd == "exit" or cmd == "quit":
                print("👋 Görüşmek üzere!")
                break
            elif cmd == "create":
                cmd_create()
            elif cmd.startswith("smart"):
                if len(cmd.split(maxsplit=1)) > 1:
                    request = cmd.split(maxsplit=1)[1]
                    smart_factory.build_from_request(request)
                else:
                    cmd_smart()
            elif cmd == "list":
                cmd_list()
            elif cmd == "help":
                cmd_help()
            else:
                print(f"❌ Bilinmeyen komut: {cmd}")
                print("   'help' yazarak komutları görün.")
        except KeyboardInterrupt:
            print("\n\n👋 Çıkış yapılıyor...")
            break
        except Exception as exc:
            print(f"❌ Hata: {exc}")


def main():
    """Ana fonksiyon."""
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "create":
            cmd_create()
        elif cmd == "smart":
            if len(sys.argv) > 2:
                request = " ".join(sys.argv[2:])
                smart_factory.build_from_request(request)
            else:
                cmd_smart()
        elif cmd == "list":
            cmd_list()
        elif cmd == "help":
            cmd_help()
        else:
            print(f"❌ Bilinmeyen komut: {cmd}")
            print("Kullanım: python main.py [create|smart|list|help]")
            sys.exit(1)
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
