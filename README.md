# pytest-typhoon-config
A pytest plugin that facilitates test parameter configuration at runtime

## Features

* specify test parameters in a python module, just like any other
* choose which module to use at runtime

This way you can define different parameter sets for the same test suite and
choose them at runtime.

## Requirements

* pytest 6+

## Installation

You can install `pytest-typhoon-config` via `pip`:

```
pip install pytest-typhoon-config
```

## Usage

Create a test parameter definition file as a Python module, such as this:

```
# myparams.py
import numpy as np

a_list = [277.0, 278.0]
a_numpy_range = np.arange(58, 63, 0.2)
even_values = [v for v in range(20) if v % 2 == 0]

class StayConnected:
    some_list = [22, 45, 85, 95]
    some_param = 0.95
```

All module attributes will be injected at runtime in
`tytest.config.runtime_settings.Config` class. They will be available as
class-level attributes of `Config`. That means you can use them
like this:

```
from tytest.runtime_settings import Config as C

@python.mark.parametrize('param1', C.even_values)
def test_something(param1):
    pass
```

In this example `even_values` variable will be initialized in `myparams.py`
module, and then injected into `Config` class. It is available in all test
code as `Config.even_values`.

This way you can create different python modules with the same variables,
having different values, and then choose which module to use when invoking
pytest. For example:

```
pytest --runconfig=myparams.py
```

The path of this file is evaluated at runtime.

## Contributions

Contributions are very welcome. Tests can be run with `tox`, please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the MIT license, `pytest-typhoon-config` is
free and open source software.
