import heapq
import unittest


def min_meeting_rooms(meetings):
    if not meetings:
        return 0

    meetings = sorted(meetings)
    end_times = []
    rooms = 0

    for start, end in meetings:
        while end_times and end_times[0] <= start:
            heapq.heappop(end_times)

        heapq.heappush(end_times, end)
        rooms = max(rooms, len(end_times))

    return rooms


class MeetingRoomsTests(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(min_meeting_rooms([]), 0)

    def test_one_meeting(self):
        self.assertEqual(min_meeting_rooms([(9, 10)]), 1)

    def test_overlapping_meetings(self):
        self.assertEqual(min_meeting_rooms([(9, 10), (9.5, 11)]), 2)

    def test_meetings_do_not_overlap(self):
        self.assertEqual(
            min_meeting_rooms([(9, 10), (10, 11), (11, 12)]),
            1
        )

    def test_unsorted_meetings(self):
        self.assertEqual(
            min_meeting_rooms([(11, 12), (9, 10), (9.5, 11)]),
            2
        )

    def test_three_overlapping_meetings(self):
        self.assertEqual(
            min_meeting_rooms([(9, 12), (9.5, 11), (10, 13)]),
            3
        )


def main():
    meetings = [(9, 10), (9.5, 11), (11, 12)]
    print("Minimum number of rooms:", min_meeting_rooms(meetings))


if __name__ == "__main__":
    main()
    unittest.main(argv=["main.py"], exit=False)
