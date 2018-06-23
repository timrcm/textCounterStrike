from unittest import TestCase
from unittest.mock import patch

import main
import config

class TestMain(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_start(self):
        # Testing that the teams are configured correctly
        pass

    def test_team_selection(self):
        with patch('__builtin__.raw_input', return_value='1') as _raw_input:
            self.assertEqual(config.team, 'Terrorist')
            _raw_input.assert_called_once_with('Terrorist')
