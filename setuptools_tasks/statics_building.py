from __future__ import print_function, unicode_literals

import subprocess
import os
from distutils import log
from distutils.core import Command

from .utils import get_from_config


IGNORED_DIRECTORIES = [".git", ".tox", "build"]


def get_sass_config_directories(config):
    log.info("Auto detecting sass configuration files.")
    ignored_dirs = get_from_config(
        config, "sass_ignored_dirs", IGNORED_DIRECTORIES, lambda x: x.split(','))
    ignored_dirs = ["./{}".format(directory) for directory in ignored_dirs]

    def _is_ignored_dir(directory):
        for ignored_dir in ignored_dirs:
            if directory.startswith(ignored_dir):
                return True
        return False

    config_directories = []
    for root, dirs, files in os.walk(".", topdown=True):
        if _is_ignored_dir(root):
            dirs[:] = []
            continue
        if "config.rb" in files:
            config_directories.append(root)
    log.info("Found directories {}".format(config_directories))
    return config_directories


def compile_sass_files(config):
    log.info("Compiling sass resources")
    directories = (get_from_config(config, "sass_directories", None, lambda x: x.split(',')) or
                   get_sass_config_directories(config))
    version_output = subprocess.check_output("compass -v".split())
    log.debug(version_output)

    for directory in directories:
        log.info("Compiling sass resources in {}".format(directory))
        command = "compass compile {}".format(directory).split()
        try:
            output = subprocess.check_output(command)
            log.info(output)
        except subprocess.CalledProcessError:
            log.error("Compass compile returned non-zero error code!")
            raise


def compile_static_files(distribution):
    config = distribution.command_options.get("setuptools_tasks", {})
    compile_sass = get_from_config(config, "sass", "False")
    if compile_sass == "True":
        compile_sass_files(config)


class BuildStaticFiles(Command):
    """
    Builds all the static files.
    """

    description = ("Build all the static files required by the application. "
                   "Command options can be configured in .cfg files.")

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        compile_static_files(self.distribution)
