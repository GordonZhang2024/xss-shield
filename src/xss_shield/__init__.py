"""
Module xss_shield
=================
A Python library to prevent your website from being attacked.
"""

"""
License: MIT License
====================

Copyright (c) 2024 Gordon Zhang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


def escape(s: str, strict=True) -> str:
    """
    Function escape()
    =================
    Replace unsafe characters.

    Usage
    =====
    ```python
    escape('unsafe string') # This will replace all unsafe characters.
    escape('unsafe string') # This will only replace the `<script>` tag.
    ```

    More info
    =========
    Please read our docs at http://xss-shield.readthedocs.io/
    """
    if strict:
        s = (
            s.replace(';', '&#59;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace(' ', '-')
            .replace("'", "&#39;")
            .replace('"', "&#34;")
            .replace('/', '&#47;')
        )
    else:
        s = s.replace('<script>', '').replace('</script>', '')

    return s
