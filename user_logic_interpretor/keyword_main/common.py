preprocess_replace_list = [
    ("' '", "'<space_replace>'")#:todo: multiple empty spce may occur need to change the logic
]
operator_list = ["!=", "==", "<=", ">="]
user_operator_list = ["FormatDate", "DiffDates"]

def preprocess(statemnt):
    for each_data in preprocess_replace_list:
        statemnt = statemnt.replace(each_data[0], each_data[1])

    return statemnt

def revert_preprocess(statement):
    for each_data in preprocess_replace_list:
        statemnt = statement.replace(each_data[1], each_data[0])

    return statemnt