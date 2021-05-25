#!/bin/bash
cd /home/dsl && PYTHONDONTWRITEBYTECODE=1 coverage run -m unittest discover -p 'Test*.py' tests/ && coverage html
cd /home/dsl/src && PYTHONDONTWRITEBYTECODE=1 python3 main.py