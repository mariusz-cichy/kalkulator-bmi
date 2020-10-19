from lettuce import step, world


@step("że uruchomiłem aplikację")
def step_impl(step_instance):
    """
    :type step_instance: lettuce.core.Step
    """
    raise NotImplementedError(u'STEP: Zakładając że uruchomiłem aplikację')


@step("na stronie aplikacji wpiszę (?P<WZROST>.+) w pole wzrost")
def step_impl(step_instance, WZROST):
    """
    :type step_instance: lettuce.core.Step
    :type WZROST: str
    """
    raise NotImplementedError(u'STEP: Jeżeli na stronie aplikacji wpiszę <WZROST> w pole wzrost')


@step("wpiszę (?P<WAGA>.+) w pole waga")
def step_impl(step_instance, WAGA):
    """
    :type step_instance: lettuce.core.Step
    :type WAGA: str
    """
    raise NotImplementedError(u'STEP: I wpiszę <WAGA> w pole waga')


@step("nacisnę przycisk Oblicz")
def step_impl(step_instance):
    """
    :type step_instance: lettuce.core.Step
    """
    raise NotImplementedError(u'STEP: I nacisnę przycisk Oblicz')


@step("powinienem zobaczyć (.+) jako wartość numeryczną BMI")
def step_impl(step_instance, arg0):
    """
    :type step_instance: lettuce.core.Step
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: Wtedy powinienem zobaczyć <BMI_LICZBOWO > jako wartość numeryczną BMI')


@step("(.+) jako kategorię przedziału BMI")
def step_impl(step_instance, arg0):
    """
    :type step_instance: lettuce.core.Step
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: I <BMI_SŁOWNIE> jako kategorię przedziału BMI')