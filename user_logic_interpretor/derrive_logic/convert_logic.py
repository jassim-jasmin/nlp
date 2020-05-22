from user_logic_interpretor.derrive_logic.common import revert_preprocess, operator_list, user_operator_list

def get_variable_operator_data(condition_array, main_data_document=None):
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
            data = ''

            if main_data_document:
                if each_statement in main_data_document:
                    data = f" main_data_document[{each_statement}] "# its a variable in the data provided

            if data:
                condition += f" {data}"

            else:
                condition += f" {each_statement} "

    return condition

def convert_logic(rule, main_data_document):
    """
    It's the final process of converting the statement logic to stnd logic
    :todo: edit needed
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