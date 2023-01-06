from Utilities.Resources import ApiResources
from Utilities.configurations import getconfig
import requests


def after_scenario(context, scenario):
    if "library" in scenario.tags:  # for preventing from running hook error
        # for other feature files where environment file execution is not required.

        deletebookurl = getconfig()['API']['endpoint'] + ApiResources.deletebook
        delebookresp = requests.post(deletebookurl, json={
            "ID": context.bookId}, headers={"Content-Type": "application/json"})

        print(delebookresp.text)
        assert delebookresp.status_code == 200
        res_json = delebookresp.json()

        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"
