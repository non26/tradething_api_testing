import os
import sys
from dotenv import load_dotenv

load_dotenv()
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
