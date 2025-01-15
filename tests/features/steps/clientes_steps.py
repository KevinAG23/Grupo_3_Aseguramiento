from behave import given, when, then

@given('estoy en la página "{page}"')
def step_on_page(context, page):
    # Simulación de estar en una página
    context.current_page = page

@when('completo el campo "{field}" con "{value}"')
def step_fill_field(context, field, value):
    # Simulación de completar un campo
    if not hasattr(context, 'form_data'):
        context.form_data = {}
    context.form_data[field] = value

@when('hago clic en "{button}"')
def step_click_button(context, button):
    # Simulación de clic en un botón
    if button == "Add":
        context.response = type('', (), {})()  # Crear un objeto simulado
        context.response.text = "Cliente agregado exitosamente"
    elif button == "Save":
        context.response = type('', (), {})()
        context.response.text = "Cliente actualizado exitosamente"
    elif button == "Delete":
        context.response = type('', (), {})()
        context.response.text = "Cliente eliminado exitosamente"

@then('debería ver "{message}"')
def step_see_message(context, message):
    # Verificación de mensaje en la respuesta
    assert hasattr(context, 'response'), "No hay respuesta configurada en el contexto"
    assert message in context.response.text, f"Mensaje esperado: '{message}', pero se obtuvo: '{context.response.text}'"

@given('existe un cliente con id {client_id}')
def step_existing_client(context, client_id):
    # Simulación de existencia de un cliente
    context.client = {'id': client_id, 'name': 'John Doe'}

@when('voy a la página de edición del cliente con id {client_id}')
def step_go_to_edit_page(context, client_id):
    # Simulación de navegación a la página de edición
    assert context.client['id'] == client_id, f"No se encontró el cliente con id {client_id}"
    context.current_page = f"Editar cliente {client_id}"

@when('actualizo el campo "{field}" con "{value}"')
def step_update_field(context, field, value):
    # Simulación de actualización de campo
    context.client[field] = value

@when('hago clic en "Delete" para el cliente con id {client_id}')
def step_click_delete(context, client_id):
    # Simulación de clic en "Delete"
    assert context.client['id'] == client_id, f"No se encontró el cliente con id {client_id}"
    context.response = type('', (), {})()
    context.response.text = "Cliente eliminado exitosamente"
