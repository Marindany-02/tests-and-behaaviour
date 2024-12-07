from behave import when, then
from selenium.webdriver.common.by import By

@when('I click the "{button}" button')
def step_impl(context, button):
    button_element = context.driver.find_element(By.XPATH, f"//button[text()='{button}']")
    button_element.click()

@then('I should see the message "{message}"')
def step_impl(context, message):
    body = context.driver.find_element(By.TAG_NAME, 'body')
    assert message in body.text

@then('I should not see the message "{message}"')
def step_impl(context, message):
    body = context.driver.find_element(By.TAG_NAME, 'body')
    assert message not in body.text

