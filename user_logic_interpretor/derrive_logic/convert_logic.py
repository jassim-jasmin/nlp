from derrive_logic.common import *
import pandas as pd

def get_variable_operator_data(condition_array, main_data_document=None):
    """
    :todo: istead of appending to a single string need to place in seperate variable, it will be helpfull for processing output connector
    :param condition_array:
    :param main_data_document:
    :return:
    """
    condition = ''

    for each_statement in condition_array:
        each_statement = revert_replace_function(preprocess_replace_list, each_statement)

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
                condition += f"{data}"

            else:
                condition += f" {each_statement} "

    return condition


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
    for each_column in main_data_document_df.columns:
        main_data_document_df = replace_function(data_frame_replace_list, main_data_document_df, each_column)

    print(main_data_document_df)
    if_ladder_depth = 0

    for each_rule in rule:
        for key_word, content in each_rule.items():
            if key_word == 'if' or key_word == "elseif":
                content = replace_function(data_frame_replace_list, content, "condition")
                if_ladder_depth += 1 # :todo: comment it, onl for testing

                # if key_word == 'if':
                #     if_ladder_depth += 1 # :todo: need to check wehter any exception is comming when nested if is comming

                if "condition" in content:
                    condition = get_variable_operator_data(content["condition"], main_data_document)

                if "action" in content:
                    action = get_variable_operator_data(content["action"], main_data_document)

                if condition and action:
                    import re

                    constant_assign = re.search(r'"([0-9a-zA-Z ]+)"',condition, re.IGNORECASE) # concated element may need preprocessing

                    if constant_assign:
                        match_string = constant_assign.group(1)
                        processing = replace_function(data_frame_replace_list, match_string)
                        # print("PProcessingn", processing)
                        condition = condition.replace(match_string, processing)


                    main_data_document_df.loc[eval(condition), 'if_else_mark'] = if_ladder_depth
                    main_data_document_df.loc[eval(condition), 'newcol'] = eval(action)

    main_data_document_df = revert_replace_function(data_frame_replace_list,main_data_document_df, each_column)

    return main_data_document_df