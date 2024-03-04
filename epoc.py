import mne
import matplotlib.pyplot as plt

def plot_eeg_channel(eeg_file_path="data.edf", channel_name="Fp1"):
    # EEG verisini oku
    raw = mne.io.read_raw_edf(eeg_file_path, preload=True)

    # Örnekleme frekansını al
    sampling_freq = raw.info['sfreq']

    # Toplam kayıt süresini al
    recording_duration = raw.times[-1]

    # Zaman aralığını hesapla
    time_interval = 30 / sampling_freq

    print(f"Örnekleme Frekansı: {sampling_freq} Hz")
    print(f"Toplam Kayıt Süresi: {recording_duration} saniye")
    print(f"Zaman Aralığı: {time_interval} saniye")

    # Belirli bir kanaldaki veriyi seç
    eeg_data, times = raw[channel_name, :]

    # EEG verisini çiz
    plt.figure(figsize=(10, 4))
    plt.plot(times, eeg_data[0], label=f'{channel_name} EEG Verisi', color='blue')
    plt.title(f'{channel_name} EEG Verisi Semra')
    plt.xlabel('Zaman (saniye)')
    plt.ylabel('EEG Amplitüdü')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_eeg_channel(eeg_file_path="data.edf", channel_name="Fp1")
