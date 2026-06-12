"""reverse_demo.py

Demonstrates how to use `reverse.py` and how to access docstrings/help
for learning and interactive exploration.

Run this script to see examples and to inspect the function docstrings.
"""

from reverse import reverse_for, reverse_while


def show_docstrings():
    print("--- docstring for reverse_for ---")
    print(reverse_for.__doc__)
    print("--- help(reverse_while) output ---")
    help(reverse_while)


def demo_examples():
    print("\nDemo: reversing lists (in-place)")
    lst = [1, 2, 3, 4, 5]
    print("before:", lst)
    print("after:", reverse_for(lst))

    print("\nDemo: reversing string characters — convert to list first")
    s = "Dharani"
    s_list = list(s)
    print("before list:", s_list)
    reverse_while(s_list)
    print("after list:", s_list)
    print("joined:", ''.join(s_list))


if __name__ == '__main__':
    show_docstrings()
    demo_examples()
