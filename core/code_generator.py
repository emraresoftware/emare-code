"""Emare Code — Code Generator Engine

Cross-platform kod üretimi ve yönetimi.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from core.provider_router import router as ai_router
from templates import get_template


class CodeGenerator:
    """Cross-platform kod üretici."""

    def __init__(self) -> None:
        load_dotenv()
        self.router = ai_router
        self._last_provider: Optional[str] = None

        if not self.router.available_providers:
            print("⚠️ UYARI: Hiçbir AI sağlayıcı yapılandırılmamış. Şablon modu aktif.")

    def generate_code(
        self,
        name: str,
        language: str,
        description: str,
        platform: str = "all",
    ) -> str:
        """AI ile kod üret."""
        if not self.router.available_providers:
            return get_template(language, name)

        platform_hints = {
            "linux": "Linux için pathlib ve POSIX komutları kullan",
            "macos": "macOS için pathlib ve POSIX komutları kullan",
            "windows": "Windows için pathlib ve platform-agnostic kod kullan",
            "all": "Linux, macOS ve Windows'ta çalışacak cross-platform kod yaz",
        }

        prompt = f"""
Sen Emare Code yazılım üretim asistanısın.
'{name}' adında bir {language} programı yazmanı istiyorum.

Görev: {description}
Platform: {platform_hints.get(platform, platform_hints['all'])}

KURALLAR:
1. Cross-platform uyumlu ol (pathlib, os.path kullan, hardcoded path yok)
2. Hata yönetimi ekle (try-except)
3. Temiz ve okunabilir kod
4. if __name__ == "__main__" bloğu ile çalıştırılabilir
5. Sadece çalışabilir kod ver, açıklama yapma
6. Platform kontrolü için platform.system() kullanabilirsin

Dil: {language}
"""

        result = self.router.generate(prompt)
        self._last_provider = result.provider

        if result.success:
            code = result.text
            # Markdown code block'larını temizle
            for marker in ["```python", "```javascript", "```go", "```rust", "```"]:
                code = code.replace(marker, "")
            code = code.strip()
            if code:
                return code

        print(f"  ⚠️ AI üretemedi, tip-bazlı şablon kullanılıyor.")
        return get_template(language, name)

    def create_project(
        self,
        name: str,
        language: str,
        description: str,
        platform: str = "all",
        output_dir: Optional[Path] = None,
    ) -> Path:
        """Tam bir proje oluştur."""
        if output_dir is None:
            output_dir = Path("./projects")

        project_path = output_dir / name
        project_path.mkdir(parents=True, exist_ok=True)

        providers_str = ", ".join(p.name for p in self.router.available_providers) or "yok"
        print(f"🧠 AI '{name}' için kod üretiyor... (sağlayıcılar: {providers_str})")

        code = self.generate_code(name, language, description, platform)

        # Dosya uzantısı belirle
        extensions = {
            "python": "py",
            "javascript": "js",
            "typescript": "ts",
            "go": "go",
            "rust": "rs",
            "php": "php",
            "bash": "sh",
        }
        ext = extensions.get(language.lower(), "txt")

        # Ana dosyayı yaz
        main_file = project_path / f"main.{ext}"
        main_file.write_text(code, encoding="utf-8")

        # Manifest oluştur
        manifest = {
            "name": name,
            "language": language,
            "description": description,
            "platform": platform,
            "version": "1.0.0",
            "created_at": datetime.utcnow().isoformat(),
            "provider": self._last_provider,
            "main_file": f"main.{ext}",
        }

        manifest_path = project_path / "manifest.json"
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        # README oluştur
        readme_content = f"""# {name}

**Dil:** {language}  
**Platform:** {platform}  
**Üretilme:** {datetime.utcnow().strftime("%Y-%m-%d")}  
**Sağlayıcı:** {self._last_provider or 'template'}

## Açıklama

{description}

## Kullanım

```bash
# Çalıştır
{self._get_run_command(language, f"main.{ext}")}
```

## Platform Notları

- ✅ Linux
- ✅ macOS  
- ✅ Windows

---

*Emare Code tarafından üretildi.*
"""
        readme_path = project_path / "README.md"
        readme_path.write_text(readme_content, encoding="utf-8")

        print(f"✅ Proje oluşturuldu: {project_path}")
        print(f"   📄 {main_file.name}")
        print(f"   📋 manifest.json")
        print(f"   📖 README.md")

        return project_path

    def _get_run_command(self, language: str, filename: str) -> str:
        """Dil için çalıştırma komutu döndür."""
        commands = {
            "python": f"python {filename}",
            "javascript": f"node {filename}",
            "typescript": f"ts-node {filename}",
            "go": f"go run {filename}",
            "rust": f"rustc {filename} && ./main",
            "php": f"php {filename}",
            "bash": f"bash {filename}",
        }
        return commands.get(language.lower(), f"# {filename} dosyasını çalıştır")


generator = CodeGenerator()
