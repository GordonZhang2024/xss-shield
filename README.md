# xss-shield
A Python library to prevent your website from being attacked.

[PyPI](https://pypi.org/project/xss-shield/)

![PyPI - Downloads](https://img.shields.io/pypi/dd/xss-shield)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/xss-shield)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/xss-shield)
![GitHub top language](https://img.shields.io/github/languages/top/GordonZhang2024/xss-shield)

## Installing
Type command:
```bash
$ pip install xss-shield
```

## Usage
example:
```python
import xss_shield

unsafe_str = '<script>alert("Bad.");</script>'
safe_str = xss_shield.escape(unsafe_str)
```
