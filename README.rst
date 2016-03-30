SetupTools-Tasks
================

This package augments setuptools commands with common tasks useful while developing and building python packages.
These tasks aim to replace the very common scripts that are copied in each repository and are run by developers before standard distutils commands.

Features
--------

- Building static resources. (Supports: "compass compile")


Design
------

- Use command line commands instead of using python packages. Example: ``subprocess.check_output("compass compile".split())`` over ``import libsass``. This is done for consistency and to prevent drawing large potentially unused dependecies.
- Support standard python packaging configuration (.cfg files)

Usage
-------

1. Only add new setuptools commands

Add setuptools-tasks to your setup_requires list and all commands will be available.

.. code-block:: python

    setup(
        name="your-package",
        ...
        setup_requires = ['setuptools-tasks'],
        )

New commands are available:

.. code-block:: console

   python setup.py build_static_files

To enable compiling for sass resources, add a ``setuptools-tasks`` section to your setup.cfg file with ``sass = True``

.. code-block:: guess

  [setuptools_tasks]
  sass = True

2. Override setuptools commands to add setuptools-tasks commands at the appropriate time.

To do this setuptools-tasks must be installed in the environment before running ``sdist``.
This will also build static files according to your configuration before the source distribution is built.

.. code-block:: console

  pip install setuptools-tasks
  python setup.py sdist
