def disable_input(*args):
    raise Exception("You should not call raw_input!")


__builtins__.raw_input = disable_input

import find_author


def approx(v1, v2):
    """return true if v1 and v2 (floating point numbers) are approximately equal"""
    return v1 - 0.0001 < v2 < v1 + 0.0001


if __name__ == "__main__":
    # test average_word_length
    text = [
        "James Fennimore Cooper\n",
        "Peter, Paul, and Mary\n",
    ]
    assert approx(find_author.average_word_length(text), 5.14285714286), \
        "average_word_length on the text:\n\n%s\n should return 5.14285714286" % repr(text)

    # test type_token_ratio
    text = [
        "James Fennimore Cooper\n",
        "Peter, Paul, and Mary\n",
        "James Gosling\n"
    ]
    assert approx(find_author.type_token_ratio(text), 0.88888), \
        "type_token_ratio on the text:\n\n%s\n should return 0.888888" % repr(text)

    # test hapax_legomana_ratio(text):
    expected = 0.777777777778
    actual = find_author.hapax_legomana_ratio(text)
    assert approx(actual, expected), \
        "hapax_legomana_ratio on the text:\n\n%s\n should return %s but got %s" % (repr(text), expected, actual)

    hooray = "Hooray! Finally, we're done."
    thesplit = ['Hooray', ' Finally', " we're done."]

    # test split_on_separators(original, separators):
    assert find_author.split_on_separators(hooray, "!,") == thesplit, \
        "split_on_separators(%s,'!,') should return %s but got %s" % (
            repr(hooray), repr(thesplit), find_author.split_on_separators(hooray, "!,"))

    # test average_sentence_length(text):
    text = ["The time has come, the Walrus said\n",
            "To talk of many things: of shoes - and ships - and sealing wax,\n",
            "Of cabbages; and kings.\n"
            "And why the sea is boiling hot;\n"
            "and whether pigs have wings.\n"]

    expected = 17.5
    actual = find_author.average_sentence_length(text)
    assert approx(actual, expected), \
        "average_sentence_length on the text:\n\n%s\n should return %s, but got %s" % (repr(text), expected, actual)

    # test average_sentence_complexity
    assert approx(find_author.avg_sentence_complexity(text), 3.5), \
        "avg_sentence_complexity on the text:\n\n%s\n should return %f" % (repr(text), 3.5)

    # test compare_signatures(sig1, sig2, weight):
    sig1 = ["a_string", 4.4, 0.1, 0.05, 10.0, 2.0]
    sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    weight = [0, 11, 33, 50, 0.4, 4]

    assert approx(find_author.compare_signatures(sig1, sig2, weight), 12), \
        "compare_signatures on signatures \n%s \n%s should return 12" \
        % (repr(sig1), repr(sig2))

    text = [
        "The time has come, the Walrus said\n To talk of many things: of shoes - and ships - and sealing wax,\n \
        Of cabbages; and kings.\n And why the sea is boiling hot;\n and whether pigs have wings.\n"]
    actual = len(find_author.get_sentences(text))
    expected = 2
    assert actual == expected, 'got ' + str(actual)

    text = "The time has come, the Walrus said\n To talk of many things: of shoes - and ships - and sealing wax,\n \
            Of cabbages; and kings.\n"
    expected = 23
    actual = len(find_author.get_words(text))
    assert actual == expected, 'got ' + '_'.join(find_author.get_words(text))

    text = [
        "The time has come, the Walrus said\n To talk of many things: of shoes - and ships - and sealing wax,\n \
         Of cabbages; and kings.\n And why the sea is boiling hot;\n and whether pigs have wings.\n"]
    expected = 35
    actual = len(find_author.get_words(text))
    assert actual == expected, 'got ' + '_'.join(find_author.get_words(text))

    # test average_sentence_length(text):
    text = ["Now, the time has come, the Walrus said\n",
            "To talk of a bunch of things: of shoes - and ships - and sealing wax,\n",
            "Of cabbages; and kings.\n"
            "And why the sea is boiling hot;\n"
            "and whether pigs have wings.\n"]

    expected = 19
    actual = find_author.average_sentence_length(text)
    assert approx(actual, expected), \
        "average_sentence_length on the text:\n\n%s\n should return %s, but got %s" % (repr(text), expected, actual)

    text = "here's some text that's KIND OF!!! WEIRD, stuff, etc...BLAH"

    expected = 3.33333
    actual = find_author.average_sentence_length(text)
    assert approx(actual, expected), \
        "average_sentence_length on the text:\n\n%s\n should return %s, but got %s" % (repr(text), expected, actual)

    # test average_word_length
    text = "more words and words. these are also words. here are some more."
    expected = 4.08333
    actual = find_author.average_word_length(text)
    assert approx(actual, expected), \
        "average_word_length on the text:\n\n%s\n should return %s but got %s" % (repr(text), expected, actual)

    # test type_token_ratio
    text = ["this is a single string string"]
    expected = 0.83333
    actual = find_author.type_token_ratio(text)
    assert approx(actual, expected), \
        "type_token_ratio on the text:\n\n%s\n should return %s but got %s" % (repr(text), expected, actual)

    # test hapax_legomana_ratio(text):
    expected = 0.66667
    actual = find_author.hapax_legomana_ratio(text)
    assert approx(actual, expected), \
        "hapax_legomana_ratio on the text:\n\n%s\n should return %s but got %s" % (repr(text), expected, actual)

    text = "pen pen apple pen pineapple pen pineapple apple"

    # test hapax_legomana_ratio(text):
    expected = 0
    actual = find_author.hapax_legomana_ratio(text)
    assert approx(actual, expected), \
        "hapax_legomana_ratio on the text:\n\n%s\n should return %s but got %s" % (repr(text), expected, actual)

    text = "word word word and some other words"

    # test hapax_legomana_ratio(text):
    expected = 4.0 / 7.0
    actual = find_author.hapax_legomana_ratio(text)
    assert approx(actual, expected), \
        "hapax_legomana_ratio on the text:\n\n%s\n should return %s but got %s" % (repr(text), expected, actual)

    text = ["The time, has come, the Walrus said\n",
            "To talk of; many things: of shoes - and ships - and sealing wax,\n",
            "Of cabbages; and kings.\n"
            "And why; the sea is boiling hot;\n"
            "and whether pigs have wings.\n"]

    # test average_sentence_complexity
    expected = 5
    actual = find_author.avg_sentence_complexity(text)
    assert approx(actual, expected), \
        "avg_sentence_complexity on the text:\n\n%s\n should return %f but got %f" % (repr(text), expected, actual)

    # test compare_signatures(sig1, sig2, weight):
    sig1 = ["a_string", 4.4, 0.1, 0.05, 10.0, 2.0]
    sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 8.0]
    weight = [0, 11, 33, 50, 0.4, 4]
    expected = 28
    actual = find_author.compare_signatures(sig1, sig2, weight)
    assert approx(actual, expected), \
        "compare_signatures on signatures \n%s \n%s should return %s but got %s" \
        % (repr(sig1), repr(sig2), expected, actual)

    print("okay")  # for python3 compatibility
