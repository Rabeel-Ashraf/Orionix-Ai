#!/bin/bash

# Orionix AI Complete Setup Script
echo "🚀 Starting Orionix AI Project Setup..."
echo "========================================"

# Create directory structure
echo "Creating directory structure..."
mkdir -p app/core app/api/v1/endpoints app/models app/schemas app/utils tests alembic/versions logs

# Create __init__.py files
echo "Creating __init__.py files..."
touch app/__init__.py app/core/__init__.py app/api/__init__.py app/api/v1/__init__.py
touch app/api/v1/endpoints/__init__.py app/models/__init__.py app/schemas/__init__.py app/utils/__init__.py
touch tests/__init__.py alembic/__init__.py

echo "✅ Directory structure created!"
