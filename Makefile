init:
	module load python3/3.4
	virtualenv myenv
	myenv myenv/bin/activate
	pip install -r requirements.txt
	
	
	
	python core.py
	

