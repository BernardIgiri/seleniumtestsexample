#!/bin/bash
python3 -m http.server webapp &;
pytest test.py --verbose --capture=no;
