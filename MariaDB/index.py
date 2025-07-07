import mariadb
import sys

from numpy.ma.core import product

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        port=8889,
        database="python_mariadb"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cursor = conn.cursor()

# # Yeni tablo oluşturma
# try:
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS product (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(100) NOT NULL,
#             price INT NOT NULL,
#             description TEXT,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#     """)
#     print("Tablo başarıyla oluşturuldu.")
# except mariadb.Error as e:
#     print(f"Tablo oluşturulurken hata oluştu: {e}")



### Veri ekleme
# try:
#     cursor.execute("INSERT INTO product(name, price, description) VALUES (?,?,?)",
#                    ("Product 1", 1500, "Product 1 description"))
#     conn.commit()
# except mariadb.Error as e:
#     print(f"Veri eklenirken hata oluştu: {e}")




### İlişkili Tablo Oluşturma
# Yeni tablo: productDetail
# try:
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS productDetail (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             product_id INT NOT NULL,
#             tax_rate DECIMAL(5,2),
#             profit_margin DECIMAL(5,2),
#             stock_quantity INT,
#             FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
#         )
#     """)
#     print("productDetail tablosu başarıyla oluşturuldu.")
# except mariadb.Error as e:
#     print(f"productDetail tablosu oluşturulurken hata oluştu: {e}")





### İlişkili Veri Ekleme
# try:
#     cursor.execute("INSERT INTO product(name, price, description) VALUES (?,?,?)", ("Product 6", 6000, "Product 6 description"))
#     productId = cursor.lastrowid  # Son eklenen ürünün ID'sini al
#
#
#     cursor.execute("INSERT INTO productDetail(product_id, tax_rate, profit_margin, stock_quantity) VALUES (?,?,?,?)", (productId, 18.00, 25.00, 100))
#     conn.commit()
# except mariadb.Error as err:
#     print(f"Veri eklenirken hata oluştu: {err}")




### Güncelleme İşlemi
# try:
#     cursor.execute("UPDATE product SET name = ?, price = ?, description = ? WHERE id = ?", ("Product 3", 2500, "Product 3 Description", 4))
#     conn.commit()
# except mariadb.Error as err:
#     print(f"Güncelleme işlemi sırasında hata oluştu: {err}")





### İlişkili Güncelleme İşlemi
# try:
#     productId = 5
#     cursor.execute("UPDATE product SET name = ?, price = ?, description = ? WHERE id = ?", ("Product 4", 4500, "Product 4 Description", productId))
#     cursor.execute("UPDATE productDetail SET tax_rate = ?, profit_margin = ?, stock_quantity = ? WHERE product_id = ?", (20.00, 30.00, 150, productId))
#     conn.commit()
# except mariadb.Error as err:
#     print(f"Güncelleme işlemi sırasında hata oluştu: {err}")




### Silme İşlemi
# try:
#     cursor.execute("DELETE FROM product WHERE id = ?", (9,))
#     conn.commit()
# except mariadb.Error as err:
#     print(f"Silme işlemi sırasında hata oluştu: {err}")