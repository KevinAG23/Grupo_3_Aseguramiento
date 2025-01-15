Feature: Gestión de pedidos
  Como administrador
  Quiero gestionar pedidos
  Para mantener actualizada la base de datos de pedidos

  Scenario: Crear un pedido
    Given estoy en la página "pedidos/crear"
    When ingreso el ID del cliente "123"
    And ingreso la fecha "2025-01-15"
    And agrego el producto "Laptop" con cantidad "2"
    And hago clic en "Guardar"
    Then debería ver el mensaje "Pedido creado exitosamente"

  Scenario: Leer pedidos
    Given estoy en la página "pedidos"
    When visualizo la lista de pedidos
    Then debería ver al menos un pedido en la lista

  Scenario: Actualizar un pedido
    Given estoy en la página "pedidos/editar/1"
    When actualizo el ID del cliente a "124"
    And actualizo la fecha a "2025-01-16"
    And actualizo la cantidad del producto "Laptop" a "3"
    And hago clic en "Guardar"
    Then debería ver el mensaje "Pedido actualizado exitosamente"

  Scenario: Eliminar un pedido
    Given estoy en la página "pedidos"
    When hago clic en "Eliminar" del pedido con ID "1"
    Then debería ver el mensaje "Pedido eliminado exitosamente"
