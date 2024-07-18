#!/bin/bash
set -e

echo "Building Odoo custom modules..."
# Assuming your custom modules are in a directory named 'custom_addons'
zip -r small_custom_module.zip /odoo/apps/odoo/lib/odoo-12.0.post20191018-py3.7.egg/odoo/addons

echo "Build complete!"
