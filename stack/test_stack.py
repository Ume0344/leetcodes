import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_valid_paranthesis(self):

        st = Stack()

        s1 = "(){}"
        s2 = "{([])}"
        s3 = "(()"
        s4 = "({[])"

        s11 = st.valid_paranthesis(s1)
        s22 = st.valid_paranthesis(s2)
        s33 = st.valid_paranthesis(s3)
        s44 = st.valid_paranthesis(s4)

        assert s11 == True
        assert s22 == True
        assert s33 == False
        assert s44 == False

if __name__ == '__main__':
    unittest.main()
