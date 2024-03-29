import unittest
from coord_draw import parse_instructions, prepare_instructions

DEFAULT_SCALE = 20


class TestCoordDraw(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(
            prepare_instructions(["(2; -3)"], DEFAULT_SCALE),
            [[[40, -60]]],
        )

    def test_float(self):
        self.assertEqual(
            prepare_instructions(["(2; 3,5)"], DEFAULT_SCALE),
            [[[40, 70]]],
        )

    def test_create_split(self):
        self.assertEqual(
            parse_instructions("(2; -3) и (3; -1)"), ["(2; -3) ", " (3; -1)"]
        )

    def test_remove_spaces(self):
        self.assertEqual(
            prepare_instructions(["(2 ; - 3) ", " (3 ; - 3 , 5)"], DEFAULT_SCALE),
            [
                [[40, -60]],
                [[60, -70]],
            ],
        )

    def test_draw_elephant(self):
        inp = """Голова слона: (2; - 3), (2; - 2), (4; - 2), (4; - 1), (3; 1), (2; 1), (1; 2), (0; 0), (- 3; 2), (- 4; 5),
(0; 8), (2; 7), (6; 7), (8; 8), (10; 6), (10; 2), (7; 0), (6; 2), (6; - 2), (5; - 3), (2; - 3) и (2; 4) и (6; 4)."""
        parsed_input = parse_instructions(inp)
        expected_result = [
            [
                [40.0, -60.0],
                [40.0, -40.0],
                [80.0, -40.0],
                [80.0, -20.0],
                [60.0, 20.0],
                [40.0, 20.0],
                [20.0, 40.0],
                [0.0, 0.0],
                [-60.0, 40.0],
                [-80.0, 100.0],
                [0.0, 160.0],
                [40.0, 140.0],
                [120.0, 140.0],
                [160.0, 160.0],
                [200.0, 120.0],
                [200.0, 40.0],
                [140.0, 0.0],
                [120.0, 40.0],
                [120.0, -40.0],
                [100.0, -60.0],
                [40.0, -60.0],
            ],
            [[40.0, 80.0]],
            [[120.0, 80.0]],
        ]
        self.assertEqual(
            prepare_instructions(parsed_input, DEFAULT_SCALE), expected_result
        )


if __name__ == "__main__":
    unittest.main()
