# -*- coding: utf-8 -*-


def test_parameters(testdir):
    test_config = """
    param1 = range(10)
    param2 = ['a', 'b', 'c']
    even_values = [v for v in range(20) if v % 2 == 0]
    """

    test_example = """
    import pytest
    from tytest.config.runtime_settings import Config as C

    pytest_plugins = "pytester"

    @pytest.mark.parametrize('param1', C.param1)
    @pytest.mark.parametrize('param2', C.param2)
    @pytest.mark.parametrize('param3', C.even_values)
    def test_1(param1, param2, param3):
        pass
    """

    testdir.makepyfile(__init__="")
    testdir.makepyfile(runconfig=test_config)
    testdir.makepyfile(test_example)
    result = testdir.runpytest("--runconfig", "runconfig.py")
    assert len(result.errlines) == 0
