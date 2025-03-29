import unittest
from main import is_valid_ipv4, find_ips_in_text
class TestIPv4Functions(unittest.TestCase):
    def test_is_valid_ipv4(self):
        self.assertTrue(is_valid_ipv4("192.168.1.1"))
        self.assertTrue(is_valid_ipv4("255.255.255.255"))
        self.assertFalse(is_valid_ipv4("256.100.50.25"))
        self.assertFalse(is_valid_ipv4("192.168.1"))
        self.assertFalse(is_valid_ipv4("abc.def.ghi.jkl"))

    def test_find_ips_in_text(self):
        text = "Valid IPs: 192.168.0.1, 8.8.8.8. Invalid: 300.168.0.1, 256.256.256.256"
        self.assertEqual(find_ips_in_text(text), ["192.168.0.1", "8.8.8.8"])

    def test_find_ips_in_url(self):
        url = "https://example.com"
        # Здесь можно замокать requests.get для тестирования

if __name__ == "__main__":
    unittest.main()