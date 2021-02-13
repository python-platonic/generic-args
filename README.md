# generic-args

[![Build Status](https://github.com/python-platonic/generic-args/workflows/test/badge.svg?branch=master&event=push)](https://github.com/python-platonic/generic-args/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/python-platonic/generic-args/branch/master/graph/badge.svg)](https://codecov.io/gh/python-platonic/generic-args)
[![Python Version](https://img.shields.io/pypi/pyversions/generic-args.svg)](https://pypi.org/project/generic-args/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Given an instantiated generic class, retrieve the type arguments of itself or its parents.


## Features

- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)
- Add yours!


## Installation

```bash
pip install generic-args
```


## Example

Showcase how your project can be used:

```python
from generic_args.generic_args import some_function

print(some_function(3, 4))
# => 7
```

## License

[MIT](https://github.com/python-platonic/generic-args/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [54efe958f72ac06e912a1423aa14be8b149f988f](https://github.com/wemake-services/wemake-python-package/tree/54efe958f72ac06e912a1423aa14be8b149f988f). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/54efe958f72ac06e912a1423aa14be8b149f988f...master) since then.
