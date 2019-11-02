import unittest
import bencode_open


class TestParser(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(bencode_open.loads(b"i17e"), 17)
        self.assertEqual(bencode_open.loads(b"i-17e"), -17)
        self.assertEqual(bencode_open.loads(b"i0e"), 0)
        with self.assertRaises(ValueError):
            bencode_open.loads(b"ie")
        with self.assertRaises(ValueError):
            bencode_open.loads(b"i-e")
        with self.assertRaises(ValueError):
            bencode_open.loads(b"i5hello3e")
        with self.assertRaises(ValueError):
            bencode_open.loads(b"i5")


    def test_string(self):
        self.assertEqual(bencode_open.loads(b"3:abc"), b"abc")
        self.assertEqual(bencode_open.loads(b"0:"), b"")
        self.assertEqual(bencode_open.loads(b"15:" + b"s" * 15), b"s" * 15)
        with self.assertRaises(ValueError):
            bencode_open.loads(b"3:a")
        with self.assertRaises(ValueError):
            bencode_open.loads(b"0:abc")
        with self.assertRaises(ValueError):
            bencode_open.loads(b"3abc")
        with self.assertRaises(ValueError):
            bencode_open.loads(b":abc")


    def test_list(self):
        self.assertEqual(bencode_open.loads(b"le"), [])
        self.assertEqual(bencode_open.loads(b"li17ee"), [17])
        self.assertEqual(bencode_open.loads(b"li-23ei17ee"), [-23, 17])
        self.assertEqual(bencode_open.loads(b"li17e3:abce"), [17, b"abc"])
        with self.assertRaises(ValueError):
            bencode_open.loads(b"l")
        with self.assertRaises(ValueError):
            bencode_open.loads(b"lholae")
        with self.assertRaises(ValueError):
            bencode_open.loads(b"l3:abc")


    def test_dict(self):
        self.assertEqual(bencode_open.loads(b"de"), {})
        self.assertEqual(bencode_open.loads(b"d3:abci17ee"), {b"abc": 17})
        self.assertEqual(bencode_open.loads(b"d1:ai-23e2:abi17ee"), {b"a": -23, b"ab": 17})
        self.assertEqual(bencode_open.loads(b"d1:ai17e1:z3:abce"), {b"a": 17, b"z": b"abc"})
        with self.assertRaises(ValueError):
            bencode_open.loads(b"d")
        with self.assertRaises(ValueError):
            bencode_open.loads(b"di17ei1ee")


    def test_edge_cases(self):
        with self.assertRaises(ValueError):
            bencode_open.loads(b"dee")
        with self.assertRaises(ValueError):
            bencode_open.loads(b"i1e3:abc")


class TestConverter(unittest.TestCase):
    def test_simple(self):
        for v in (
            17, -17, 0, # Integers
            b"abc", b"", b"s" * 15, # Strings
            [], [17], [-23, 17], [17, b"abc"], # Lists, mixed type lists
            {}, {b"abc": 17}, {b"a": -23, b"ab": 17}, {b"a": 17, b"z": b"abc"} # Dicts
        ):
            self.assertEqual(bencode_open.loads(bencode_open.dumps(v)), v)


    def test_dict_order(self):
        self.assertEqual(bencode_open.dumps({b"a": 1, b"b": 2}), b"d1:ai1e1:bi2ee")
        self.assertEqual(bencode_open.dumps({b"b": 1, b"a": 2}), b"d1:ai2e1:bi1ee")


    def test_types(self):
        with self.assertRaises(ValueError):
            bencode_open.dumps(13.7)
        with self.assertRaises(ValueError):
            bencode_open.dumps(11.0)
        with self.assertRaises(ValueError):
            bencode_open.dumps("str")
        with self.assertRaises(ValueError):
            bencode_open.dumps(None)
        with self.assertRaises(ValueError):
            bencode_open.dumps({1: b"bytes"})


if __name__ == "__main__":
    unittest.main()
