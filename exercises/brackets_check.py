# Check if brackets sequence is right
# Example
# ()()(()()) -> True
# ())( -> False

def check_sequence_of_brackets(seq: str):
    counter = 0
    if len(seq) == 0:
        return True
    for symb in seq:
        if symb == ')':
            counter += 1
        elif symb == '(':
            counter -= 1
        if counter > 0:
            return False

    return counter == 0

# TESTS
tests = (
    ('', True),
    ('(', False),
    (')', False),
    ('()', True),
    (')(', False),
    ('((', False),
    ('(()', False),
    ('((()))))(((())', False),
    ('(())((()', False),
    ('()())(', False),
    ('()()(()())', True)
)

for test in tests:
    res = check_sequence_of_brackets(test[0])
    assert res == test[1], f"Seq: {test[0]}, Expect: {test[1]}, Res: {res}"

print("OK")