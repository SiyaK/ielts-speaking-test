import os
import asyncio
from deepgram import DeepgramClient

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

async def transcribe_stream(audio_chunk):
    client = DeepgramClient(DEEPGRAM_API_KEY)

    # Send the audio to Deepgram for transcription
    response = await client.listen.prerecorded(
        payload={"buffer": audio_chunk, "mimetype": "audio/wav"},
        options={"punctuate": True, "language": "en"}
    )

    transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
    return transcript
