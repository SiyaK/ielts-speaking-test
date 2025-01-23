import os
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import asyncio
from utils.speech_to_text import transcribe_stream
from utils.evaluate_response import evaluate_response
from utils.text_to_speech import generate_speech

app = FastAPI()

# Get the absolute path to the frontend folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# Mount the frontend directory to serve static files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    with open(index_path, "r") as file:
        return HTMLResponse(content=file.read())

@app.websocket("/ws/audio")
async def websocket_audio_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            audio_data = await websocket.receive_bytes()
            transcript = await transcribe_stream(audio_data)  # type: ignore
            feedback = evaluate_response(transcript)
            audio_response = generate_speech(feedback)

            await websocket.send_json({
                "transcript": transcript,
                "feedback": feedback,
                "audio_response": audio_response
            })
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()
