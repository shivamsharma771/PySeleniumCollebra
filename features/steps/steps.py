from behave import *
from selenium import webdriver
from hamcrest import equal, contains, equal_to

path = r'C:\Users\hp\Downloads\chromedriver.exe'
browserobject = webdriver(path)
urltolaunch = browserobject("https://signup.gradright.com/?redirect_uri=https://gradright.com")


@given('launch the GradRight signup page')
def step_impl(context):
    path = r'C:\Users\hp\Downloads\chromedriver.exe'
    browserobject = webdriver(path)
    urltolaunch = browserobject("https://signup.gradright.com/?redirect_uri=https://gradright.com")
    launchBrowser = browserobject.get(urltolaunch)

@Then('Verify if signup is present on the form')
def step_impl():
    signupobject = driver.findElement(By.xpath("//*[@id="user_options-forms"]/div/form/div[1]/h2(text()")
    assert.value(signupobject, equal_to, ("equal_to"))

@Then('')

