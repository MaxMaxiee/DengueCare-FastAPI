**To run the project:**
1. Run command "venv\scripts\activate"
2. If it returns an error delete the venv folder and create new by running command "python -m venv venv". Then repeat step 1. (Ignore this step if there's no error)
3. Go to project folder then run command "uvicorn main:app --reload" or "uvicorn main:app --port *prefered port number*"
4. To access the localhost go to "http://127.0.0.1:8000/docs#/". You should see the different endpoints.

**The process of creating this project:**
1. Create requirements.txt and install
2. Create main.py containing the app variable and including its router/s.
3. Create db folder containing the models.py(containing the tables and it's attributes)
4. 
