### Description ####
Python skeleton script to access EEA GPU that is running
Mistral-Small-3.1-24B-Instruct-2503

Description of the model:
[Documentation](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506)


### Installation ###
Create a python env, activate the environement, install openai dependency

```bash
  python -m venv venv
  venv\Scripts\activate 
  pip install openai
  pip install flask
  pip install IPython
  pip install python-dotenv
  pip install flask-cors
```

### Execution ###
First update file .env with your API_KEY provided by EEA

Then you can do a simple call with a question:
```bash
  python simpleCall.py
```

Or launch the chatBot:
```bash
  python chatBotCall.py
```

Or use it as a service in your own python projects:
```bash
  python serviceICall.py
```