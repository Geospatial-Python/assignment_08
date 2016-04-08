# Assignment 06 - OOP and Inheretance

As usual, please fork this assignment to your own repository and
clone the code locally to your computer. 

Like last assignment, we are going to be working with point patterns.  The code 
we have written so far has been largely functional in style.  This week, we will
move some of the code to a more Object Oriented style.  This is not a full
move to OO; the vast majority of the work I do fuses OO with functional to 
leverage the strengths of both.  In fact, for those of you with experience
working with design patterns, many begin to 'fall apart' when using a 
dynamically typed language.  That is not to suggest that you can not code using
those design patterns verbatim, but that it frequently is not necessary.

Tasks:

1. Move your code (logic and tests) from assignment 05 into the assigment 06 repository and run `nosetests` to make sure you are building on your previous work.
1. Create a point class with three attributes, `x`, `y`, and a keyword argument `mark`.  Please place the point pattern class in `point.py`.
1. Add a method to the Point class to check if another point, passed as an argument, is coincident.  Remember that you already wrote this logic.
1. Add a method to shift the point in some direction.  This logic is also already written.
1. Create a `.py` file in the `tests/` directory (maybe `point_test.py`) that:
	* Tests that the class sets the `x` and `y` attribute correctly
	* Tests that you can pass a coincident point to the coincident point checking method and return True, and pass a non-conicident point to return False.
	* Tests that you can shift the points in some arbitrary direction correctly. 
	* Tests that you can create marked points properly.  To do this:
		* Seed a random number generator (see the functional test from last week if you are unsure how to do this).
		* Create a list of marks, e.g. `marks = ['red', 'blue']` (please use something different than red/blue).
		* Use `random.choice` to randomly select a mark and instantiate maybe 10 or 20.
		* Create a list of your points and maybe count the number of times each mark comes up.
		* Assert that the count is the same every time.
	* If you have trouble with import statements or getting this test to run:
		1. Check the other working tests and try to get a stripped down version working.
		2. Post in the forums with a code example. 	
1. Alter your average nearest neighbor distance check to 
	* Take a list of instances of your point class.
	* Accept a `mark` keyword argument where you can compute an average nearest neighbor distance for points with a shared `mark`.  If `mark` is not provided, compute the average nearest neighbor using all points.
1. Update or write a new function to create n random Points, where Point is an instance of your point class (instead of a tuple, last the previous few weeks).  This function should now be able to accept a list of potential marks and randomly mark a point.  A potential function signature might be:
 
	```python
	from points import Point
	def create_random_marked_points(n, marks=[]):
	    # for i in range(n):
		    # get random x and y
	   	   	# randomly select a mark
		    # create a point
		    # Add it to a list
	```

1. Update the functional test to:
	* Perform the same test as in assignment 5 (take all of the points, find the average nearest, generate n_random points, and find the critical points.  You should be able to update `test_point_pattern` to do this.
	* Write a new test that does an identical thing, but for each mark.  If you have two marks `['red, 'blue']` the test should compute the observed average nearest neighbor and the critical points for both the `red` marked points and the `blue` marked points.  I would generate at least 100 points and perform at least 99 permutations to get relatively stable numbers to base your tests off of (Note: I assume that you will get your test results from your tests.  This is not generally a great idea, but it is what we have to work with for now.)

If you have any questions, please post in the forums.

Once you are happy with your assignment, go ahead and submit a pull request.
If TravisCI shows an error (red X in the pull request) feel free to update
your repository (`git add -A .`, `git commit`, `git push origin master`).  Please
*do not* open more than one pull request.


