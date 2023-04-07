### How to run the model's backend server

```
pip install uvicorn
uvicorn model:app --host 127.0.0.1 --port 8080
```

Example request:

`http://127.0.0.1:8080/?s1=back_pain&s2=constipation&s3=abdominal_pain&s4=diarrhoea&s5=mild_fever`
