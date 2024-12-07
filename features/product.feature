
 Scenario: Read a product
    Given a product with name "Test Product" and price "10"
    When I view the product details
    Then I should see the product details

  Scenario: Update a product
    Given a product with name "Test Product" and price "10"
    When I update the product with name "Updated Product" and price "20"
    Then I should see the updated product details

  Scenario: Delete a product
    Given a product with name "Test Product" and price "10"
    When I delete the product
    Then the product should be deleted

  Scenario: List all products
    Given there are products in the database
    When I list all products
    Then I should see a list of all products

  Scenario: Search by category
    Given a product with name "Test Product" and category "Test Category"
    When I search for products by category "Test Category"
    Then I should see products in that category

  Scenario: Search by availability
    Given a product with name "Test Product" and availability "In Stock"
    When I search for products by availability "In Stock"
    Then I should see products that are in stock

  Scenario: Search by name
    Given a product with name "Test Product"
    When I search for products by name "Test Product"
    Then I should see the product with that name

