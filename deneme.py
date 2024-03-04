import mne
import matplotlib.pyplot as plt

# def plot_eeg_channel(eeg_file_path="data.edf", channel_name="Fp1"):
    # EEG verisini oku
 #    raw = mne.io.read_raw_edf(eeg_file_path, preload=True)

    # Belirli bir kanaldaki veriyi seç
   #  eeg_data, times = raw[channel_name, :]

    # EEG verisini çiz
   #  plt.figure(figsize=(10, 4))
  #   plt.plot(times, eeg_data[0], label=f'{channel_name} EEG Verisi', color='blue')
  #   plt.title(f'{channel_name} EEG Verisi')
  #   plt.xlabel('Zaman (saniye)')
  #   plt.ylabel('EEG Amplitüdü')
  #   plt.legend()
  #   plt.show()

# if __name__ == "__main__":
 #    plot_eeg_channel(eeg_file_path="data.edf", channel_name="Fp3")

import mne
import matplotlib.pyplot as plt

def plot_eeg_channel(eeg_file_path="data.edf", channel_name="Fp1", start_time=0, end_time=30):
    # EEG verisini oku
    raw = mne.io.read_raw_edf(eeg_file_path, preload=True)

    # Belirli bir zaman aralığındaki veriyi seç
    eeg_data, times = raw[channel_name, int(start_time * raw.info['sfreq']):int(end_time * raw.info['sfreq'])]

    # EEG verisini çiz
    plt.figure(figsize=(10, 4))
    plt.plot(times, eeg_data[0], label=f'{channel_name} EEG Verisi', color='blue')
    plt.title(f'{channel_name} EEG Verisi ({start_time} saniye - {end_time} saniye)')
    plt.xlabel('Zaman (saniye)')
    plt.ylabel('EEG Amplitüdü')
    plt.legend()
    plt.show()

#if __name__ == "__main__":
   # plot_eeg_channel(eeg_file_path="data.edf", channel_name="Fp1", start_time=0, end_time=30)


if __name__ == "__main__":
    plot_eeg_channel(eeg_file_path="data.edf", channel_name="Fp1", start_time=10, end_time=15)
    plt.savefig('kanal_gorseli.jpg', format='jpg', dpi=300)
    


