from derrive_logic.common import user_operator, main_data_document_df, CONDITON, BEGIN, END, ACTION


key_word = []

"""
condition is given as array, since other syntax may come
"""

syntax_dic = {
    "if":
        {
            CONDITON: [{BEGIN: ["("], END: [")"]}],# general rule for condition
            ACTION: {BEGIN: ["Then"], END: [";"], ACTION: "unknown"}
        }
    ,
    "elseif":
        {
            CONDITON: [{BEGIN: ["("], END: [")"]}],
            ACTION: {BEGIN: ["Then"], END: [";"], ACTION: "unknown"}
        }
}


def get_next_split_statement(statement, index):
    if index < len(statement):
        next = statement[index]

        return next, index+1

    else:
        return False

def get_begin_end_statement(split_statement, keyword_index,each_condition_rule):
    result = []

    if BEGIN in each_condition_rule:  # if begin encounter upto end should itrate
        begin_match_array = each_condition_rule[BEGIN]  # if nothing match syntax error exit()
        next_itrate = get_next_split_statement(split_statement, keyword_index)

        if next_itrate:
            next_word_in_statement, keyword_index = next_itrate

        else:
            print("statement end of without having a condition")

        if next_word_in_statement in begin_match_array:
            next_itrate = get_next_split_statement(split_statement, keyword_index)

            if next_itrate:
                next_word_in_statement, keyword_index = next_itrate

            else:
                print("incomplete statement, begin not complete")
                return False

            end_match_array = each_condition_rule[END]

            while next_word_in_statement not in end_match_array:
                result.append(next_word_in_statement)
                next_itrate = get_next_split_statement(split_statement, keyword_index)

                if next_itrate:
                    next_word_in_statement, keyword_index = next_itrate

                else:
                    print("condition not completed, end of string")
                    return False

            return result, keyword_index

        else:
            print("if each condition rule has a begin rule defined, it should satisfy")
            exit(1)  #:todo: change this to move next statement

def key_word_syntax(split_statement, keyword_index, data):
    syntax_doc = {}
    # print(split_statement[keyword_index])
    key = split_statement[keyword_index].lower()

    if key in syntax_dic:
        each_syntax_rul = syntax_dic[key]
        syntax_doc[key] = {}

    else:
        print("error in key_word_syntax mapping")
        exit(1)

    keyword_index += 1

    if CONDITON in each_syntax_rul: # logic need to add for each sub rule
        conditions = each_syntax_rul[CONDITON]

        if ACTION in each_syntax_rul:
            action_rule = each_syntax_rul[ACTION]

        else:
            action_rule = None

        for each_condition_rule in conditions:
            # checking the split statement
            if BEGIN in each_condition_rule:
                #:todo: suppose ( is comming multiple times means, the end key ) will need to check once again.
                result, keyword_index = get_begin_end_statement(split_statement, keyword_index, each_condition_rule)
                syntax_doc[key][CONDITON] = result
                # Begin followed by condition, then action is next

                if action_rule: # Changed to single rule
                    action, keyword_index = get_begin_end_statement(split_statement, keyword_index, action_rule)
                    general_array = []

                    for each_action in action:
                        if each_action in data:
                            # syntax_doc[key][ACTION] = [f"{main_data_document_df}['{each_action}']"]
                            general_array.append(f"{main_data_document_df}['{each_action}']")

                        elif each_action in user_operator:
                            # syntax_doc[key][ACTION] = [f"pre_function['{each_action}']"]
                            general_array.append(f"pre_function['{each_action}']")

                        else:
                            # syntax_doc[key][ACTION] = [f"'{each_action}'"]
                            general_array.append(f"'{each_action}'")


                    if general_array:
                        syntax_doc[key][ACTION] = general_array

                else:
                    print("exception in action rule, not found:", each_syntax_rul)

            else:
                print("no begin found")

    else:
        print(f"no {CONDITON} found in {each_syntax_rul}")

    # print(syntax_doc)

    return keyword_index, syntax_doc
