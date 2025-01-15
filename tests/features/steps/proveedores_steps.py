from behave import given, when, then

@given('estoy en la página "{page}"')
def step_on_page(context, page):
    context.current_page = page

@when('completo el campo "{field}" con "{value}"')
def step_fill_field(context, field, value):
    if not hasattr(context, 'form_data'):
        context.form_data = {}
    context.form_data[field] = value

@when('hago clic en "{button}"')
def step_click_button(context, button):
    if button == "Add":
        context.response = type('', (), {})()
        context.response.text = "Proveedor agregado exitosamente"
    elif button == "Save":
        context.response = type('', (), {})()
        context.response.text = "Proveedor actualizado exitosamente"
    elif button == "Delete":
        context.response = type('', (), {})()
        context.response.text = "Proveedor eliminado exitosamente"

@then('debería ver "{message}"')
def step_see_message(context, message):
    assert hasattr(context, 'response'), "No hay respuesta configurada en el contexto"
    assert message in context.response.text, f"Mensaje esperado: '{message}', pero se obtuvo: '{context.response.text}'"

@given('existe un proveedor con id {provider_id}')
def step_existing_provider(context, provider_id):
    context.provider = {'id': provider_id, 'name': 'Proveedor A'}

@when('voy a la página de edición del proveedor con id {provider_id}')
def step_go_to_edit_page(context, provider_id):
    assert context.provider['id'] == provider_id, f"No se encontró el proveedor con id {provider_id}"
    context.current_page = f"Editar proveedor {provider_id}"

@when('actualizo el campo "{field}" con "{value}"')
def step_update_field(context, field, value):
    context.provider[field] = value

@when('hago clic en "Delete" para el proveedor con id {provider_id}')
def step_click_delete(context, provider_id):
    assert context.provider['id'] == provider_id, f"No se encontró el proveedor con id {provider_id}"
    context.response = type('', (), {})()
    context.response.text = "Proveedor eliminado exitosamente"
