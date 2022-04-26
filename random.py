import sys
from pathlib import Path
sys.path.remove(str(Path(__file__).resolve().parent))

import random

print(random.randint(1, 10))
