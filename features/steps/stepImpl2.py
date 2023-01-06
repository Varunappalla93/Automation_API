import requests
from behave import given, when, then

from Utilities import Resources
from Utilities.Resources import ApiResources
from Utilities.configurations import getAccessToken


@given(u'I have github credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ("V@runappalla93", getAccessToken())


@when(u'I execute github repo API of git')
def step_impl(context):
    context.gitresp2 = context.se.get(ApiResources.githubrepo)


@then(u'status code should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.gitresp2.text)
    print(context.gitresp2.status_code)
    assert context.gitresp2.status_code == statusCode
