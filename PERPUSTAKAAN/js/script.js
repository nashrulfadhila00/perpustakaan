// script.js

// Fungsi untuk memvalidasi formulir tambah buku
function validasiForm() {
    const judul = document.getElementById('judul').value.trim();
    const penulis = document.getElementById('penulis').value.trim();
    const tahun = document.getElementById('tahun').value.trim();

    if (!judul || !penulis || !tahun) {
        alert("Semua kolom harus diisi!");
        return false;
    }

    if (isNaN(tahun) || tahun.length !== 4) {
        alert("Tahun harus berupa angka 4 digit.");
        return false;
    }

    return true;
}

// Fungsi untuk menampilkan konfirmasi sebelum menghapus buku
function konfirmasiHapus(judul) {
    return confirm(`Apakah Anda yakin ingin menghapus buku "${judul}"?`);
}
