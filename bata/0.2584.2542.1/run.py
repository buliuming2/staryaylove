#!/usr/bin/env python3
import sys
import os

# 将项目根目录加入路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine.main import main

if __name__ == "__main__":
    main()