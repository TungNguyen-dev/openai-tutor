#!/usr/bin/env bash
set -e  # Stop on first error

# --- CONFIGURATION ---
PYTHON_BIN="python3"
SRC_DIR="src"

# --- CHECK PYTHON INSTALLATION ---
if ! command -v "$PYTHON_BIN" &>/dev/null; then
  echo "❌ Python is not installed or not found in PATH."
  echo "Please install Python 3 before running this script."
  exit 1
fi

# --- FIND AND INSTALL REQUIREMENTS ---
echo "📦 Searching for requirements.txt files in $SRC_DIR..."
REQ_FILES=$(find "$SRC_DIR" -type f -name "requirements.txt")

if [ -z "$REQ_FILES" ]; then
  echo "⚠️  No requirements.txt files found under $SRC_DIR."
else
  for req in $REQ_FILES; do
    REQ_DIR=$(dirname "$req")
    VENV_DIR="$REQ_DIR/.venv"

    echo "📂 Processing: $REQ_DIR"
    echo "🔧 Creating virtual environment: $VENV_DIR"
    "$PYTHON_BIN" -m venv "$VENV_DIR"

    echo "🔁 Activating virtual environment..."
    # shellcheck disable=SC1091
    source "$VENV_DIR/bin/activate"

    echo "⬆️  Upgrading pip..."
    pip install --upgrade pip

    echo "📥 Installing dependencies from: $req"
    (
      cd "$REQ_DIR"
      pip install -r "requirements.txt"
    )

    deactivate
    echo "✅ Done: $REQ_DIR"
    echo
  done
fi

# --- DONE ---
echo "🎉 All environments set up successfully."
echo "To activate one manually, run:"
echo "   source path/to/module/.venv/bin/activate"
