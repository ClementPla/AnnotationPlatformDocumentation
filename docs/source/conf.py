# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme
# -- Project information -----------------------------------------------------
project = 'Retinal Annotations Platform Documentation'
copyright = '2020, Clément Playout'
author = 'Clément Playout'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel',
              "sphinx_rtd_theme"
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
image_height = 24
rst_prolog = '''
.. |brushTool| image:: /images/brush_tool.png
  :height: {0}
  :alt: Brush tool icon
  
.. |fillTool| image:: /images/fill_tool.png
  :height: {0}
  :alt: Fill tool icon

.. |eraserTool| image:: /images/eraser_tool.png
  :height: {0}
  :alt: Eraser tool icon

.. |lassoEraserTool| image:: /images/lasso_eraser_tool.png
  :height: {0}
  :alt: Lasso eraser tool icon
  
.. |panTool| image:: /images/pan_tool.png
  :height: {0}
  :alt: Pan tool icon

.. |pickTool| image:: /images/pick_tool.png
  :height: {0}
  :alt: Pick tool icon

.. |undo| image:: /images/undo.png
  :height: {0}
  :alt: Undo icon
  
.. |visibility| image:: /images/visibility_mode.png
  :height: {0}
  :alt: Visibility icon

.. |wireframe| image:: /images/wireframe_mode.png
  :height: {0}
  :alt: Wireframe icon

.. |opacity| image:: /images/opacity_option.png
  :width: {0}
  :alt: Opacity icon

.. |mouseRight| image:: /images/right_mouse_click.png
  :height: {0}
  :alt: Right Mouse Click icon

.. |centerMouseClick| image:: /images/center_mouse_click.png
  :height: {0}
  :alt: Center Mouse Click icon

.. |centerMouseWheel| image:: /images/mouse_wheel.png
  :height: {0}
  :alt: Center Mouse Wheel icon
  
.. |redo| image:: /images/redo.png
  :height: {0}
  :alt: Redo icon

.. |submit| image:: /images/submit.png
  :height: {0}
  :alt: Submit button icon

.. |preprocessing| image:: /images/preprocessing.png
  :height: {0}
  :alt: Preprocessing icon

.. |flip| image:: /images/flip.png
  :height: {0}
  :alt: Flip icon

.. |browse| image:: /images/browseImage.png
  :height: {0}
  :alt: Browse Image icon

.. |bug_report| image:: /images/bug_report.png
  :height: {0}
  :alt: Bug Report icon

.. |hierarchical_mode| image:: /images/hierarchicalMode.png
  :height: {0}
  :alt: Hierarchical Mode icon
'''.format(str(image_height))
# -- Options for HTML output -------------------------------------------------
master_doc = 'index'
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = "sphinx_rtd_theme"
html_theme = "bootstrap"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
