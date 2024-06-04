"""
Module xss_shield
=================
A Python library to prevent your website from being attacked.
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
    Please read `README.md`
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
