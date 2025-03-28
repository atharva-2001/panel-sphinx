# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tardis'
copyright = '2025, atharva'
author = 'atharva'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
]

templates_path = ['_templates']
exclude_patterns = []

# Execute notebooks during docs build
import os
os.makedirs('_static', exist_ok=True)
nbsphinx_execute = 'auto'  # 'always' can cause timeouts, 'auto' is more robust

# Optional: Set timeout for cell execution (in seconds)
nbsphinx_timeout = 600  # Increase timeout to 10 minutes

# Optional: If you want to ignore notebook execution errors
nbsphinx_allow_errors = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
