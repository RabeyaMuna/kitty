#!./kitty/launcher/kitty +launch
# License: GPL v3 Copyright: 2016, Kovid Goyal <kovid at kovidgoyal.net>

import importlib
import sys
import traceback


def main() -> None:
    try:
        if len(sys.argv) > 1 and sys.argv[1] == 'mypy':
            import subprocess
            raise SystemExit(subprocess.call([sys.executable, '-m', 'mypy', *sys.argv[2:]]))
        m = importlib.import_module('kitty_tests.main')
        getattr(m, 'main')()
    except Exception:
        traceback.print_exc()
        raise SystemExit(1)


if __name__ == '__main__':
    main()
