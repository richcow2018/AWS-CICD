#!/bin/bash
set -e

echo "Preparing for installation..."
# Stop Odoo service
sudo /odoo/ctlscript.sh stop 

# Backup existing custom modules
timestamp=$(date +%Y%m%d_%H%M%S)
sudo mv /odoo/apps/odoo/lib/odoo-12.0.post20191018-py3.7.egg/odoo/addons/small_custom_addons /odoo/apps/odoo/lib/odoo-12.0.post20191018-py3.7.egg/odoo/addons/small_custom_addons_backup_$timestamp

echo "Preparation complete!"
