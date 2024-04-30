def escape(s: str) -> str:
    s = s.replace('<', '&lt')\
         .replace('>', '&gt')\
         .replace('&', '&amp')\
         .replace(' ', '-')\
         .replace("'", "&#39;")\
         .replace('"', "&#34;")\
         .replace(';', '&#59')
    
    return s
