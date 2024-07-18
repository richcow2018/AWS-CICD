#!/bin/bash
set -e

echo "Running SAST scan..."
bandit -r . -f custom

echo "Running SCA..."
safety check -r requirements.txt

echo "Security scans complete!"
