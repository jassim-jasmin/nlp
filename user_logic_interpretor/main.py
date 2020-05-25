from derrive_logic import key_word_syntax, syntax_dic
from derrive_logic import convert_logic
from derrive_logic import replace_function, revert_replace_function, preprocess_replace_list

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
ElseIf ( SDIS.Y == ""Subject died"" ) Then  SDIS.S ;
ElseIf ( SDIS.S == ""Subject died"" ) Then  FormatDate ( "Demo.BIRTHDT" ) ;'''

    if statement:
        return statement

def process_statement(main_data_document):
    rule = []
    statement = get_statement()
    print(statement,'\n\n')
    statement = replace_function(preprocess_replace_list, statement)
    split_statement = statement.split()
    limit = len(split_statement)
    index = 0

    while index<limit:
        if split_statement[index].lower() in syntax_dic:
            index, rule_data = key_word_syntax(split_statement, index, main_data_document) # identifying keyword,
            # variable, data
            rule.append(rule_data)

        else:
            index += 1

    # print(main_data_document)
    logic_applyed_dataframe = convert_logic(rule, main_data_document)

    print(logic_applyed_dataframe)

process_statement(main_data_document)
