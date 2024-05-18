def escape(s: str, strict=True) -> str:
    if strict:
        s = s.replace(';', '&#59;')\
             .replace('<', '&lt;')\
             .replace('>', '&gt;')\
             .replace(' ', '-')\
             .replace("'", "&#39;")\
             .replace('"', "&#34;")\
             .replace('/', '&#47;')
    else:
        s = s.replace('<script>', '')\
             .replace('</script>', '')
    return s
