
# 1. Install Dependency
```
pip install -r requirements.txt
```

# 2. Run Fast API
```
uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload
```

# 3. Tunneling The Localhost using ngrok (Optional)
```
ngrok http 8000

```
