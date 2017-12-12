# Course-Snagger

This will check every 2 seconds.


Firstly, lets setup a virtual environment that will contain all of the necessary modules

1. Run 'module load python3/3.4'
2. Run 'virtualenv myenv'
3. Run 'source myenv/bin/activate'

Lastly, install all of the necessary modules

4. Run 'make core'
5. you will be prompted for information in the following format
	Email (Send): <YOUR EMAIL>
	Email Password: <PASS>
	Recipient: <RECEIVER>
	Number of Courses to check: <NUM_OF_CCOURSES>
	
	Then it will ask for the Department (i.e. "CS" or "ECE" or "FR" for "Computer Science", "Electrical Engineering" and "French" respectively), Course Number ("374", "411","101", etc.), and Course crn ("64089", etc) sequentially.
	
	

If you can install the fbchat module (manually or pip) then Run 'make core1" instead (I couldn't find a way to install this module.  I looked everywhere).





http://studentcode.illinois.edu/ specifies the rules and regulations regarding automated scraping and registration
