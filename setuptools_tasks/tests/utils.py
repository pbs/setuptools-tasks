from distutils import dist

from mock import MagicMock


def make_mock_distribution(config=None, verbose=True):
    mock_dist = MagicMock(spec=dist.Distribution)
    mock_dist.verbose = verbose
    full_config = {'sdist': {}, 'aliases': {}}
    if config:
        full_config['setuptools_tasks'] = config
    mock_dist.command_options = full_config
    return mock_dist
