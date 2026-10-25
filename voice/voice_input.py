
import sounddevice as sd
import speech_recognition as sr
import numpy as np
import time


def listen():
    recognizer = sr.Recognizer()

    sample_rate = 16000
    silence_limit = 5
    max_duration = 30
    frame_duration = 0.1

    silence_threshold = 300

    print("Listening... Speak now.")

    audio_frames = []
    silence_start = None
    speech_detected = False
    start_time = time.time()

    try:
        with sd.InputStream(
            samplerate=sample_rate,
            channels=1,
            dtype="int16"
        ) as stream:

            while True:
                frame, overflowed = stream.read(
                    int(sample_rate * frame_duration)
                )

                audio_frames.append(frame.copy())

                audio_level = np.abs(
                    frame.astype(np.int32)
                ).mean()

                if audio_level > silence_threshold:
                    speech_detected = True
                    silence_start = None

                elif speech_detected:
                    if silence_start is None:
                        silence_start = time.time()

                    elif time.time() - silence_start >= silence_limit:
                        print("Silence detected. Processing...")
                        break

                if time.time() - start_time >= max_duration:
                    print("Maximum recording time reached.")
                    break

        if not speech_detected:
            print("No speech detected.")
            return None

        audio_data = np.concatenate(audio_frames, axis=0)

        audio = sr.AudioData(
            audio_data.tobytes(),
            sample_rate,
            2
        )

        print("Recognizing speech...")

        try:
            text = recognizer.recognize_google(audio)
            return text

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand you.")
            return None

        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None

    except Exception as e:
        print(f"Microphone error: {e}")
        return None
