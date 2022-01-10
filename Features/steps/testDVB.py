def test_check_error_in_log():
    file = open("/Users/gsehdou/Downloads/DSLog.txt", "r")
    data = file.read().count("| E |")
    assert data == 0


def test_check_fatal_in_log():
    file = open("/Users/gsehdou/Downloads/DSLog.txt", "r")
    data = file.read().count("| F |")
    assert data == 0


def test_check_warning_in_log():
    file = open("/Users/gsehdou/Downloads/DSLog.txt", "r")
    data = file.read().count("| W |")
    assert data > 100



def test_check_no_default_0_in_Prepare_Alert():
    file = open("/Users/gsehdou/Downloads/Prepare_Alert.csv", "r")
    data = file.read().count("(0)")
    assert data == 0



def test_check_no_default_0_in_Alert_Feedback():
    file = open("/Users/gsehdou/Downloads/Alert_Feedback.csv", "r")
    data = file.read().count("(0)")
    assert data == 0
