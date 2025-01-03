# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'Smart Mirror'
copyright = '2022, Filippos Zacharopoulos & Dimitris Papageorgiou'
author = 'Filippos Zacharopoulos & Dimitris Papageorgiou'

# The full version, including alpha/beta/rc tags
release = '0.7'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
    'm2r2',
    'sphinx.ext.githubpages'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# Default flags used by autodoc directives
autodoc_default_options = {
  'members': True,
  'inherited-members': True,
  'show-inheritance': True,
}

# Generate autodoc stubs with summaries from code
autosummary_generate = True

# Typehint Options
typehints_fully_qualified = True

source_suffix = ['.rst', '.md']

intersphinx_mapping = {
    'urllib3': ('http://urllib3.readthedocs.org/en/latest', None),
    'python': ('http://docs.python.org/3', None),
    'deap': ('https://deap.readthedocs.io/en/master/', None),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []