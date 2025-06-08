
# Bluetooth PIN Brute Force Tool

### **Purpose:**

This tool is designed to perform a brute-force attack on Bluetooth devices to attempt pairing by trying a list of PIN codes. It uses **Bluetooth Low Energy (BLE)** to find and connect to devices using their MAC addresses and a PIN list.

### **Features:**
- **Bluetooth device scanning**: Scans for nearby Bluetooth devices and displays their MAC addresses.
- **PIN Brute-Force Attack**: Attempts to pair with a Bluetooth device using multiple PIN codes from a wordlist file.
- **Cross-Platform Support**: Works on **Windows**, **Kali Linux**, and **VM Kali Linux**.
- **Error Handling**: Notifies the user of any connection or pairing issues.

### **How the Tool Works:**

1. **Scan Bluetooth Devices**: 
   The tool first scans for nearby Bluetooth devices and lists their MAC addresses and names.

2. **Load Wordlist**: 
   You can load a text file that contains a list of potential PINs to try for pairing.

3. **Brute Force Pairing**: 
   The tool attempts to pair with the target device using each PIN in the list. If successful, it will display the found PIN and stop.

---

## **Installation and Setup**

### 1. **System Requirements:**

- **Python 3.x** (Recommended: 3.7+)
- **`pip` package manager**
- Bluetooth adapter and drivers for your system

### 2. **Installation on Windows**:

1. **Install Python 3.x**:
   - Download Python from the official website: https://www.python.org/downloads/.
   - During installation, make sure to check **"Add Python to PATH"**.

2. **Install Dependencies**:
   Open a terminal or Command Prompt and install the required libraries:
   ```bash
   pip install bleak
   ```

3. **Run the Script**:
   After installing dependencies, simply run the `bluetooth_brute_force.py` script:
   ```bash
   python bluetooth_brute_force.py
   ```

---

### 3. **Installation on Kali Linux (or any Linux-based OS)**:

1. **Install Python 3.x**:
   Kali Linux typically comes with Python pre-installed, but you can ensure you have Python 3.x by running:
   ```bash
   python3 --version
   ```

2. **Install Dependencies**:
   First, ensure you have `pip` installed:
   ```bash
   sudo apt install python3-pip
   ```

   Then install the required packages:
   ```bash
   pip3 install bleak
   ```

3. **Run the Script**:
   Run the Python script using:
   ```bash
   python3 bluetooth_brute_force.py
   ```

---

### 4. **Installation on Kali Linux VM**:

Follow the same steps as on Kali Linux, ensuring that:
- The **Bluetooth adapter** is properly configured and recognized by the VM.
- The **Bluetooth service** is running inside the VM (this might require additional configuration, depending on the VM software).

1. **Install Python**:
   ```bash
   python3 --version
   ```

2. **Install Dependencies**:
   ```bash
   pip3 install bleak
   ```

3. **Run the Script**:
   ```bash
   python3 bluetooth_brute_force.py
   ```

---

## **Troubleshooting and Error Handling**

### 1. **Bluetooth Library Not Found (`ImportError`)**:

- Ensure that you have installed the necessary libraries (`bleak` for Windows, `pybluez` for Linux).
- If `bleak` is not installed, run:
  ```bash
  pip install bleak
  ```

### 2. **Permission Issues on Kali Linux**:

- Sometimes, you may face permission issues accessing Bluetooth devices on Kali Linux. Ensure that your user is in the `bluetooth` group:
  ```bash
  sudo usermod -aG bluetooth $USER
  sudo reboot
  ```

### 3. **Device Not Found**:

- Ensure the Bluetooth adapter is properly plugged in and recognized by your machine or VM.
- Check the device’s Bluetooth settings to make sure it is discoverable.

---

## **Usage Instructions**

1. **Launching the Tool**:
   - On Windows: Open the Command Prompt or PowerShell and run:
     ```bash
     python bluetooth_brute_force.py
     ```
   - On Kali Linux (or VM): Open the terminal and run:
     ```bash
     python3 bluetooth_brute_force.py
     ```

2. **GUI Interface**:
   - Enter the **target MAC address** of the Bluetooth device you want to attack in the input field labeled **"Target MAC Address (Bluetooth)"**.
   - Enter a list of **PIN codes** you want to try, one per line, in the **"Daftar PIN (satu per baris)"** field.
   - **Load Wordlist**: Click on **"Muat Wordlist dari File"** to load a list of PIN codes from a file.
   - **Start Brute Force**: Click **"Mulai Brute Force"** to start the brute force attack. The program will attempt each PIN on the target device.
   - **Scan Bluetooth Devices**: Click **"Scan Perangkat Bluetooth di Sekitar"** to scan for available Bluetooth devices and display their MAC addresses and names in the log.

