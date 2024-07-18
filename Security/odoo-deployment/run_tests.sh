#!/bin/bash
set -e

echo "Running Odoo unit tests..."
python3 /opt/bitnami/odoo/odoo-bin -c /opt/bitnami/odoo/conf/odoo.conf -d test_db --test-enable --stop-after-init --modules=small_custom_module

echo "All tests passed!"
