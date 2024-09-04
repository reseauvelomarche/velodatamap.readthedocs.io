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
    'sphinx_new_tab_link',
    'sphinx_last_updated_by_git',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'style_nav_header_background' : '#223F82',
    'body_max_width' : 'none',
}

html_logo = 'images/logo_velodatamap.png'

html_last_updated_fmt = '%d %B %Y'

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "sig-veloterritoires", # Username
    "github_repo": "velodatamap.readthedocs.io", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/docs/source/", # Path in the checkout to the docs root
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
