from distutils import dist

from mock import patch, MagicMock

from setuptools_tasks.sdist import sdist as custom_sdist


@patch("setuptools_tasks.sdist.compile_static_files")
@patch("setuptools_tasks.sdist.orig")
def test_sdist_normal_run(mock_orig_sdist, mock_compile_static):
    mock_dist = MagicMock(spec=dist.Distribution)
    mock_dist.verbose = True
    sdist_command = custom_sdist(mock_dist)
    sdist_command.run()

    assert mock_orig_sdist.sdist.run.call_count == 1
    assert mock_compile_static.call_count == 1
