from flask import Blueprint, render_template, request, redirect, url_for
from . import mysql

main = Blueprint("main", __name__)

# Halaman utama: daftar semua buku
@main.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM buku")
    buku = cur.fetchall()
    cur.close()
    return render_template("index.html", buku=buku)

# Tambah buku
@main.route("/tambah", methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        judul = request.form["judul"]
        penulis = request.form["penulis"]
        tahun = request.form["tahun"]

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO buku (judul, penulis, tahun) VALUES (%s, %s, %s)",
            (judul, penulis, tahun)
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("main.index"))

    return render_template("tambah.html")

# Edit buku
@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cur = mysql.connection.cursor()

    if request.method == "POST":
        judul = request.form["judul"]
        penulis = request.form["penulis"]
        tahun = request.form["tahun"]

        cur.execute(
            "UPDATE buku SET judul=%s, penulis=%s, tahun=%s WHERE id=%s",
            (judul, penulis, tahun, id)
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("main.index"))

    # Tampilkan form edit dengan data buku
    cur.execute("SELECT * FROM buku WHERE id = %s", (id,))
    buku = cur.fetchone()
    cur.close()

    if not buku:
        return "Buku tidak ditemukan", 404

    return render_template("edit.html", buku=buku)

# Hapus buku
@main.route("/hapus/<int:id>", methods=["GET"])
def hapus(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM buku WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("main.index"))

# Detail buku
@main.route("/buku/<int:id>")
def show(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM buku WHERE id = %s", (id,))
    buku = cur.fetchone()
    cur.close()

    if not buku:
        return "Buku tidak ditemukan", 404

    return render_template("show.html", buku=buku)
