Feature: Verify if books are added and deleted using Library API

  @library
  Scenario: Verify add book api functionality
    Given the book details needed to be added to library
    When we execute addbookresp post method
    Then book should be succesfully added to the library

  @library
  Scenario Outline: Verify add book api functionality
    Given the book details with <isbn> and <aisle> needed to be added to library
    When we execute addbookresp post method
    Then book should be succesfully added to the library
    Examples:
      | isbn | aisle |
      | var  |32     |
      |gdfg  |54     |


# to run that feature , use behave features/BookAPI.feature --no-capture is used to run logs.
# to run only set of test cases, use tags, eg: behave features/BookAPI.feature --no-capture --tags=smoke

# to use allure reports , use behave features --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# to generate reports - allure serve <allure reports path>



