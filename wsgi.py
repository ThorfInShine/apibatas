#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

# Add project directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Set environment variables
os.environ['FLASK_ENV'] = 'production'
os.environ['DEPLOYED'] = 'true'

# Import and configure app
from app import app as application

if __name__ == "__main__":
    application.run()