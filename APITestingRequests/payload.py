from Utilities.configurations import getQuery


def addbookpayload(isbn,aisle):
    body = {
        "name": "Learn Selenium with varun",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Varun Appalla"
    }
    return body


def buildPayLoadFromDB(query):

    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
