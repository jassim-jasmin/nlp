from derrive_logic import key_word_syntax, syntax_dic
from derrive_logic import convert_logic
from derrive_logic import replace_function, revert_replace_function, preprocess_replace_list, CONDITON, ACTION

"""sample input date"""
main_data_document = {
    "AESA.X": ["something", '', 'other'],
    "SDIS.Y": ["somethin", 'x', 'Subject died'],
    "SDIS.Z": ["somethin", '', 'other'],
    "SDIS.P": ["something", '', 'other'],
    "SDIS.Q": ["something", '', 'other'],
    "SDIS.R": ["something", '', 'other'],
    "SDIS.S": ["something", '', 'this value will upate']

}

def get_statement(statement=None):
    """
    :todo: need to fix ("") assigining empty string as "" will be an issue.
    :param statement:
    :return:
    """
    statement = '''If ( AESA.X != '' ) Then  AESA.X ;
    ElseIf ( AESA.X == '' ) Then SDIS.Y ;
    ElseIf ( SDIS.Y == ""Subject died"" ) Then  this_is_a_constant ;
    ElseIf ( SDIS.S == ""Subject died"" ) Then  FormatDate ( "Demo.BIRTHDT" ) ;'''

    if statement:
        return statement


def get_all_rules(statement):
    split_statement = statement.split()
    rule = []
    limit = len(split_statement)
    index = 0

    while index < limit:
        if split_statement[index].lower() in syntax_dic:
            index, rule_data = key_word_syntax(split_statement, index, main_data_document)  # identifying keyword,
            # variable, data
            rule.append(rule_data)

        else:
            index += 1

    return rule

def print_rule(rules):
    rule_sta = ''

    for each_rule in rules:
        for each_keyword, keyword_data in each_rule.items():
            condition = ''
            action = ''

            for each_condition in keyword_data[CONDITON]:
                condition += f" {each_condition}"

            for each_action in keyword_data[ACTION]:
                action += f" {each_action}"

            rule_sta += f"\n{each_keyword} \n{CONDITON} : {condition} \n{ACTION} {action}\n"

    print(rule_sta)

def process_statement(main_data_document):
    statement = get_statement()
    print(statement, '\n\n')
    statement = replace_function(preprocess_replace_list, statement)

    rule  = get_all_rules(statement)
    print_rule(rule)

    # print(main_data_document)
    # logic_applyed_dataframe = convert_logic(rule, main_data_document)
    #
    # print(logic_applyed_dataframe)


if __name__ == '__main__':
    process_statement(main_data_document)
