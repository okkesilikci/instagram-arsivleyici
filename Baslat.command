#!/bin/bash
cd "$(dirname "$0")"
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 bulunamadı. python.org üzerinden Python 3 kur."
  read -p "Çıkmak için Enter..."
  exit 1
fi
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
open http://127.0.0.1:5050
python app.py
