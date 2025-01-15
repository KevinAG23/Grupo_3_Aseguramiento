Feature: Gestión de productos
  Como administrador
  Quiero gestionar productos
  Para mantener actualizada la base de datos de productos

  Scenario: Crear un producto
    Given estoy en la página "productos/crear"
    When ingreso el nombre "Laptop"
    And ingreso el precio "1500"
    And ingreso la cantidad "10"
    And hago clic en "Guardar"
    Then debería ver el mensaje "Producto creado exitosamente"

  Scenario: Leer productos
    Given estoy en la página "productos"
    When visualizo la lista de productos
    Then debería ver al menos un producto en la lista

  Scenario: Actualizar un producto
    Given estoy en la página "productos/editar/1"
    When actualizo el nombre a "Laptop Pro"
    And actualizo el precio a "2000"
    And hago clic en "Guardar"
    Then debería ver el mensaje "Producto actualizado exitosamente"

  Scenario: Eliminar un producto
    Given estoy en la página "productos"
    When hago clic en "Eliminar" del producto con ID "1"
    Then debería ver el mensaje "Producto eliminado exitosamente"
