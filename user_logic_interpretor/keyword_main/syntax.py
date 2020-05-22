CONDITON = "condition"
BEGIN = "begin"
END = "end"
ACTION = "action" # what the statement to be done, eg:- return a
LADDER = "ladder"
key_word = []


"""
condition is given as array, since other syntax may come
"""

syntax_dic = {
    "if": [
        {
            CONDITON: [{BEGIN: ["("], END: [")"]}]# general rule for condition
        }
    ],
    "elseif": [
        {
            CONDITON: [{BEGIN: ["("], END: [")"]}]
        }
    ]
}

action_rule = {
    "if": {BEGIN: ["Then"], END: [";"], ACTION: "unknown"},
    "elseif": {BEGIN: ["Then"], END: [";"], ACTION: "unknown"}
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

def key_word_syntax(split_statement, keyword_index):
    syntax_doc = {}
    # print(split_statement[keyword_index])
    key = split_statement[keyword_index].lower()

    if key in syntax_dic:
        syntax_rule_array = syntax_dic[key]
        syntax_doc[key] = {}

    else:
        print("error in key_word_syntax mapping")
        exit(1)

    keyword_index += 1

    for each_syntax_rul in syntax_rule_array:
        if CONDITON in each_syntax_rul: # logic need to add for each sub rule
            conditions = each_syntax_rul[CONDITON]
            for each_condition_rule in conditions:
                # checking the split statement
                if BEGIN in each_condition_rule:
                    #:todo: suppose ( is comming multiple times means, the end key ) will need to check once again.
                    result, keyword_index = get_begin_end_statement(split_statement, keyword_index, each_condition_rule)
                    syntax_doc[key][CONDITON] = result
                    # Begin followed by condition, then action is next

                    if key in action_rule:
                        action, keyword_index = get_begin_end_statement(split_statement, keyword_index, action_rule[key])
                        syntax_doc[key][ACTION] = action


    return keyword_index, syntax_doc
