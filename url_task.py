from urllib.parse import urlencode
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/encode_url/{url:path}")
def encode_url(url: str = Path(...)):

    encoded_url = urlencode({"url": url})
    return {"encoded_url": encoded_url}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
