# xss-shield
A Python library to prevent your website from being attacked

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
