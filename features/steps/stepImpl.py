import requests
from behave import when, given, then

from APITestingRequests.payload import addbookpayload
from Utilities.Resources import ApiResources
from Utilities.configurations import getconfig, getAccessToken


@given('the book details needed to be added to library')
def step_impl(context):
    context.addbookurl = getconfig()['API']['endpoint'] + ApiResources.addbook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addbookpayload("fds", "32")


@given('the book details with {isbn} and {aisle} needed to be added to library')
def step_impl(context, isbn, aisle):
    context.addbookurl = getconfig()['API']['endpoint'] + ApiResources.addbook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addbookpayload(isbn, aisle)


@when('we execute addbookresp post method')
def step_impl(context):
    context.response = requests.post(context.addbookurl, json=context.payLoad, headers=context.headers, )


@then('book should be succesfully added to the library')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json["Msg"] == "successfully added"
