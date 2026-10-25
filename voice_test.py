from voice.voice_input import listen

print("Jarvis Voice Test")
print("=================")
result = listen()

if result:
    print("You said:", result)