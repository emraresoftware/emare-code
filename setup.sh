#!/bin/bash
# Emare Code - Quick Setup Script
# Usage: bash setup.sh

set -e

echo "╔════════════════════════════════════════════╗"
echo "║    💻 EMARE CODE - QUICK SETUP            ║"
echo "╚════════════════════════════════════════════╝"
echo ""

# Detect OS
OS="$(uname -s)"
case "${OS}" in
    Linux*)     PLATFORM=Linux;;
    Darwin*)    PLATFORM=macOS;;
    CYGWIN*)    PLATFORM=Windows;;
    MINGW*)     PLATFORM=Windows;;
    *)          PLATFORM="Unknown:${OS}"
esac

echo "🖥️  Platform: $PLATFORM"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 bulunamadı. Lütfen Python 3.9+ yükleyin."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python: $PYTHON_VERSION"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Virtual environment oluşturuluyor..."
    python3 -m venv venv
    echo "✅ Virtual environment oluşturuldu"
else
    echo "✅ Virtual environment mevcut"
fi

# Activate virtual environment
echo "🔌 Virtual environment aktive ediliyor..."
if [ "$PLATFORM" = "Windows" ]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install dependencies
echo "📥 Dependencies yükleniyor..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "✅ Dependencies yüklendi"

# Create .env if not exists
if [ ! -f ".env" ]; then
    echo "⚙️  .env dosyası oluşturuluyor..."
    cp .env.example .env
    echo "✅ .env oluşturuldu (API anahtarlarını düzenlemeyi unutma!)"
else
    echo "✅ .env mevcut"
fi

# Create projects directory
if [ ! -d "projects" ]; then
    mkdir projects
    echo "✅ projects/ klasörü oluşturuldu"
fi

# Create data directory
if [ ! -d "data" ]; then
    mkdir -p data
    echo "✅ data/ klasörü oluşturuldu"
fi

echo ""
echo "╔════════════════════════════════════════════╗"
echo "║         ✅ KURULUM TAMAMLANDI             ║"
echo "╚════════════════════════════════════════════╝"
echo ""
echo "📝 Sonraki adımlar:"
echo ""
echo "1. .env dosyasını düzenle:"
echo "   nano .env"
echo "   (GOOGLE_API_KEY ekle)"
echo ""
echo "2. Virtual environment'ı aktive et:"
if [ "$PLATFORM" = "Windows" ]; then
    echo "   venv\\Scripts\\activate"
else
    echo "   source venv/bin/activate"
fi
echo ""
echo "3. Emare Code'u çalıştır:"
echo "   python main.py"
echo ""
echo "4. Yardım için:"
echo "   python main.py help"
echo ""
echo "🚀 Hazırsın! Cross-platform kod üretmeye başlayabilirsin."
