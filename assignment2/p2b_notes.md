
```
For all intervals I in S (by ascending start times):
    For all rooms R in use:
        If I can fit in R:
            Put I in R.
    If no room could be found:
        Create a new room R.
        Put I in R.
```

In any collection of intervals, there exist points which have the maximum number of intervals intersecting at the same time.
Say at these points that n intervals intersect.
This means that there is no way to fit these classes with any fewer than n rooms.
For that reason, any algorithm which assigns this collection to n rooms will be optimal.

We consider the algorithm above.
It trivially satisfies the no overlap rule; it will not place a class into a room unless the entire class time is available.
Thus, all that is left to show is that this algorithm will assign a collection of classes to no more rooms than the maximum number occuring at the same time.

Each room is chosen by start time, so all previous rooms are already placed.
Now, this course overlaps with some (n) already placed, and some (m) not yet placed.
Note that the placement of this course will require n+1 rooms to be optimal, by the lemma shown above.
Now, becuse the other n have been placed, this course conflicts with them all, and thus requires exactly n+1 rooms.
This process repeats for each course.

Therefore, the algorithm above does indeed solve the Interval Coloring Problem.