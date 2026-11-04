# Meeting Rooms

## Project Idea

Find the minimum number of rooms needed for a list of meetings so that no two meetings in the same room overlap.

## How to Run

You need Python 3.

Run this command:

```bash
python main.py
```

The program prints the minimum number of rooms and runs the tests.

## Algorithm

The program sorts meetings by their start time and uses a min-heap to store meeting end times.

If a meeting has finished, its room can be used by another meeting.

## Tests

The tests are included in `main.py`. They check empty input, one meeting, overlapping meetings, meetings that touch, unsorted input, and three overlapping meetings.
