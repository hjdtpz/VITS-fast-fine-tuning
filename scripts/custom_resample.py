import os
import json
import argparse
import torchaudio


def main():
    with open("./configs/finetune_speaker.json", 'r', encoding='utf-8') as f:
        hps = json.load(f)
    target_sr = hps['data']['sampling_rate']
    filelist = list(os.walk("./raw_audio"))[0][2]
    for wavfile in filelist:
        print(wavfile)
        wav, sr = torchaudio.load("./raw_audio" + "/" + wavfile, frame_offset=0, num_frames=-1,
                                  normalize=True, channels_first=True)
        wav = torchaudio.transforms.Resample(orig_freq=sr, new_freq=target_sr)(wav)
        torchaudio.save("./custom_character_voice/NagatoYuki_1" + "/" + wavfile, wav, target_sr, channels_first=True)

if __name__ == "__main__":
    main()
