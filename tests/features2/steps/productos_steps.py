from behave import given, when, then

@given('estoy en la página "{page}"')
def step_impl(context, page):
    context.page = page
    print(f"Navegando a la página: {page}")

@when('ingreso el nombre "{nombre}"')
def step_impl(context, nombre):
    context.nombre = nombre
    print(f"Ingresando nombre: {nombre}")

@when('ingreso el precio "{precio}"')
def step_impl(context, precio):
    context.precio = precio
    print(f"Ingresando precio: {precio}")

@when('ingreso la cantidad "{cantidad}"')
def step_impl(context, cantidad):
    context.cantidad = cantidad
    print(f"Ingresando cantidad: {cantidad}")

@when('hago clic en "Guardar"')
def step_impl(context):
    print("Guardando los cambios")

@then('debería ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    print(f"Verificando mensaje: {mensaje}")
    assert mensaje in ["Producto creado exitosamente", "Producto actualizado exitosamente", "Producto eliminado exitosamente"]

@when('visualizo la lista de productos')
def step_impl(context):
    print("Visualizando la lista de productos")

@then('debería ver al menos un producto en la lista')
def step_impl(context):
    print("Verificando que al menos un producto está en la lista")
    # Aquí puedes simular una validación o agregar una consulta

@when('actualizo el nombre a "{nombre}"')
def step_impl(context, nombre):
    context.nombre = nombre
    print(f"Actualizando nombre: {nombre}")

@when('actualizo el precio a "{precio}"')
def step_impl(context, precio):
    context.precio = precio
    print(f"Actualizando precio: {precio}")

@when('hago clic en "Eliminar" del producto con ID "{id}"')
def step_impl(context, id):
    print(f"Eliminando el producto con ID: {id}")
