from keyword_main import key_word_syntax, syntax_dic

main_data_document = {"AESA.DTHDAT": "something"}

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

def get_statement(statement=None):
    statement = """If ( AESA.DTHDAT != ' ' ) Then  AESA.DTHDAT ;
ElseIf ( SDIS.DSTERMSC_DLV == """"Subject died"""" ) Then SDIS.DSSTDATSC ;
ElseIf ( SDIS.DSTERMTR_DLV == """"Subject died"""" ) Then  SDIS.DSSTDATTR ;
ElseIf ( SDIS.DSTERMFU_DLV == """"Subject died"""" ) Then  SDIS.DSSTDATFU ;"""

    if statement:
        return statement

def get_variable_operator_data(condition_array):
    condition = ''
    for each_statement in condition_array:
        each_statement = revert_preprocess(each_statement)

        if each_statement in operator_list:
            # :todo: need to add validation and exception action for both :var condition: and :var each_statement:
            condition += f" {each_statement} "

        elif each_statement in user_operator_list:
            # :todo: need to add action for this perticular option
            pass

        else: # it might be a variable from data provided
            if each_statement in main_data_document:
                condition += f" main_data_document[{each_statement}] "# its a variable in the data provided

            else:
                condition += f" {each_statement} "

def process_statement():
    rule = []
    statement = get_statement()
    statement = preprocess(statement)
    split_statement = statement.split()
    limit = len(split_statement)
    index = 0

    while index<limit:
        if split_statement[index].lower() in syntax_dic:
            index, rule_data = key_word_syntax(split_statement, index)
            rule.append(rule_data)

        else:
            index += 1

    for each_rule in rule:
        for key_word, content in each_rule.items():
            if key_word == 'if':
                if "condition" in content:
                    get_variable_operator_data(content["condition"])

                if "action" in content:
                    get_variable_operator_data(content["action"])

process_statement()