3. **Log Output**:
   - The **log** will display each attempt to pair with the target device using the current PIN and show a success or failure message.
   - If a correct PIN is found, the tool will notify you with a success message.

---

## **Conclusion**

### **What this Tool Does**:
This tool is primarily intended for **security testing** and educational purposes to demonstrate how brute-force attacks work against Bluetooth PINs. It should only be used on devices you own or have explicit permission to test. Unauthorized access to devices is illegal.

### **How the Tool Works**:
1. The tool scans for nearby Bluetooth devices using `bleak` on Windows and `pybluez` on Linux.
2. It attempts to brute-force a Bluetooth pairing using a list of PINs provided by the user.
3. If a matching PIN is found, the program displays it, otherwise, it informs the user that no matching PINs were found.

### **Important Notes**:
- **Use Responsibly**: Only use this tool on devices you own or have explicit permission to test.
- **Bluetooth Low Energy (BLE)**: This tool uses BLE for pairing. Ensure the device supports BLE before running the tool.

---

## **Additional Resources**:

- **Python Bluetooth Libraries**:
  - [PyBluez](https://github.com/pybluez/pybluez) (for Linux)
  - [Bleak](https://github.com/hbldh/bleak) (for Windows and Linux)

---

# **Bluetooth PIN Brute Force**

### **Tujuan:**

Alat ini dirancang untuk melakukan serangan brute-force pada perangkat Bluetooth dengan mencoba berbagai kode PIN. Alat ini menggunakan **Bluetooth Low Energy (BLE)** untuk menemukan dan menghubungkan ke perangkat menggunakan alamat MAC dan daftar PIN.

### **Fitur:**
- **Pemindaian Perangkat Bluetooth**: Memindai perangkat Bluetooth di sekitar dan menampilkan alamat MAC serta nama perangkat.
- **Serangan Brute-Force PIN**: Mencoba memasangkan perangkat Bluetooth menggunakan berbagai PIN dari file wordlist.
- **Dukungan Multi-Platform**: Berfungsi di **Windows**, **Kali Linux**, dan **VM Kali Linux**.
- **Penanganan Error**: Memberikan pemberitahuan kepada pengguna jika terjadi masalah saat menghubungkan atau memasangkan perangkat.

### **Cara Kerja Alat Ini:**

1. **Memindai Perangkat Bluetooth**: 
   Alat ini pertama kali memindai perangkat Bluetooth yang ada di sekitar dan menampilkan alamat MAC serta nama perangkat.

2. **Muat Daftar Wordlist**: 
   Anda dapat memuat file teks yang berisi daftar PIN yang akan dicoba untuk memasangkan perangkat.

3. **Serangan Brute Force PIN**: 
   Alat ini akan mencoba memasangkan perangkat target menggunakan setiap PIN dalam daftar. Jika berhasil, alat akan menampilkan PIN yang ditemukan dan berhenti.

---

## **Instalasi dan Pengaturan**

### 1. **Persyaratan Sistem:**

- **Python 3.x** (Disarankan: 3.7+)
- **Manajer paket `pip`**
- **Adaptor Bluetooth** dan **driver Bluetooth** yang sesuai dengan sistem Anda.

### 2. **Instalasi di Windows**:

1. **Instal Python 3.x**:
   - Unduh Python dari situs web resmi: https://www.python.org/downloads/.
   - Pastikan untuk mencentang **"Add Python to PATH"** saat proses instalasi.

2. **Instalasi Dependensi**:
   Buka terminal atau Command Prompt dan instal pustaka yang diperlukan:
   ```bash
   pip install bleak
   ```

3. **Jalankan Skrip**:
   Setelah menginstal dependensi, jalankan skrip `bluetooth_brute_force.py` dengan perintah:
   ```bash
   python bluetooth_brute_force.py
   ```

---

### 3. **Instalasi di Kali Linux (atau sistem berbasis Linux lainnya)**:

1. **Instal Python 3.x**:
   Kali Linux biasanya sudah dilengkapi dengan Python, namun pastikan Anda memiliki Python 3.x dengan menjalankan:
   ```bash
   python3 --version
   ```

2. **Instalasi Dependensi**:
   Pastikan Anda sudah memiliki `pip` dengan menjalankan:
   ```bash
   sudo apt install python3-pip
   ```

   Kemudian instal pustaka yang diperlukan:
   ```bash
   pip3 install bleak
   ```

3. **Jalankan Skrip**:
   Jalankan skrip Python dengan perintah:
   ```bash
   python3 bluetooth_brute_force.py
   ```

---

### 4. **Instalasi di Kali Linux VM**:

Ikuti langkah-langkah yang sama seperti di Kali Linux, pastikan:
- **Adaptor Bluetooth** sudah terpasang dengan baik dan terdeteksi oleh sistem atau VM.
- **Layanan Bluetooth** sedang berjalan di dalam VM (ini mungkin memerlukan konfigurasi tambahan, tergantung pada perangkat lunak VM yang digunakan).

1. **Instal Python**:
   ```bash
   python3 --version
   ```

2. **Instal Dependensi**:
   ```bash
   pip3 install bleak
   ```

3. **Jalankan Skrip**:
   ```bash
   python3 bluetooth_brute_force.py
   ```

---

## **Penanganan Error dan Troubleshooting**

### 1. **Library Bluetooth Tidak Ditemukan (`ImportError`)**:

- Pastikan Anda telah menginstal pustaka yang diperlukan (`bleak` untuk Windows, `pybluez` untuk Linux).
- Jika `bleak` belum terinstal, jalankan:
  ```bash
  pip install bleak
  ```

### 2. **Masalah Izin di Kali Linux**:

- Kadang-kadang, Anda mungkin mengalami masalah izin saat mengakses perangkat Bluetooth di Kali Linux. Pastikan pengguna Anda sudah termasuk dalam grup `bluetooth`:
  ```bash
  sudo usermod -aG bluetooth $USER
  sudo reboot
  ```

### 3. **Perangkat Tidak Ditemukan**:

- Pastikan **Adaptor Bluetooth** terpasang dengan baik dan terdeteksi oleh sistem atau VM Anda.
- Periksa pengaturan Bluetooth perangkat untuk memastikan perangkat dapat ditemukan (discoverable).

---

## **Instruksi Penggunaan**

1. **Menjalankan Alat**:
   - Di Windows: Buka **Command Prompt** atau **PowerShell** dan jalankan:
     ```bash
     python bluetooth_brute_force.py
     ```
   - Di Kali Linux (atau VM): Buka terminal dan jalankan:
     ```bash
     python3 bluetooth_brute_force.py
     ```

2. **Antarmuka GUI**:
   - Masukkan **alamat MAC perangkat target** yang ingin Anda serang di kolom **"Target MAC Address (Bluetooth)"**.
   - Masukkan daftar **PIN** yang ingin Anda coba, satu PIN per baris, di kolom **"Daftar PIN (satu per baris)"**.
   - **Muat Wordlist**: Klik **"Muat Wordlist dari File"** untuk memuat daftar PIN dari file.
   - **Mulai Brute Force**: Klik **"Mulai Brute Force"** untuk memulai serangan brute force. Alat ini akan mencoba setiap PIN pada perangkat target.
   - **Pindai Perangkat Bluetooth**: Klik **"Scan Perangkat Bluetooth di Sekitar"** untuk memindai perangkat Bluetooth yang tersedia dan menampilkan alamat MAC serta nama perangkat di log.

3. **Output Log**:
   - **Log** akan menampilkan setiap upaya untuk memasangkan perangkat dengan PIN yang sedang dicoba dan memberikan pesan sukses atau gagal.
   - Jika PIN yang cocok ditemukan, alat akan memberi pemberitahuan dengan pesan sukses.

---

## **Kesimpulan**

### **Apa yang Dilakukan Alat Ini**:
Alat ini terutama dimaksudkan untuk **pengujian keamanan** dan **tujuan edukasi** untuk menunjukkan bagaimana serangan brute-force bekerja pada PIN Bluetooth. Gunakan alat ini hanya pada perangkat yang Anda miliki atau memiliki izin eksplisit untuk mengujinya. Akses tanpa izin terhadap perangkat adalah ilegal.

### **Cara Kerja Alat Ini**:
1. Alat ini memindai perangkat Bluetooth di sekitar menggunakan `bleak` di Windows dan `pybluez` di Linux.
2. Alat ini mencoba brute-force memasangkan perangkat dengan berbagai PIN dari daftar yang diberikan.
3. Jika menemukan PIN yang cocok, alat ini akan menampilkannya, jika tidak, memberi tahu bahwa tidak ada PIN yang cocok ditemukan.

### **Catatan Penting**:
- **Gunakan Secara Bertanggung Jawab**: Gunakan alat ini hanya pada perangkat yang Anda miliki atau memiliki izin eksplisit untuk mengujinya.
- **Bluetooth Low Energy (BLE)**: Alat ini menggunakan BLE untuk pemasangan. Pastikan perangkat yang Anda uji mendukung BLE sebelum menjalankan alat ini.

---

## **Sumber Daya Tambahan**:

- **Pustaka Bluetooth Python**:
  - [PyBluez](https://github.com/pybluez/pybluez) (untuk Linux)
  - [Bleak](https://github.com/hbldh/bleak) (untuk Windows dan Linux)
