import setuptools.command.sdist as orig

from setuptools_tasks.statics_building import compile_static_files


class sdist(orig.sdist):

    def run(self):
        compile_static_files(self.distribution)
        orig.sdist.run(self)
