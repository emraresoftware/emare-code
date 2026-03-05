"""Emare Code — Smart Factory

Doğal dil ile çoklu proje üretimi.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Optional

from core.provider_router import ProviderRouter, router as default_router


class SmartFactory:
    """Doğal dil komutlarından proje üretir."""

    def __init__(self, router: Optional[ProviderRouter] = None) -> None:
        self.router = router or default_router

    def analyze_request(self, natural_language: str) -> list[dict]:
        """Doğal dil isteğini analiz edip proje planı çıkar."""
        prompt = f"""Sen bir yazılım mimarısın. Aşağıdaki isteği analiz et ve
gerekli projelerin listesini JSON dizisi olarak ver.

Her proje için:
- name: snake_case proje adı
- language: python | javascript | go | rust | php | bash
- description: Kısa görev açıklaması
- platform: linux | macos | windows | all

İstek: {natural_language}

SADECE JSON dizisi yaz, başka hiçbir şey yazma. Örnek format:
[{{"name":"x","language":"y","description":"z","platform":"all"}}]

JSON:"""

        result = self.router.generate(prompt)
        if not result.success:
            # Fallback: tek proje olarak yorumla
            safe_name = re.sub(r'[^a-z0-9_]', '_', natural_language.lower()[:30])
            return [{
                "name": safe_name,
                "language": "python",
                "description": natural_language,
                "platform": "all",
            }]

        try:
            text = result.text.strip()
            # JSON bloğunu çıkar
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip()

            projects = json.loads(text)
            if isinstance(projects, dict):
                projects = [projects]
            return projects
        except (json.JSONDecodeError, IndexError):
            safe_name = re.sub(r'[^a-z0-9_]', '_', natural_language.lower()[:30])
            return [{
                "name": safe_name,
                "language": "python",
                "description": natural_language,
                "platform": "all",
            }]

    def build_from_request(self, natural_language: str) -> list[dict]:
        """Doğal dil isteğinden projeleri üret."""
        from core.code_generator import generator

        print(f"🧠 İstek analiz ediliyor: \"{natural_language[:60]}...\"")
        plan = self.analyze_request(natural_language)
        print(f"📐 Plan: {len(plan)} proje üretilecek\n")

        results = []
        for i, proj in enumerate(plan, 1):
            name = proj.get("name", f"project_{i}")
            lang = proj.get("language", "python")
            desc = proj.get("description", "")
            platform = proj.get("platform", "all")

            print(f"  [{i}/{len(plan)}] {name} ({lang} - {platform})")

            try:
                project_path = generator.create_project(name, lang, desc, platform)
                results.append({
                    "name": name,
                    "status": "created",
                    "path": str(project_path)
                })
            except Exception as exc:
                results.append({
                    "name": name,
                    "status": "failed",
                    "error": str(exc)
                })
                print(f"    ❌ Hata: {exc}")

        print(f"\n✅ {sum(1 for r in results if r['status'] == 'created')}/{len(results)} proje üretildi.")
        return results


smart_factory = SmartFactory()
