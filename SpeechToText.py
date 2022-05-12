import multiprocessing as multi
import threading as th
import speech_recognition as sprecog

def PrintText(fileContents,index):
    try:
        print("Call: %d ; Process: %s " % (index, 1))
        print("Transcribed Text: " + recog.recognize_google(fileContents))
    except sprecog.UnknownValueError:
        print("Audio file could not be transcribed")

def SpeechToText(queue):
    index = queue.get()
    with sprecog.AudioFile(speechFiles[index]) as s:
        fileContents = recog.record(s)
    PrintText(fileContents, index)

speechFiles = ["sample1.wav", "sample2.wav"]
recog = sprecog.Recognizer()

if __name__ == '__main__':
    queue = multi.Queue()
    p = multi.Process(target=SpeechToText, args=(queue,))
    p.start()
    p = multi.Process(target=SpeechToText, args=(queue,))
    p.start()

    queue.put(0)
    queue.put(1)

    p.join()
