#!/bin/bash
set -e

echo "Running Odoo unit tests..."
python3 /odoo/apps/odoo/bin/odoo-bin -c /odoo/apps/odoo/conf/odoo-server.conf -d test_db --test-enable --stop-after-init --modules=small_custom_module

echo "All tests passed!"
