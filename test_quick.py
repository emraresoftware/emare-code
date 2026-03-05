#!/usr/bin/env python3
"""Emare Code - Quick Test"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from core.code_generator import generator

print("=" * 50)
print("🧪 EMARE CODE - QUICK TEST")
print("=" * 50)

# Test 1: AI Router
print("\n1️⃣  AI Router Test")
print(f"   Providers: {len(generator.router.available_providers)}")
for p in generator.router.available_providers:
    print(f"   ✅ {p.name} ({p.model})")

# Test 2: Template System
print("\n2️⃣  Template System Test")
from templates import get_template
code = get_template("python", "test_app")
print(f"   ✅ Template works ({len(code)} chars)")
print(f"   Preview: {code[:100]}...")

# Test 3: Simple Project Generation
print("\n3️⃣  Project Generation Test")
try:
    project_path = generator.create_project(
        name="hello_world",
        language="python",
        description="Simple hello world application",
        platform="all"
    )
    print(f"   ✅ Project created: {project_path}")
    
    # List generated files
    files = list(project_path.glob("*"))
    print(f"   📁 Files generated:")
    for f in files:
        print(f"      - {f.name}")
    
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("✅ Test completed!")
print("=" * 50)
