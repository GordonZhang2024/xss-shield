def escape(s: str) -> str:
    s = s.replace(';', '&#59;')\
         .replace('<', '&lt;')\
         .replace('>', '&gt;')\
         .replace(' ', '-')\
         .replace("'", "&#39;")\
         .replace('"', "&#34;")\
         .replace('/', '&#47;')\
    
    return s
