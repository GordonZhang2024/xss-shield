import xss_shield

class TestPreview:
    def test_escape(self):
        unsafe_str = '<script>alert("Bad."</script>'
        safe_str   = xss_shield.escape(unsafe_str)

        assert '<' not in safe_str

