from pathlib import Path

NODE_MODULES_DIR = Path(__file__).resolve().parent.parent.parent
print(NODE_MODULES_DIR)