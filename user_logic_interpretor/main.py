from derrive_logic import key_word_syntax, syntax_dic
from derrive_logic import convert_logic
from derrive_logic import preprocess

main_data_document = {
    "AESA.DTHDAT": "something",
    "SDIS.DSTERMSC_DLV": "something",
    "SDIS.DSSTDATFU": "somethin",
    "SDIS.DSSTDATTR": "something",
    "SDIS.DSTERMTR_DLV": "something",
    "SDIS.DSSTDATSC": "something",
    "SDIS.DSTERMFU_DLV": "something"

}

def get_statement(statement=None):
    """Subject died having issue"""
    statement = '''If ( AESA.DTHDAT != ' ' ) Then  AESA.DTHDAT ;
ElseIf ( SDIS.DSTERMSC_DLV == ""Subject died"" ) Then SDIS.DSSTDATSC ;
ElseIf ( SDIS.DSTERMTR_DLV == ""Subject died"" ) Then  SDIS.DSSTDATTR ;
ElseIf ( SDIS.DSTERMFU_DLV == ""Subject died"" ) Then  SDIS.DSSTDATFU ;'''

    if statement:
        return statement

def process_statement():
    rule = []
    statement = get_statement()
    # print(statement)
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

    # print(rule)
    convert_logic(rule, main_data_document)

process_statement()
