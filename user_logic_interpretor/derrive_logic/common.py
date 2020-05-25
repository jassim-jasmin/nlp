preprocess_replace_list = [
    ("' '", "'<space_replace>'")#:todo: multiple empty spce may occur need to change the logic
]
operator_list = ["!=", "==", "<=", ">="]
user_operator_list = ["FormatDate", "DiffDates"]
main_data_document_df = "main_data_document_df"

def preprocess(statement):
    for each_data in preprocess_replace_list:
        statement = statement.replace(each_data[0], each_data[1])

    statement = statement.replace('\"\"', '\"')

    return statement

def revert_preprocess(statement):
    for each_data in preprocess_replace_list:
        statemnt = statement.replace(each_data[1], each_data[0])

    return statemnt

def FormatDate(test):
    """
    :todo need to add user operation
    :param test:
    :return:
    """
    pass

user_operator= {
    "FormatDate":FormatDate
}