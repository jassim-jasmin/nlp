from user_logic_interpretor.derrive_logic.common import *

def get_variable_operator_data(condition_array, main_data_document=None):
    condition = ''
    for each_statement in condition_array:
        each_statement = revert_preprocess(each_statement)

        if each_statement in operator_list:
            # :todo: need to add validation and exception action for both :var condition: and :var each_statement:
            condition += f" {each_statement} "

        elif each_statement in user_operator_list:
            # :todo: need to add action for this perticular option
            condition += f"{user_operator}['{each_statement}']"

        else: # it might be a variable from data provided
            data = ''

            if main_data_document:
                if each_statement in main_data_document:
                    data = f"{main_data_document_df}['{each_statement}']"# its a variable in the data provided

            if data:
                condition += f" {data}"

            else:
                condition += f" {each_statement} "

    return condition

def convert_logic_test(rule, main_data_document):
    """
    It's the final process of converting the statement logic to stnd logic
    :todo: edit needed, written for readability
    :param rule:
    :return:
    """
    for each_rule in rule:
        for key_word, content in each_rule.items():
            final_statement = ''
            """ The formatting procedure """
            if key_word == 'if':
                final_statement += 'if ('
                if "condition" in content:
                    final_statement += get_variable_operator_data(content["condition"], main_data_document)

                if "action" in content:
                    final_statement += ') Then:' + get_variable_operator_data(content["action"], main_data_document)
            elif key_word == 'elseif':
                final_statement += 'elif ('
                if "condition" in content:
                    final_statement += get_variable_operator_data(content["condition"], main_data_document)

                if "action" in content:
                    final_statement += ') Then:' + get_variable_operator_data(content["action"], main_data_document)

            if final_statement:
                print(final_statement)

import pandas as pd

def convert_logic(rule, main_data_document):
    """
    :todo :var main:_data_document is not dataframe
    :todo: need remove if_else_mark column from final output, instead of :var newcol: update with statement output field name
    :param rule:
    :param main_data_document:
    :return:
    """
    main_data_document_df = pd.DataFrame(main_data_document)
    main_data_document_df = main_data_document_df.reindex(main_data_document_df.columns.tolist() + ['if_else_mark'], axis=1) # adding new column
    main_data_document_df = main_data_document_df.reindex(main_data_document_df.columns.tolist() + ['newcol'],
                                                          axis=1)
    print(main_data_document_df)
    if_ladder_depth = 0

    for each_rule in rule:
        for key_word, content in each_rule.items():
            if key_word == 'if' or key_word == "elseif":
                if key_word == 'if':
                    if_ladder_depth += 1 # :todo: need to check wehter any exception is comming when nested if is comming

                if "condition" in content:
                    condition = get_variable_operator_data(content["condition"], main_data_document)

                if "action" in content:
                    action = get_variable_operator_data(content["action"], main_data_document)

                if condition and action:
                    main_data_document_df.loc[eval(condition), 'if_else_mark'] = if_ladder_depth

                    main_data_document_df.loc[eval(condition), 'newcol'] = eval(action)


    return main_data_document_df