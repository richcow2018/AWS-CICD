#!/bin/bash
set -e

echo "Preparing deployment artifact..."
zip -r odoo_deployment.zip . -x "*.git*" "tests/*"

echo "Artifact prepared!"
