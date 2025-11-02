#!/usr/bin/env bash
set -e # Stop on first error

# --- CONFIGURATION ---
PYTHON_BIN="python3"
VENV_DIR=".venv"
SRC_DIR="src"

# --- CHECK PYTHON INSTALLATION ---
if ! command -v $PYTHON_BIN &>/dev/null; then
  echo "❌ Python is not installed or not found in PATH."
  echo "Please install Python 3 before running this script."
  exit 1
fi

# --- CREATE VIRTUAL ENVIRONMENT ---
if [ ! -d "$VENV_DIR" ]; then
  echo "🔧 Creating virtual environment in $VENV_DIR..."
  $PYTHON_BIN -m venv "$VENV_DIR"
else
  echo "✅ Virtual environment already exists: $VENV_DIR"
fi

# --- ACTIVATE VIRTUAL ENVIRONMENT ---
echo "🔁 Activating virtual environment..."
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

# --- UPGRADE PIP ---
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# --- FIND AND INSTALL REQUIREMENTS ---
echo "📦 Searching for requirements.txt files in $SRC_DIR..."
REQ_FILES=$(find "$SRC_DIR" -type f -name "requirements.txt")

if [ -z "$REQ_FILES" ]; then
  echo "⚠️  No requirements.txt files found under $SRC_DIR."
else
  for req in $REQ_FILES; do
    echo "📥 Installing dependencies from: $req"
    pip install -r "$req"
  done
fi

# --- DONE ---
echo "✅ Environment setup complete."
echo "To activate manually later, run:"
echo "   source $VENV_DIR/bin/activate"
