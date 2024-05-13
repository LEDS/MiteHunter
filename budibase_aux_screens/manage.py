#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def manage():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budibase_aux_screens.budibase_aux_screens.settings')

    # Adiciona o diretório raiz do projeto ao PYTHONPATH
    root_project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(root_project_path)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)