# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Velodatamap'
copyright = '2024, Vélo & Territoires'
author = '@IdrissaD'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_design',
    'sphinx.ext.autosectionlabel',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'style_nav_header_background' : '#223F82'
}

html_logo = 'images/logo_velodatamap.png'

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "sig-veloterritoires", # Username
    "github_repo": "velodatamap.readthedocs.io", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/docs/source/", # Path in the checkout to the docs root
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
