#!/usr/bin/env python3
"""Full project generation test"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from core.code_generator import generator

print("=" * 60)
print("🚀 EMARE CODE - PROJECT GENERATION TEST")
print("=" * 60)

# Test: Generate a Python backup tool
print("\n📦 Generating: Python File Backup Tool")
print("-" * 60)

try:
    project_path = generator.create_project(
        name="file_backup_tool",
        language="python",
        description="Cross-platform file backup tool with compression support",
        platform="all"
    )
    
    print(f"\n✅ SUCCESS!")
    print(f"📁 Project created at: {project_path}")
    print(f"\n📄 Generated files:")
    
    for item in sorted(project_path.rglob("*")):
        if item.is_file():
            size = item.stat().st_size
            rel_path = item.relative_to(project_path)
            print(f"   {rel_path} ({size} bytes)")
    
    # Show main.py preview
    main_file = project_path / "main.py"
    if main_file.exists():
        content = main_file.read_text()
        print(f"\n📝 main.py preview (first 500 chars):")
        print("-" * 60)
        print(content[:500])
        print("...")
        print("-" * 60)
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
