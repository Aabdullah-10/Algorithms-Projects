# Meeting Rooms

## 1. Problem

The problem is to find the minimum number of rooms needed for a list of meetings.

Two meetings cannot use the same room if their times overlap. If one meeting ends when another starts, they can use the same room.

## 2. Method

The program uses a min-heap.

First, it sorts the meetings by their start times. Then it checks the earliest ending meeting.

If that meeting has ended, its room can be used again. The program removes finished meetings from the heap and adds the current meeting.

The largest number of meetings in the heap is the minimum number of rooms needed.

## 3. Complexity Analysis

Sorting the meetings takes O(n log n).

Each meeting is added to the heap once and removed at most once. Heap operations take O(log n).

Therefore, the total time complexity is O(n log n).

The heap can store up to n meeting end times, so the space complexity is O(n).

## 4. Experiments

The program was checked using these test cases:

| Test case | Expected rooms | Result |
|---|---:|---|
| Empty list | 0 | Passed |
| One meeting | 1 | Passed |
| Two overlapping meetings | 2 | Passed |
| Meetings that do not overlap | 1 | Passed |
| Unsorted meetings | 2 | Passed |
| Three overlapping meetings | 3 | Passed |

All six tests passed.

## 5. Conclusion

The project uses a min-heap to find the minimum number of meeting rooms. The solution is simple and works in O(n log n) time.

## 6. Reflection

The important point was that meetings should be processed by start time. The min-heap makes it easy to find the meeting that ends first.

In the future, the program could also show which room is assigned to each meeting.
