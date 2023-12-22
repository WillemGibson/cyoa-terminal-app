#!/bin/bash
cd "$(dirname "$0")"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "#!/bin/bash"
echo "cd '$(dirname "$0")'"
echo "source .venv/bin/activate" 
echo "python main.py"