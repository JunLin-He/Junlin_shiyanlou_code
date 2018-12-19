#!/usr/bin/env python
import unittest
from mounttab import parse_mounts

class TestMount(unittest.TestCase):
    '''
    Basic test class
    '''

    def test_parsemount(self):
        '''
        All test case have prefix `test_`
        '''
        result = parse_mounts()
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)

    def test_roottext4(self):
        '''
        Find the root file system
        '''
        result = parse_mounts()
        for line in result:
            if line[1] == '/' and line[2] != 'rootfs':
                self.assertEqual(line[2], 'ext4')


if __name__ == '__main__':
    unittest.main()
