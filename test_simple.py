#!/usr/bin/env python3
"""Simple template test"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from templates import get_template

print("Testing template system...")
code = get_template("python", "my_app")
print(f"✅ Generated {len(code)} characters")
print("\nCode preview:")
print("-" * 50)
print(code)
print("-" * 50)
