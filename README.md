# code-assignment
This is my submission for the HiQ technical interview

### Running the program
1. Python version used is 3.12.
2. Create a virtual environment using the command 
```python -m venv <environment name>```
3. Enter the environment:
```source <environment name>/bin/activate```
4. Install required packages using the requirement file:
```pip install -r /path/to/requirements.txt```
5. To run the program, go to the src directory and run
```python main.py```

The program runs on port 8080. Requests are sent to localhost:8080/file and expects a field namned "file" in the body. The request must be a POST request. I used Insomnia to test.