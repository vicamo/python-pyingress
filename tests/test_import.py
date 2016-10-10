# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import inspect
import unittest

import pyingress

# =============================
# from pyingress import * tests
# =============================

class TestImportStar(unittest.TestCase):
    def test(self):
        for name in pyingress.__all__:
            self.assertTrue(hasattr(pyingress, name))

    def test_all_exports_everything_but_modules(self):
        items = [
            name
            for name, value in vars(pyingress).items()
            if not name.startswith("_")
            if not inspect.ismodule(value)
        ]
        self.assertEqual(sorted(items), sorted(pyingress.__all__))
