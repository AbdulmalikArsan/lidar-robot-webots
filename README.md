# LiDAR Object Avoidant Robot in Webots

Simulasi robot otonom penghindar rintangan (*obstacle avoidance*) berbasis sensor **LiDAR** menggunakan simulator **Webots** dan bahasa pemrograman **Python**.

![Preview Simulasi](worlds/.lidarCapsul.jpg)

## Cara Kerja Algoritma
1. **Pembagian Sektor LiDAR**: Resolusi horizontal data jarak LiDAR (`getRangeImage`) dibagi menjadi 3 sektor utama, yaitu **Kanan**, **Depan**, dan **Kiri**, lalu diambil jarak rintangan terdekat yang valid pada masing-masing sektor.
2. **Deteksi Jarak Aman**: Robot menggunakan batas jarak aman (`SAFE_DISTANCE`) sebesar **0.5 meter** dengan kecepatan maksimum motor (`MAX_SPEED`) **6.28 rad/s**.
3. **Logika Penghindar Rintangan**:
   - **Jalur Aman**: Jika jarak depan >= 0.5m, robot melaju lurus dengan kecepatan penuh (`1.0 * MAX_SPEED`).
   - **Rintangan di Depan**: Robot membandingkan jarak kiri dan kanan, lalu berputar di tempat (`0.5 * MAX_SPEED`) menuju sisi yang lebih luas.
4. **Monitoring Real-Time**: Konsol Webots menampilkan log jarak tiap sektor dalam satuan meter beserta status aksi robot secara *real-time*.

## Konfigurasi Perangkat Robot
- **Aktuator**: 2 motor roda diferensial (`motor_kanan` dan `motor_kiri`) dalam mode kontrol kecepatan.
- **Sensor**: 1 unit sensor `lidar` untuk pemindaian jarak rintangan di sekitar robot.

## Cara Menjalankan Simulasi
1. Clone repository ini ke komputer Anda:
   ```bash
   git clone https://github.com
   ```
2. Buka aplikasi **Webots**.
3. Pilih menu **File > Open World...**, lalu buka file `worlds/lidarCapsul.wbt`.
4. Pastikan *controller* robot sudah terhubung ke `lidarCapsul`, lalu klik tombol **Play** untuk memulai simulasi.
