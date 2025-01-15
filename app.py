from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# ----------------------------
# CRUD para Clientes
# ----------------------------
@app.route('/clientes')
def clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Clients')
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('clientes.html', clientes=clientes)

@app.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Clients (name, email, phone) VALUES (?, ?, ?)', 
                       (name, email, phone))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('clientes'))
    return render_template('add_cliente.html')

@app.route('/edit_cliente/<int:id>', methods=['GET', 'POST'])
def edit_cliente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cursor.execute('UPDATE Clients SET name = ?, email = ?, phone = ? WHERE id = ?', 
                       (name, email, phone, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('clientes'))

    cursor.execute('SELECT * FROM Clients WHERE id = ?', (id,))
    cliente = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit_cliente.html', cliente=cliente)

@app.route('/delete_cliente/<int:id>')
def delete_cliente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Clients WHERE id = ?', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('clientes'))

# ----------------------------
# CRUD para Proveedores
# ----------------------------
@app.route('/proveedores')
def proveedores():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Providers')
    proveedores = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('proveedores.html', proveedores=proveedores)

@app.route('/add_proveedor', methods=['GET', 'POST'])
def add_proveedor():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        company_name = request.form['company_name']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Providers (name, email, phone, address, company_name) '
                       'VALUES (?, ?, ?, ?, ?)', 
                       (name, email, phone, address, company_name))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('proveedores'))
    return render_template('add_proveedor.html')

@app.route('/edit_proveedor/<int:id>', methods=['GET', 'POST'])
def edit_proveedor(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        company_name = request.form['company_name']
        cursor.execute('UPDATE Providers SET name = ?, email = ?, phone = ?, address = ?, company_name = ? '
                       'WHERE id = ?', (name, email, phone, address, company_name, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('proveedores'))

    cursor.execute('SELECT * FROM Providers WHERE id = ?', (id,))
    proveedor = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit_proveedor.html', proveedor=proveedor)

@app.route('/delete_proveedor/<int:id>')
def delete_proveedor(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Providers WHERE id = ?', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('proveedores'))

# ----------------------------
# CRUD para Productos
# ----------------------------
@app.route('/productos')
def productos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT Products.id, Products.name, Products.description, Products.price, Products.stock, Providers.name '
                   'FROM Products JOIN Providers ON Products.provider_id = Providers.id')
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('productos.html', productos=productos)

@app.route('/add_producto', methods=['GET', 'POST'])
def add_producto():
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        provider_id = request.form['provider_id']

        cursor = conn.cursor()
        cursor.execute('INSERT INTO Products (name, description, price, stock, provider_id) '
                       'VALUES (?, ?, ?, ?, ?)', 
                       (name, description, price, stock, provider_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('productos'))

    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM Providers')
    providers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('add_producto.html', providers=providers)

@app.route('/edit_producto/<int:id>', methods=['GET', 'POST'])
def edit_producto(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        provider_id = request.form['provider_id']
        cursor.execute('UPDATE Products SET name = ?, description = ?, price = ?, stock = ?, provider_id = ? '
                       'WHERE id = ?', (name, description, price, stock, provider_id, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('productos'))

    cursor.execute('SELECT * FROM Products WHERE id = ?', (id,))
    producto = cursor.fetchone()

    cursor.execute('SELECT id, name FROM Providers')
    providers = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('edit_producto.html', producto=producto, providers=providers)

@app.route('/delete_producto/<int:id>')
def delete_producto(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Products WHERE id = ?', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('productos'))

# ----------------------------
# CRUD para Pedidos
# ----------------------------
@app.route('/pedidos')
def pedidos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT Orders.id, Clients.name, Orders.order_date, Orders.total_amount '
                   'FROM Orders JOIN Clients ON Orders.client_id = Clients.id')
    pedidos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('pedidos.html', pedidos=pedidos)

@app.route('/add_pedido', methods=['GET', 'POST'])
def add_pedido():
    conn = get_db_connection()
    if request.method == 'POST':
        client_id = request.form['client_id']
        product_id = request.form['product_id']
        quantity = int(request.form['quantity'])
        order_date = request.form['order_date']

        # Consultar el precio del producto
        cursor = conn.cursor()
        cursor.execute('SELECT price FROM Products WHERE id = ?', (product_id,))
        product = cursor.fetchone()
        if product is None:
            cursor.close()
            conn.close()
            return "Producto no encontrado", 404

        price = product[0]
        total_amount = price * quantity

        # Insertar el pedido en la base de datos
        cursor.execute(
            'INSERT INTO Orders (client_id, product_id, quantity, order_date, total_amount) '
            'VALUES (?, ?, ?, ?, ?)', 
            (client_id, product_id, quantity, order_date, total_amount)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('pedidos'))

    # Consultar clientes y productos para el formulario
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM Clients')
    clients = cursor.fetchall()

    cursor.execute('SELECT id, name FROM Products')
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('add_pedido.html', clients=clients, products=products)


@app.route('/edit_pedido/<int:id>', methods=['GET', 'POST'])
def edit_pedido(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        client_id = request.form['client_id']
        product_id = request.form['product_id']
        quantity = int(request.form['quantity'])
        order_date = request.form['order_date']

        # Consultar el precio del producto
        cursor.execute('SELECT price FROM Products WHERE id = ?', (product_id,))
        product = cursor.fetchone()
        if product is None:
            cursor.close()
            conn.close()
            return "Producto no encontrado", 404

        price = product[0]
        total_amount = price * quantity

        # Actualizar el pedido
        cursor.execute(
            'UPDATE Orders SET client_id = ?, product_id = ?, quantity = ?, order_date = ?, total_amount = ? '
            'WHERE id = ?',
            (client_id, product_id, quantity, order_date, total_amount, id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('pedidos'))

    # Obtener el pedido actual
    cursor.execute('SELECT * FROM Orders WHERE id = ?', (id,))
    pedido = cursor.fetchone()
    if not pedido:
        cursor.close()
        conn.close()
        return "Pedido no encontrado", 404

    # Obtener clientes y productos para los selectores
    cursor.execute('SELECT id, name FROM Clients')
    clients = cursor.fetchall()

    cursor.execute('SELECT id, name FROM Products')
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    # Renderizar el formulario con los datos existentes
    return render_template('edit_pedido.html', pedido=pedido, clients=clients, products=products)


@app.route('/delete_pedido/<int:id>')
def delete_pedido(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Orders WHERE id = ?', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('pedidos'))

if __name__ == '__main__':
    app.run(debug=True)

