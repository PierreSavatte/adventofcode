# Simplify existing implementation
Remove the helper function, and simplyfy the parsing to avoid building the
dug_cells.


# New idea
Test just computing the limits:

.#...#.
##....#
.......
#.#....
..#...#

Limits:

- if y in `[0, 0]`: x in `[1, 5]`
- if y in `[1, 3]`: x in `[0, 6]`
- if y in `[4, 4]`: x in `[2, 6]`
