from time import sleep

from behave import *
from hamcrest import *

use_step_matcher("re")


@step("że uruchomiłem aplikację")
def step_impl(context):
    context.driver.get("http://18.197.162.204")


@step("na stronie aplikacji wpiszę (?P<WZROST>.+)")
def step_impl(context, WZROST):
    pole_wzrost = context.driver.find_element_by_xpath("//input[@id='wzrost']")
    pole_wzrost.clear()
    pole_wzrost.send_keys(WZROST)


@step("wpiszę (?P<WAGA>.+)")
def step_impl(context, WAGA):
    pole_wzrost = context.driver.find_element_by_xpath("//input[@id='waga']")
    pole_wzrost.clear()
    pole_wzrost.send_keys(WAGA)


@step("nacisnę przycisk Oblicz")
def step_impl(context):
    przycisk_oblicz = context.driver.find_element_by_xpath("//button")
    przycisk_oblicz.click()


@step("zobaczę wynik numerycznie: (?P<BMI_NUMERYCZNIE>.+)")
def step_impl(context, BMI_NUMERYCZNIE):
    actual_result = context.driver.find_element_by_xpath("//*[name()='svg']//*[name()='text' and @class='c3-gauge-value']").text
    assert_that(actual_result, equal_to(BMI_NUMERYCZNIE))


@step("zobaczę wynik słownie: (?P<BMI_SLOWNIE>.+)")
def step_impl(context, BMI_SLOWNIE):
    actual_result = context.driver.find_element_by_xpath('//h4').text
    assert_that(actual_result, equal_to(BMI_SLOWNIE))
    sleep(3)

