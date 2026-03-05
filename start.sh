#!/bin/bash
# Emare Code - Quick Start
# Kurulum + İlk Çalıştırma

echo "💻 Emare Code - Quick Start"
echo ""

# Kurulum yap
if [ ! -d "venv" ]; then
    echo "▶️  Kurulum yapılıyor..."
    bash setup.sh
fi

# Aktive et
echo "▶️  Başlatılıyor..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Çalıştır
python main.py
