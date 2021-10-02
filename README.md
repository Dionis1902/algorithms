### Laboratory work 3 

Suppose the company you work for develops an electronic calendar. The calendar has a function that shows when different teams of programmers will be busy during any meeting.

The periods when the team is busy are marked on the calendar as time ranges, for example, from 10:00 to 12:30 or from 12:30 to 13:00. In your program, the time interval is represented as a pair of two integers. The number means the number of the 30-minute block that goes after 9:00 am. For example, tuple (2, 4) means the range from 10:00 to 11:00, and (0, 1) is the interval 9: 00-9: 30.

You need to write a function that should simplify the output of information in such a way that if the team is busy between 10:00 to 12:30 and from 12:30 to 13:00, it should be displayed as 10: 00-13: 00. For example: at the input of your function an unordered array of tuples [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)], then at the output you should get an ordered array [(0, 1), (3, 8), (9, 12)].


In the future, it is planned to make changes to the program, where instead of 30-minute blocks will be minutes, as implemented in the Unix-time representation. With that in mind, your feature needs to work with large numbers right now. Remember that a tuple is a type of data in which the contents of a variable cannot be changed after it has been created.
  ### How to run
  + Clone this repository with command `git clone https://github.com/DioniS1902/algorithms.git`
  + Go into folder with files with command `cd algorithms`  
  + Choose branch quicksort with command `git checkout lab3`
  + run command `python3 main.py` on Mac/Linux
  + run command `py main.py` on Windows