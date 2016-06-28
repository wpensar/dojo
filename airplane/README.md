Given a number of rows on a plane and seats that have already been sold, the
objective of this Kata is to tell how many families of 3 can still be seated
together on this airplane.

Each row has 10 seats from A to J. The isles are between seats C, D and G, H.
An airplane with one row would be the following:

    1A 1B 1C | | 1D 1E 1F 1G | | 1H 1I 1J

We say that a family of 3 was seated together when they are side by side, on
3 contiguous seats, with no isles or other people between them.


For example a family of 3 would be seated together if they were on seats:

    "1A 1B 1C"

But they could not be seated together on seats:

    "1G 1H 1I"
