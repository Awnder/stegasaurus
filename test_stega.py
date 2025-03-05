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

        # self.assertEqual(
        #     stega._hide_message(
        #         [23, 200, 102, 50, 0, 21, 24, 59, 99, 83, 79, 1, 32, 255, 0, 33, 232, 100, 203, 88, 254, 23, 104, 76],
        #         [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0] #h e l
        #     ),
        #     [22, 201, 103, 50, 1, 20, 24, 58, 98, 83, 79, 0, 32, 255, 0, 33, 232, 101, 203, 88, 255, 23, 104, 76]
        # )

        # self.assertEqual(
        #     stega._extract_message(
        #         [22, 201, 103, 50, 1, 20, 24, 58, 98, 83, 79, 0, 32, 255, 0, 33, 232, 101, 203, 88, 255, 23, 104, 76]
        #     ),
        #     [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0] #h e l
        # )
        
        # original_array = [
        #     23, 200, 102, 50, 0, 21, 24, 59, 99, 83, 79, 1, 32, 255, 0, 33, 232, 100, 203, 88,
        #     254, 23, 104, 76, 23, 200, 102, 50, 0, 21, 24, 59, 99, 83, 79, 1, 32, 255, 0, 33
        # ]

        # # Binary representation of "hello"
        # binary_message = [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0,
        #         0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]

        # # Expected transformed array after embedding the message
        # expected_array = [
        #     22, 201, 103, 50, 1, 20, 24, 58, 98, 83, 79, 0, 32, 255, 0, 33, 232, 101, 203, 88,
        #     255, 23, 104, 76, 22, 201, 102, 50, 1, 21, 24, 59, 99, 83, 78, 1, 32, 255, 0, 33
        # ]

        # # Test the function
        # self.assertEqual(
        #     stega._hide_message(original_array, binary_message),
        #     expected_array
        # )

        # # Test the extraction function
        # self.assertEqual(
        #     stega._extract_message(expected_array),
        #     binary_message
        # )

        self.assertEqual(
            stega.extract_message(
                stega.hide_message(
                    Image.open("flower.png"), 
                    b"one two three four five six seven eight nine ten"
                )
            ),
            b"one two three four five six seven eight nine ten"
        )


if __name__ == "__main__":
    unittest.main()
