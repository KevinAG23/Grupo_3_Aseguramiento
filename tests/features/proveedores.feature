Feature: CRUD de Proveedores
  Como usuario
  Quiero gestionar proveedores
  Para mantener actualizada la lista de proveedores

  Scenario: Agregar un proveedor
    Given estoy en la página "add proveedor"
    When completo el campo "name" con "Proveedor A"
    And completo el campo "contact" con "contact@proveedor.com"
    And hago clic en "Add"
    Then debería ver "Proveedor agregado exitosamente"

  Scenario: Editar un proveedor existente
    Given existe un proveedor con id 1
    When voy a la página de edición del proveedor con id 1
    And actualizo el campo "name" con "Proveedor B"
    And hago clic en "Save"
    Then debería ver "Proveedor actualizado exitosamente"

  Scenario: Eliminar un proveedor
    Given existe un proveedor con id 1
    When hago clic en "Delete" para el proveedor con id 1
    Then debería ver "Proveedor eliminado exitosamente"
