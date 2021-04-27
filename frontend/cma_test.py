import unittest
from cma import C


class TestParserConstant(unittest.TestCase):

    def test_parsing_constant(self):
        data = "42"
        result = str(C.Expression.parseString(data))
        desired = "[Constant(value=42)]"
        self.assertEqual(result, desired)

    def test_parsing_constant_truncation(self):
        data = "42 43"
        result = str(C.Expression.parseString(data))
        desired = "[Constant(value=42)]"
        self.assertEqual(result, desired)


class TestParserIdentifier(unittest.TestCase):

    def test_parsing_identifier(self):
        data = "asdf"
        result = str(C.Expression.parseString(data))
        desired = "[Identifier(name='asdf')]"
        self.assertEqual(result, desired)

    def test_parsing_identifier_truncation(self):
        data = "asdf asdf"
        result = str(C.Expression.parseString(data))
        desired = "[Identifier(name='asdf')]"
        self.assertEqual(result, desired)


class TestParserBinOp(unittest.TestCase):
    def test_parsing_binop_minus_constants(self):
        data = "42 - 1"
        result = str(C.Expression.parseString(data))
        desired = "[BinaryOp(left=Constant(value=42), op='-', right=Constant(value=1))]"
        self.assertEqual(result, desired)

    def test_parsing_binop_plus_identifier(self):
        data = "a + b"
        result = str(C.Expression.parseString(data))
        desired = "[BinaryOp(left=Identifier(name='a'), op='+', right=Identifier(name='b'))]"
        self.assertEqual(result, desired)

    def test_parsing_binop_precedence(self):
        data = "3 + d / 5"
        result = str(C.Expression.parseString(data))
        desired = "[BinaryOp(left=Constant(value=3), op='+', right=BinaryOp(left=Identifier(name='d'), op='/', right=Constant(value=5)))]"
        self.assertEqual(result, desired)


class TestParserUnaryOp(unittest.TestCase):
    def test_parsing_binop_minus_constants(self):
        data = "-1"
        result = str(C.Expression.parseString(data))
        desired = "[UnaryOp(op='-', expr=Constant(value=1))]"
        self.assertEqual(result, desired)


class TestParserAssignment(unittest.TestCase):
    
    def test_parsing_correct_constant_assignment(self):
        data = "x = 3"
        result = str(C.Expression.parseString(data))
        desired = "[Assignment(left=Identifier(name='x'), right=Constant(value=3))]"
        self.assertEqual(result, desired)

    def test_parsing_incorrect_constant_assignment(self):
        data = "3 = 3"
        result = str(C.Expression.parseString(data))
        desired = "[Constant(value=3)]"
        self.assertEqual(result, desired)

    def test_parsing_correct_binop_assignment(self):
        data = "x = 3 + y"
        result = str(C.Expression.parseString(data))
        desired = "[Assignment(left=Identifier(name='x'), right=BinaryOp(left=Constant(value=3), op='+', right=Identifier(name='y')))]"
        self.assertEqual(result, desired)

    def test_parsing_incorrect_binop_assignment(self):
        data = "3 + 3 = x"
        result = str(C.Expression.parseString(data))
        desired = "[BinaryOp(left=Constant(value=3), op='+', right=Constant(value=3))]"
        self.assertEqual(result, desired)
if __name__ == '__main__':
    unittest.main()
