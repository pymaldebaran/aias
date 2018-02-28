from pytest_bdd import (
    scenario,
    given,
    when,
    then)

@scenario('enter_the_shell.feature', 'Entering in the shell')
def test_entering_in_the_shell():
    pass

@given('I am a player')
def player():
    return 'Ze player'
    
@when('I enter the shell')
def enter_shell():
    pass
    
@then('I have a character')
def have_character():
    assert True
    
@then('I have a scenario')
def have_scenario():
    assert True

