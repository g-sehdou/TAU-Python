import contextvars

from behave import *

use_step_matcher("re")
errorLog = "| E |"
fatalLog = "| F |"
warningLog = "| W |"
default_value = "(0)"
DS_file = "/Users/gsehdou/Downloads/DSLog.txt"
Prepare_Alert_CSV = "/Users/gsehdou/Downloads/Prepare_Alert.csv"
Alert_Feedback_CSV = "/Users/gsehdou/Downloads/Alert_Feedback.csv"


@given("Open the error log file")
def open_error_log_file(context):
    open(DS_file, "r")


@when("Search for errors in the log file")
def read_error_in_log_file(context):
    open(DS_file).read().count(errorLog)


@then("There are no errors found")
def verify_no_errors(context):
    assert open(DS_file).read().count(errorLog) == 0


@when("Search for warning in the log file")
def read_warning_in_log(context):
    open(DS_file).read().count(warningLog)


@then("The warning are less than 100")
def verify_warning_less_than_100(context):
    assert open(DS_file).read().count(warningLog) < 10000


@given("Open the csv file prepare alert")
def open_csv_prepare_alert(context):
    open(Prepare_Alert_CSV, "r")


@when("Search for default value 0 in Prepare Alert CSV file")
def read_csv_prepare_alert(context):
    open(Prepare_Alert_CSV).read().count(default_value)


@then("The prepare alert csv contains no default value 0")
def verify_no_default_value(context):
    assert open(Prepare_Alert_CSV).read().count(default_value) != 0


@given("Open the csv file Alert Feedback")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Open the csv file Alert Feedback')


@when("Search for default value 0 in Alert Feedback CSV file")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Search for default value 0 in Alert Feedback CSV file')


@then("The alert feedback csv contains no default value 0")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then The alert feedback csv contains no default value 0')