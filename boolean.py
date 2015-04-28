__author__ = 'ags7kor'
import operator,re

# global all_combinations
all_combinations=[]

def do_not(string):
    matches=re.findall(r'!.',string)
    for match in matches:
        replace_with=str( int( not int( match[1])))
        string=string.replace(match,replace_with)
    return string

def do_or(string):
    matches=re.findall(r'.\|.(?:\|.)*',string)
    for match in matches:
        replace_with='0'
        vars=re.findall(r'[01]',match)
        if '1' in vars:
            replace_with='1'
        string=string.replace(match,replace_with)
    return string

def do_and(string):
    matches=re.findall(r'.\&.(?:\&.)*',string)
    for match in matches:
        replace_with='1'
        vars=re.findall(r'[01]',match)
        if '0' in vars:
            replace_with='0'
        string=string.replace(match,replace_with)
    return string

def solve(combination, input_str, rank):
    call_map={'!':do_not, '|':do_or, '&':do_and}

    try:
        substituted_str=""
        for i in input_str:
            if i in combination:
                substituted_str+=str(combination[i])
            else:
                substituted_str+=i
        print substituted_str
        for item in rank:
            do_func=call_map[item[0]]
            substituted_str=do_func(substituted_str)
            print "----",substituted_str
        print
        return substituted_str
    except:
        pass

def generate_combination(variables,comb_dict, length, current_index):
    if len(comb_dict)==length:
        # print comb_dict
        all_combinations.append(comb_dict.copy())
        # print all_combinations,"\n"
    else:
        for i in [1,0]:
            comb_dict[variables[current_index]]=i
            generate_combination(variables,comb_dict, length,current_index+1)
            comb_dict.pop(variables[current_index], None)


def main(input_str,variables,order):
    answers=[]
    rank=sorted(order.items(), key=operator.itemgetter(1))

    generate_combination(variables, {}, len(variables), 0)

    print "\nTotal no. of combinations : ",len(all_combinations),"\n"
    for combination in all_combinations:
        ans=solve(combination, input_str, rank)
        if ans=='1':
            answers.append(combination)

    print "\nAll the solutions : \n"
    for ans in answers:
        print ans

    # for answer in answers:
    #     print answer

def nothing():
    pass

if __name__ == '__main__':
    And,Or,Not,input_str='&','|','!','a&b|c&!d|g&!e|f&g' # If you don't want to give inputs repeatedly

    # print "Enter your symbols for :\n"
    # And=raw_input("And = ")
    # Or=raw_input("Or = ")
    # Not=raw_input("Not = ")
    # input_str=raw_input("Enter the expression :")

    input_str=input_str.replace(" ","")

    mapping={And:"&", Or:"|", Not:"!"}
    order={"&":3, "|":2, "!":1}


    variables=[]
    processed_str=""

    for i in input_str:
        if i in mapping:
            processed_str+=mapping[i]
        else:
            processed_str+=i
            variables.append(i)
    variables=list(set(variables))

    print "\n\nReconstituted string : ",processed_str
    print "Variables : ",variables,"\n"

    main(processed_str,variables,order)
