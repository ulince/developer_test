# Developer test
After cloning or downloading the project, to run the program execute:
```
cd /developer_test/src
python grid_test.py
```
Additionally, provide the optional command-line argument '--all' to have the program print all the randomly generated seed data after the required results:
```
python grid_test.py --all
```
The program makes the folowing assumptions:
- The number of tickets per event is between 0 and 10
- The price range of tickets is between 1.0 and 100.0
- Events with no tickets will not be shown, even if they are closer to the coordinates.
These assumptions were made for practical reasons, but in no way constrain the logic of the algorithm.

## Extending the program
- How might you change your program if you needed to support multiple events at the same location? 
I would change the data structure that represents the grid to hold lists of Events, instead of single Event objects. I would declare it like this:
```
grid = defaultdict(lambda : defaultdict(list))
```
and Events would be added like this:
```
grid[some_x][some_y].append(some_event)
```
- How would you change your program if you were working with a much larger world size? 
Assuming that the whole world fits in memory, I would only change line 111 in the main algorithm, replacing the 441 for the total number of coordinates in the world. Even though the algorithm would visit all vertices in the worst case scenario, typically the size of the world shouldn't be a problem.
