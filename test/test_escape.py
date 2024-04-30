from xss_shield import *


class Test_escape:
    def test_escape(self):
        unsafe_str = '<script>alert("Bad.");</script>'
        safe_str = escape(unsafe_str)
        expected = '&ampltscript&ampgtalert(&#34&#59Bad.&#34&#59)&#59&amplt/script&ampgt'
        assert safe_str == expected

