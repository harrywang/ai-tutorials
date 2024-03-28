revised from https://www.toolify.ai/ai-news/learn-how-to-create-a-highspeed-streaming-api-with-python-93264

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

http://127.0.0.1:8000/
http://127.0.0.1:8000/jokes to see streaming output