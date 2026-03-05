"""Kod şablonları — Hazır template'ler.

AI kullanılamadığında bu şablonlar kullanılır.
"""

TEMPLATES = {
    "python": '''"""Emare Code Project — {name}"""
import platform
import sys
from pathlib import Path


def main():
    """Ana fonksiyon."""
    print(f"🚀 {name} çalışıyor...")
    print(f"Platform: {{platform.system()}} {{platform.release()}}")
    print(f"Python: {{sys.version}}")
    
    # TODO: Proje mantığı buraya
    

if __name__ == "__main__":
    main()
''',

    "javascript": '''// Emare Code Project — {name}
const os = require('os');

function main() {{
    console.log('🚀 {name} çalışıyor...');
    console.log(`Platform: ${{os.platform()}} ${{os.release()}}`);
    console.log(`Node: ${{process.version}}`);
    
    // TODO: Proje mantığı buraya
}}

main();
''',

    "go": '''package main

import (
    "fmt"
    "runtime"
)

func main() {{
    fmt.Println("🚀 {name} çalışıyor...")
    fmt.Printf("Platform: %s %s\\n", runtime.GOOS, runtime.GOARCH)
    fmt.Printf("Go: %s\\n", runtime.Version())
    
    // TODO: Proje mantığı buraya
}}
''',

    "rust": '''// Emare Code Project — {name}

fn main() {{
    println!("🚀 {name} çalışıyor...");
    println!("Platform: {{}}", std::env::consts::OS);
    
    // TODO: Proje mantığı buraya
}}
''',

    "php": '''<?php
// Emare Code Project — {name}

function main() {{
    echo "🚀 {name} çalışıyor...\\n";
    echo "Platform: " . PHP_OS . "\\n";
    echo "PHP: " . PHP_VERSION . "\\n";
    
    // TODO: Proje mantığı buraya
}}

main();
''',

    "bash": '''#!/bin/bash
# Emare Code Project — {name}

echo "🚀 {name} çalışıyor..."
echo "Platform: $(uname -s)"
echo "Shell: $SHELL"

# TODO: Proje mantığı buraya
''',
}


def get_template(language: str, project_name: str) -> str:
    """Dile göre şablon kodu döndür."""
    template = TEMPLATES.get(language.lower(), TEMPLATES["python"])
    return template.format(name=project_name)
