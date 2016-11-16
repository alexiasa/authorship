def disable_input(*args):
    raise Exception("You should not call raw_input!")

__builtins__.raw_input = disable_input

import find_author

def approx(v1, v2):
    '''return true if v1 and v2 (floating point numbers) are approximately equal'''
    return v1-0.0001 < v2 < v1+0.0001

if __name__=="__main__":
    
    #test average_word_length
    text = [
        "James Fennimore Cooper\n",
        "Peter, Paul, and Mary\n",
    ]
    assert approx(find_author.average_word_length(text),5.14285714286),\
        "average_word_length on the text:\n\n%s\n should return 5.14285714286"%repr(text)

    #test type_token_ratio
    text = [
        "James Fennimore Cooper\n",
        "Peter, Paul, and Mary\n",
        "James Gosling\n"
    ]   
    assert approx(find_author.type_token_ratio(text), 0.88888),\
        "type_token_ratio on the text:\n\n%s\n should return 0.888888"%repr(text)
    

    #test hapax_legomana_ratio(text):
    assert approx(find_author.hapax_legomana_ratio(text),0.777777777778),\
        "hapax_legomana_ratio on the text:\n\n%s\n should return 0.777777777778"%repr(text)

    hooray = "Hooray! Finally, we're done."
    thesplit = ['Hooray', ' Finally', " we're done."]

    #test split_on_separators(original, separators):
    assert find_author.split_on_separators(hooray, "!,")==thesplit,\
        "split_on_separators(%s,'!,') should return %s"%(repr(hooray),repr(thesplit))

    #test average_sentence_length(text):
    text = ["The time has come, the Walrus said\n",
            "To talk of many things: of shoes - and ships - and sealing wax,\n",
            "Of cabbages; and kings.\n"
            "And why the sea is boiling hot;\n"
            "and whether pigs have wings.\n"]

    assert approx(find_author.average_sentence_length(text),17.5),\
        "average_sentence_length on the text:\n\n%s\n should return 17.5"%repr(text)

    #test average_sentence_complexity
    assert approx(find_author.avg_sentence_complexity(text), 3.5), \
         "avg_sentence_complexity on the text:\n\n%s\n should return %f"%(repr(text),3.5)

    #test compare_signatures(sig1, sig2, weight):
    sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    weight = [0, 11, 33, 50, 0.4, 4]

    assert approx(find_author.compare_signatures(sig1, sig2, weight), 12), \
           "compare_signatures on signatures \n%s \n%s should return 12" \
           %(repr(sig1), repr(sig2))


    print "okay"
