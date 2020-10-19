from time import sleep

from behave import *
from hamcrest import *
from selenium.webdriver.common.keys import *

use_step_matcher("re")


@step("że uruchomiłem aplikację")
def step_impl(context):
    context.driver.get("http://18.197.162.204")
    sleep(4)


@step("na stronie aplikacji wpiszę (?P<WZROST>.+)")
def step_impl(context, WZROST):
    raise NotImplementedError(u'STEP: Jeżeli na stronie aplikacji wpiszę <WZROST>')


@step("wpiszę (?P<WAGA>.+)")
def step_impl(context, WAGA):
    raise NotImplementedError(u'STEP: I wpiszę <WAGA>')


@step("nacisnę przycisk Oblicz")
def step_impl(context):
    raise NotImplementedError(u'STEP: I nacisnę przycisk Oblicz')


@step("zobaczę wynik numerycznie: (?P<BMI_NUMERYCZNIE>.+)")
def step_impl(context, BMI_NUMERYCZNIE):
    actual_result = context.driver.find_element_by_xpath("//*[name()='svg']//*[name()='text' and @class='c3-gauge-value']").text
    assert_that(actual_result, equal_to(BMI_NUMERYCZNIE))


@step("zobaczę wynik słownie: (?P<BMI_SLOWNIE>.+)")
def step_impl(context, BMI_SLOWNIE):
    raise NotImplementedError(u'STEP: Oraz zobaczę wynik słownie: <BMI_SŁOWNIE>')