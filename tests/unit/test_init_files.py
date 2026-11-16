# SPDX-License-Identifier: GPL-2.0

import unittest
from pathlib import Path


class TestInitFiles(unittest.TestCase):
    def test_test_dirs_have_init_py(self) -> None:
        tests_dir = Path(__file__).resolve().parent.parent
        missing = sorted(
            str(test_file.parent.relative_to(tests_dir))
            for test_file in tests_dir.rglob("test_*.py")
            if not (test_file.parent / "__init__.py").exists()
        )
        self.assertEqual(missing, [])
