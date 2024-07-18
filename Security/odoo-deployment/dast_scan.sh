#!/bin/bash
set -e

echo "Running DAST scan..."
# Using OWASP ZAP as an example
docker run -t owasp/zap2docker-stable zap-baseline.py -t http://127.0.0.1:8080 -r dast_report.html

echo "DAST scan complete!"
