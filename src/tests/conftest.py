import sys
from pathlib import Path

# src/ zum sys.path hinzufügen
src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))
