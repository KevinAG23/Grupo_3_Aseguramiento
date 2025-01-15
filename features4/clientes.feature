Feature: CRUD de Clientes
  Como usuario
  Quiero gestionar clientes
  Para mantener la información actualizada

  Scenario: Agregar un cliente
    Given estoy en la página "add cliente"
    When completo el campo "name" con "John Doe"
    And completo el campo "email" con "john@example.com"
    And completo el campo "phone" con "123456789"
    And hago clic en "Add"
    Then debería ver "Cliente agregado exitosamente"

  Scenario: Editar un cliente existente
    Given existe un cliente con id 1
    When voy a la página de edición del cliente con id 1
    And actualizo el campo "name" con "Jane Doe"
    And hago clic en "Save"
    Then debería ver "Cliente actualizado exitosamente"

  Scenario: Eliminar un cliente
    Given existe un cliente con id 1
    When hago clic en "Delete" para el cliente con id 1
    Then debería ver "Cliente eliminado exitosamente"
