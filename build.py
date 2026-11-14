"""Build the Hello World app into dist/helloworld.xtapp."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "tools", "vendor"))

import xtpack  # noqa: E402


def main():
    out = os.path.join(HERE, "dist", "helloworld.xtapp")
    xtpack.pack(os.path.join(HERE, "app"), out)


if __name__ == "__main__":
    main()
