from derrive_logic import key_word_syntax, syntax_dic
from derrive_logic import convert_logic
from derrive_logic import preprocess

"""sample input date"""
main_data_document = {
    "AESA.DTHDAT": ["something", '', 'other'],
    "SDIS.DSTERMSC_DLV": ["something", 'x', 'Subject died'],
    "SDIS.DSSTDATFU": ["somethin", '', 'other'],
    "SDIS.DSSTDATTR": ["something", '', 'other'],
    "SDIS.DSTERMTR_DLV": ["something", '', 'other'],
    "SDIS.DSSTDATSC": ["something", '', 'other'],
    "SDIS.DSTERMFU_DLV": ["something", 'this value will upate', 'other']

}

def get_statement(statement=None):
    statement = '''If ( AESA.DTHDAT != ' ' ) Then  AESA.DTHDAT ;
ElseIf ( SDIS.DSTERMSC_DLV == ""Subject died"" ) Then SDIS.DSSTDATSC ;
ElseIf ( SDIS.DSTERMSC_DLV == ""x"" ) Then  SDIS.DSTERMFU_DLV ;
ElseIf ( SDIS.DSTERMFU_DLV == ""Subject_died"" ) Then  FormatDate ( "Demo.BIRTHDT" ) ;'''

    if statement:
        return statement

def process_statement(main_data_document):
    rule = []
    statement = get_statement()
    print(statement,'\n\n')
    statement = preprocess(statement)
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
