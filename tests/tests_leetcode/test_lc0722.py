import pytest

from leetcode import lc0722

examples = [
    (
        [
            "/*Test program */",
            "int main()",
            "{ ",
            "  // variable declaration ",
            "int a, b, c;",
            "/* This is a test",
            "   multiline  ",
            "   comment for ",
            "   testing */",
            "a = b + c;",
            "}",
        ],
        ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"],
    ),
    (["a/*comment", "line", "more_comment*/b"], ["ab"]),
]


@pytest.mark.parametrize("source, output_true", examples)
def test_removeComments(source: list[str], output_true: list[str]):
    output_calc = lc0722.removeComments(source=source)
    assert output_calc == output_true
