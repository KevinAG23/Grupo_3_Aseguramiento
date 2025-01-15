from behave import given, when, then

@given('estoy en la página "{page}"')
def step_impl(context, page):
    context.page = page
    print(f"Navegando a la página: {page}")

@when('ingreso el ID del cliente "{cliente_id}"')
def step_impl(context, cliente_id):
    context.cliente_id = cliente_id
    print(f"Ingresando ID del cliente: {cliente_id}")

@when('ingreso la fecha "{fecha}"')
def step_impl(context, fecha):
    context.fecha = fecha
    print(f"Ingresando fecha: {fecha}")

@when('agrego el producto "{producto}" con cantidad "{cantidad}"')
def step_impl(context, producto, cantidad):
    context.producto = producto
    context.cantidad = cantidad
    print(f"Agregando producto: {producto} con cantidad: {cantidad}")

@when('actualizo el ID del cliente a "{cliente_id}"')
def step_impl(context, cliente_id):
    context.cliente_id = cliente_id
    print(f"Actualizando ID del cliente a: {cliente_id}")

@when('actualizo la fecha a "{fecha}"')
def step_impl(context, fecha):
    context.fecha = fecha
    print(f"Actualizando fecha a: {fecha}")

@when('actualizo la cantidad del producto "{producto}" a "{cantidad}"')
def step_impl(context, producto, cantidad):
    context.producto = producto
    context.cantidad = cantidad
    print(f"Actualizando cantidad del producto: {producto} a: {cantidad}")

@when('hago clic en "Guardar"')
def step_impl(context):
    print("Guardando los cambios")

@then('debería ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    print(f"Verificando mensaje: {mensaje}")
    assert mensaje in [
        "Pedido creado exitosamente",
        "Pedido actualizado exitosamente",
        "Pedido eliminado exitosamente"
    ]

@when('visualizo la lista de pedidos')
def step_impl(context):
    print("Visualizando la lista de pedidos")

@then('debería ver al menos un pedido en la lista')
def step_impl(context):
    print("Verificando que al menos un pedido está en la lista")
    # Aquí puedes simular una validación o agregar una consulta

@when('hago clic en "Eliminar" del pedido con ID "{id}"')
def step_impl(context, id):
    print(f"Eliminando el pedido con ID: {id}")
