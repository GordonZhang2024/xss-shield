# xss-shield
**xss-shield** is a python library which is used to stop your website from being attacked.

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