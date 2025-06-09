
import os
from groq import Groq


INPUT_TEXT = """
Whose woods these are I think I know.
His house is in the village, though;
He will not see me stopping here
To watch his woods fill up with snow.

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year.

He gives his harness bells a shake
To ask if there is some mistake.
The only other sound's the sweep
Of easy wind and downy flake.

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
"""

client = Groq(api_key=os.environ["GROQ_API_KEY"])
speech_file_path = "./poem.wav"
response = client.audio.speech.create(
  model="playai-tts",
  voice="Mitch-PlayAI",
  response_format="wav",
  input=INPUT_TEXT
)
response.write_to_file(speech_file_path)
      