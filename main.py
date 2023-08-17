"""
Main
"""
import os
import sys

module_two_pointers = os.path.abspath(os.path.join('two_pointers'))
sys.path.append(module_two_pointers)


def main():
    print(sys.path)


if __name__ == '__main__':
    main()
