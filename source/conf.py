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
nbsphinx_execute = 'always'  # Other options: 'never', 'auto'

# Optional: Set timeout for cell execution (in seconds)
nbsphinx_timeout = 300  # 5 minutes

# Optional: If you want to ignore notebook execution errors
nbsphinx_allow_errors = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
