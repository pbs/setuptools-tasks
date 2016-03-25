from distutils import dist

from mock import patch, call, MagicMock

from setuptools_tasks.statics_building import (
    compile_static_files, compile_sass_files, get_sass_config_directories,
    BuildStaticFiles
)

from .utils import make_mock_distribution


@patch("setuptools_tasks.statics_building.compile_sass_files")
def test_sass_no_run(compile_sass):
    distribution = make_mock_distribution()
    compile_static_files(distribution)
    assert compile_sass.called == 0, "Sass compiling was called!"


@patch("setuptools_tasks.statics_building.compile_sass_files")
def test_sass_is_run(compile_sass):
    distribution = make_mock_distribution(config={"sass": (None, "True")})
    compile_static_files(distribution)
    assert compile_sass.call_args_list == [call({'sass': (None, 'True')})]


@patch("setuptools_tasks.statics_building.subprocess.check_output")
def test_sass_normal_run(mock_check_output):
    config = {"sass_directories": (None, "a,b/c")}
    compile_sass_files(config)
    expected_calls = [
        call(["compass", "-v"]),
        call(["compass", "compile", "a"]),
        call(["compass", "compile", "b/c"]),
    ]
    assert mock_check_output.call_args_list == expected_calls


@patch("setuptools_tasks.statics_building.os.walk")
def test_sass_dir_autodetect(mock_walk):
    mock_walk.return_value = [
        ("./.tox", ['a'], ('a.txt',)),
        ("./.tox/a", [], ('config.rb',)),
        ("./.git", [], ('config.rb',)),
        ("./normal", ['b', 'c'], ('run.rb',)),
        ("./normal/b", [], ('config.rb',)),
        ("./normal/c", [], ('config.rb',)),
    ]
    actual = get_sass_config_directories({})
    expected = ["./normal/b", "./normal/c"]
    assert actual == expected


@patch("setuptools_tasks.statics_building.compile_static_files")
def test_build_command_normal(mock_compile_static):
    mock_dist = MagicMock(spec=dist.Distribution)
    mock_dist.verbose = True
    build_command = BuildStaticFiles(mock_dist)
    build_command.run()

    assert mock_compile_static.call_count == 1
