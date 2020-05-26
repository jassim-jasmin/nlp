preprocess_replace_list = [
    ("' '", "'<space_replace>'")#:todo: multiple empty spce may occur need to change the logic
    # ,('== ""', "== ''"),
    # ('!= ""', "== ''"),
    # ('<= ""', "<= ''"),
    # ('>= ""', ">= ''"),
    # ('==""', "== ''"),
    # ('!=""', "!= ''"),
    # ('<=""', "<= ''"),
    # ('>=""', ">= ''") # This cannot be fixed like this, should consider ending with
]
operator_list = ["!=", "==", "<=", ">="]
user_operator_list = ["FormatDate", "DiffDates"]
main_data_document_df = "main_data_document_df"

"""(logic string, to replace, data frame string)"""
data_frame_replace_list = [
("  ", "<space_replace>","  ", "<space_replace>"),
    (" ", "<space_replace>"," ", "<space_replace>"),
    ('""', '"', '""', '"'),# :todo: will be an issue if assigning an empty string
    ("''",  "'<empty_string>'", '', "<empty_string>")# Exception for dataframe,change to empty string
]

def replace_function(replace_list, statement, column_name=None):
    """
    :todo: if statement is dataframe, :var replace: should be of :var data_frame_replace_list:
    :param replace_list:
    :param statement:
    :param column_name:
    :return:
    """
    # print(str(type(statement)))


    for each_data in replace_list:
        if str(type(statement)) == "<class 'list'>":
            statement = [w.replace(each_data[0], each_data[1]) for w in statement]

        elif str(type(statement)) == "<class 'pandas.core.frame.DataFrame'>":
            statement = statement.replace(each_data[2], each_data[3], regex=True)

        elif str(type(statement)) == "<class 'dict'>":
            for each_data in replace_list:
                statement[column_name] = [w.replace(each_data[0], each_data[1]) for w in statement[column_name]]

        else:
            for each_data in replace_list:
                statement = statement.replace(each_data[0], each_data[1])


    return statement

def revert_replace_function(replace_list, statement, column_name=None):
    for each_data in replace_list:
        if str(type(statement)) == "<class 'list'>":
            statement = [w.replace(each_data[1], each_data[0]) for w in statement]

        elif str(type(statement)) == "<class 'pandas.core.frame.DataFrame'>":
            statement = statement.replace(each_data[3], each_data[2], regex=True)

        elif str(type(statement)) == "<class 'dict'>":
            for each_data in replace_list:
                statement[column_name] = [w.replace(each_data[1], each_data[0]) for w in statement[column_name]]

        else:
            for each_data in replace_list:
                statement = statement.replace(each_data[1], each_data[0])

    return statement

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