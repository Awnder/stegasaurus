import unittest
import stega
from PIL import Image


class TestStega(unittest.TestCase):
    def test_stega(self):
        self.assertEqual(
            [0, 0, 0, 0, 0, 0, 0, 1],
            stega._bytes_to_bit_array(b"\x01"),
        )
        self.assertEqual(
            [1, 0, 0, 0, 0, 0, 0, 0],
            stega._bytes_to_bit_array(b"\x80"),
        )
        self.assertEqual(
            [0, 0, 0, 0, 0, 0, 0, 0],
            stega._bytes_to_bit_array(b"\x00"),
        )
        self.assertEqual(
            [1, 1, 1, 1, 1, 1, 1, 1],
            stega._bytes_to_bit_array(b"\xFF"),
        )
        self.assertEqual(
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
            stega._bytes_to_bit_array(b"he"),
        )
        self.assertEqual([
            0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 
            1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1
            ],
            stega._bytes_to_bit_array(b"hello")
        )
        self.assertEqual([
            0, 1, 1, 0, 1, 0, 0, 0,  # h
            0, 1, 1, 0, 0, 1, 0, 1,  # e
            0, 1, 1, 0, 1, 1, 0, 0,  # l
            0, 1, 1, 0, 1, 1, 0, 0,  # l
            0, 1, 1, 0, 1, 1, 1, 1,  # o
            0, 0, 1, 0, 0, 0, 0, 0,  # (space)
            0, 1, 1, 0, 1, 0, 0, 0,  # h
            0, 1, 1, 0, 0, 1, 0, 1,  # e
            0, 1, 1, 0, 1, 1, 0, 0,  # l
            0, 1, 1, 0, 1, 1, 0, 0,  # l
            0, 1, 1, 0, 1, 1, 1, 1,  # o
            0, 0, 1, 0, 0, 0, 0, 0,  # (space)
            0, 1, 1, 0, 1, 0, 0, 0,  # h
            0, 1, 1, 0, 0, 1, 0, 1,  # e
            0, 1, 1, 0, 1, 1, 0, 0,  # l
            0, 1, 1, 0, 1, 1, 0, 0,  # l
            0, 1, 1, 0, 1, 1, 1, 1,  # o
            0, 0, 1, 0, 0, 0, 0, 0,  # (space)
            0, 1, 1, 0, 1, 0, 0, 0,  # h
            0, 1, 1, 0, 0, 1, 0, 1,  # e
            0, 1, 1, 0, 1, 1, 0, 0,  # l
            0, 1, 1, 0, 1, 1, 0, 0,  # l
            0, 1, 1, 0, 1, 1, 1, 1   # o
        ],
            stega._bytes_to_bit_array(b"hello hello hello hello")
        )
        
        self.assertEqual(
            b"\x01",
            stega._bit_array_to_bytes([0, 0, 0, 0, 0, 0, 0, 1]),
        )
        self.assertEqual(
            b"\x80",
            stega._bit_array_to_bytes([1, 0, 0, 0, 0, 0, 0, 0]),
        )
        self.assertEqual(
            b"\x00",
            stega._bit_array_to_bytes([0, 0, 0, 0, 0, 0, 0, 0]),
        )
        self.assertEqual(
            b"\xFF",
            stega._bit_array_to_bytes([1, 1, 1, 1, 1, 1, 1, 1]),
        )
        self.assertEqual(
            b"he",
            stega._bit_array_to_bytes([0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]),
        )
        self.assertEqual(
            b"hello",
            stega._bit_array_to_bytes([0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1])
        )
        self.assertEqual(
            b"hello hello hello hello",
            stega._bit_array_to_bytes([
                0, 1, 1, 0, 1, 0, 0, 0,  # h
                0, 1, 1, 0, 0, 1, 0, 1,  # e
                0, 1, 1, 0, 1, 1, 0, 0,  # l
                0, 1, 1, 0, 1, 1, 0, 0,  # l
                0, 1, 1, 0, 1, 1, 1, 1,  # o
                0, 0, 1, 0, 0, 0, 0, 0,  # (space)
                0, 1, 1, 0, 1, 0, 0, 0,  # h
                0, 1, 1, 0, 0, 1, 0, 1,  # e
                0, 1, 1, 0, 1, 1, 0, 0,  # l
                0, 1, 1, 0, 1, 1, 0, 0,  # l
                0, 1, 1, 0, 1, 1, 1, 1,  # o
                0, 0, 1, 0, 0, 0, 0, 0,  # (space)
                0, 1, 1, 0, 1, 0, 0, 0,  # h
                0, 1, 1, 0, 0, 1, 0, 1,  # e
                0, 1, 1, 0, 1, 1, 0, 0,  # l
                0, 1, 1, 0, 1, 1, 0, 0,  # l
                0, 1, 1, 0, 1, 1, 1, 1,  # o
                0, 0, 1, 0, 0, 0, 0, 0,  # (space)
                0, 1, 1, 0, 1, 0, 0, 0,  # h
                0, 1, 1, 0, 0, 1, 0, 1,  # e
                0, 1, 1, 0, 1, 1, 0, 0,  # l
                0, 1, 1, 0, 1, 1, 0, 0,  # l
                0, 1, 1, 0, 1, 1, 1, 1   # o
            ])
        )

        self.assertEqual(
            stega._hide_message(
                [23, 200, 102, 50, 0, 21, 24, 59, 99, 83, 79, 1, 32, 255, 0, 33, 232, 100, 203, 88, 254, 23, 104, 76],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0] #h e l
            ),
            [22, 201, 103, 50, 1, 20, 24, 58, 98, 83, 79, 0, 32, 255, 0, 33, 232, 101, 203, 88, 255, 23, 104, 76]
        )

        self.assertEqual(
            stega._extract_message(
                [22, 201, 103, 50, 1, 20, 24, 58, 98, 83, 79, 0, 32, 255, 0, 33, 232, 101, 203, 88, 255, 23, 104, 76]
            ),
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0] #h e l
        )

        # this test shows _hide_message works as expected regarding 256 and beyond characters
        self.assertEqual(
            stega._hide_message(
            stega._bytes_to_bit_array(b"\x00" * 64), # 512 bits
            [0, 1] * 256 # 512 bits
            ),
            [0, 1] * 256
        )

        # shows _extract_message works as expected regarding 256 and beyond characters
        self.assertEqual(
            stega._extract_message(
                stega._hide_message(
                    stega._bytes_to_bit_array(b"\x00" * 64), # 512 bits
                        [0, 1] * 256 # 512 bits
                    )
                ),
            [0, 1] * 256
        )
        # error: overflow here and resets to "" 
        self.assertEqual( 
            stega.extract_message(
                stega.hide_message(
                    Image.open("flower.png"), 
                    b"one two three four five six seve" # 256 bits (32 characters * 8 bits per character)
                )
            ),
            b"one two three four five six seve"
        )

        ### TESTS CREATED BY CHATGPT ### -- ALL OF THESE PASS
        self.assertEqual(
            stega._hide_message(
            [255, 255, 255, 255, 255, 255, 255, 255],
            [1, 0, 1, 0, 1, 0, 1, 0]
            ),
            [255, 254, 255, 254, 255, 254, 255, 254]
        )

        self.assertEqual(
            stega._extract_message(
            [255, 254, 255, 254, 255, 254, 255, 254]
            ),
            [1, 0, 1, 0, 1, 0, 1, 0]
        )

        self.assertEqual(
            stega._hide_message(
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1]
            ),
            [1, 1, 1, 1, 1, 1, 1, 1]
        )

        self.assertEqual(
            stega._extract_message(
            [1, 1, 1, 1, 1, 1, 1, 1]
            ),
            [1, 1, 1, 1, 1, 1, 1, 1]
        )

        self.assertEqual(
            stega._hide_message(
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
            ),
            [0, 0, 0, 0, 0, 0, 0, 0]
        )

        self.assertEqual(
            stega._extract_message(
            [0, 0, 0, 0, 0, 0, 0, 0]
            ),
            [0, 0, 0, 0, 0, 0, 0, 0]
        )

        self.assertEqual(
            stega._hide_message(
            [23, 200, 102, 50, 0, 21, 24, 59, 99, 83, 79, 1, 32, 255, 0, 33, 232, 100, 203, 88, 254, 23, 104, 76],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ),
            [23, 201, 103, 51, 1, 21, 25, 59, 99, 83, 79, 1, 33, 255, 1, 33, 233, 101, 203, 89, 255, 23, 105, 77]
        )

        self.assertEqual(
            stega._extract_message(
            [23, 201, 103, 51, 1, 21, 25, 59, 99, 83, 79, 1, 33, 255, 1, 33, 233, 101, 203, 89, 255, 23, 105, 77]
            ),
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        )

        self.assertEqual(
            stega._hide_message(
            [23, 200, 102, 50, 0, 21, 24, 59, 99, 83, 79, 1, 32, 255, 0, 33, 232, 100, 203, 88, 254, 23, 104, 76],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ),
            [22, 200, 102, 50, 0, 20, 24, 58, 98, 82, 78, 0, 32, 254, 0, 32, 232, 100, 202, 88, 254, 22, 104, 76]
        )

        self.assertEqual(
            stega._extract_message(
            [22, 200, 102, 50, 0, 20, 24, 58, 98, 82, 78, 0, 32, 254, 0, 32, 232, 100, 202, 88, 254, 22, 104, 76]
            ),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

if __name__ == "__main__":
    unittest.main()
