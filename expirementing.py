import re

pattern = r'^\(?-?\d+(\.\d+)?,\s?-?\d+(\.\d+)?\)?$'

# Test cases
test_cases = ["(1, 2)", "1,2", "1, 2", "1,2,3", "(1, 2, 3)", "(1.0, -2.5)", "-1.2, 3.4", "(1.2, 3.4)"]

for test in test_cases:
    if re.match(pattern, test):
        print(f"'{test}' is a valid point.")
    else:
        print(f"'{test}' is NOT a valid point.")
