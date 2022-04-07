# -*- coding: utf-8 -*-
import importlib
import os
import pytest
import sys
from .runtime_settings import Config, Settings


def pytest_addoption(parser):
    group = parser.getgroup('tytest')
    group.addoption(
        '--runconfig',
        dest='runconfig',
        help='Test parameters script')


@pytest.fixture
def runconfig(request):
    return request.config.option.runconfig


def pytest_configure(config):
    # import runtime configuration module
    # and store its contents in
    # tytest.config.runtime_settings.Config class
    file_name = config.getoption('runconfig')
    if file_name and os.path.isfile(file_name):
        Settings.RUN_CONFIG = file_name
        dirname, basename = os.path.split(os.path.abspath(file_name))
        sys.path.append(dirname)
        if basename.endswith('.py'):
            module_name = os.path.splitext(basename)[0]
        else:
            module_name = file_name
        importlib.invalidate_caches()
        module = importlib.import_module(module_name)
        if module:
            for key, value in module.__dict__.items():
                if not key.startswith('_'):
                    setattr(Config, key, value)
