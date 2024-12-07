Scenario: Reading a product
  Given the product "Test Product" exists
  When I fetch the product by ID
  Then the product name should be "Test Product"
