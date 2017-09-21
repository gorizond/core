FROM gorizond/aiohttp

ADD main.py main.py

CMD ["python3", "main.py"]
