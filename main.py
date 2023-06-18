import os
import json
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer

# Diretórios de áudio e transcrição
audio_dir = './audios'
transcript_dir = './transcript'

# Cria o diretório de transcrição se não existir
if not os.path.exists(transcript_dir):
    os.makedirs(transcript_dir)

# Carrega o modelo de reconhecimento de fala
model = Model("./vosk-model-pt")

# Itera sobre todos os arquivos de áudio
for filename in os.listdir(audio_dir):
    if filename.endswith('.wav'):  # ou '.mp3', etc.
        # Carrega o áudio
        audio_file = os.path.join(audio_dir, filename)
        audio = AudioSegment.from_wav(audio_file)  # ou from_mp3, etc.

        # Transcreve o áudio para texto
        with open(audio_file, 'rb') as f:
            rec = KaldiRecognizer(model, 16000)
            while True:
                data = f.read(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    print(rec.Result())
                else:
                    print(rec.PartialResult())
            result = rec.FinalResult()

        # Extrai o texto da transcrição do JSON
        result_json = json.loads(result)
        transcript_text = result_json.get('text', '')

        # Salva a transcrição
        transcript_file = os.path.join(transcript_dir, filename.replace('.wav', '.txt'))
        with open(transcript_file, 'w') as f:
            f.write(transcript_text)



# import os
# import speech_recognition as sr
# from pydub import AudioSegment
#
# # Diretórios de áudio e transcrição
# audio_dir = './calls'
# transcript_dir = './transcript'
#
# # Cria o diretório de transcrição se não existir
# if not os.path.exists(transcript_dir):
#     os.makedirs(transcript_dir)
#
# # Cria um reconhecedor de fala
# r = sr.Recognizer()
#
# # Itera sobre todos os arquivos de áudio
# for filename in os.listdir(audio_dir):
#     if filename.endswith('.mp3'):
#         # Carrega o áudio
#         audio_file = os.path.join(audio_dir, filename)
#         audio = AudioSegment.from_mp3(audio_file)
#
#         # Converte o áudio para WAV
#         wav_file = audio_file.replace('.mp3', '.wav')
#         audio.export(wav_file, format='wav')
#
#         # Transcreve o áudio para texto
#         with sr.AudioFile(wav_file) as source:
#             audio_data = r.record(source)
#             try:
#                 text = r.recognize_google(audio_data, language='pt-BR')
#             except sr.UnknownValueError:
#                 print(f"Google Speech Recognition could not understand audio from file {filename}")
#                 continue
#
#         # Salva a transcrição
#         transcript_file = os.path.join(transcript_dir, filename.replace('.mp3', '.txt'))
#         with open(transcript_file, 'w') as f:
#             f.write(text)


# import os
# import speech_recognition as sr
# from pydub import AudioSegment
#
# # Diretórios de áudio e transcrição
# audio_dir = './audios'
# transcript_dir = './transcript'
#
# # Cria o diretório de transcrição se não existir
# if not os.path.exists(transcript_dir):
#     os.makedirs(transcript_dir)
#
# # Cria um reconhecedor de fala
# r = sr.Recognizer()
#
# # Carrega as transcrições corretas
# with open(os.path.join(audio_dir, 'PROMPTS.txt'), 'r') as f:
#     correct_transcripts = {line.split()[0]: ' '.join(line.split()[1:]) for line in f}
#
# # Itera sobre todos os arquivos de áudio
# for filename in os.listdir(audio_dir):
#     if filename.endswith('.wav'):  # ou '.mp3', etc.
#         # Carrega o áudio
#         audio_file = os.path.join(audio_dir, filename)
#         audio = AudioSegment.from_wav(audio_file)  # ou from_mp3, etc.
#
#         # Transcreve o áudio para texto
#         with sr.AudioFile(audio_file) as source:
#             audio_data = r.record(source)
#             text = r.recognize_google(audio_data, language='pt-BR')
#
#         # Salva a transcrição
#         transcript_file = os.path.join(transcript_dir, filename.replace('.wav', '.txt'))  # ou '.mp3', etc.
#         with open(transcript_file, 'w') as f:
#             f.write(text)
#
#         # Compara a transcrição gerada com a transcrição correta
#         correct_transcript = correct_transcripts.get(filename.replace('.wav', ''), '')  # ou '.mp3', etc.
#         if text.lower() == correct_transcript.lower():
#             print(f'Transcrição correta para {filename}!')
#         else:
#             print(f'Transcrição incorreta para {filename}. Esperado: {correct_transcript}, Obtido: {text}')
