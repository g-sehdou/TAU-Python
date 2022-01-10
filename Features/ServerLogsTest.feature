# Created by gsehdou at 04/01/2022
Feature: Check server logs
  # Enter feature description here

  Scenario: Validate that there is no error in the server log
    Given Open the error log file
    When Search for errors in the log file
    Then There are no errors found

  Scenario: Validate that the amount of warnings are less than 100
    Given Open the error log file
    When Search for warning in the log file
    Then The warning are less than 100

  Scenario: Validate that there is no default (0) in the Prepare Alert csv file
    Given Open the csv file prepare alert
    When Search for default value 0 in Prepare Alert CSV file
    Then The prepare alert csv contains no default value 0

"""
   Scenario: Validate that there is no default (0) in the Alert Feedback csv file
     Given Open the csv file Alert Feedback
     When Search for default value 0 in Alert Feedback CSV file
     Then The alert feedback csv contains no default value 0
"""


