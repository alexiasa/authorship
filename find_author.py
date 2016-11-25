import os.path, math
import re

DBG = False  # for debugging purposes


def clean_up(s):
    """ Return a version of string s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. """
    
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result


def average_word_length(text):
    """ Return the average length of all words in text. Do not
    include surrounding punctuation in words. 
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word. """
    
    words = get_words(text)
    num_words = len(words)

    num_letters = 0
    for each_word in words:
        num_letters += len(each_word)

    avg_word_length = float(num_letters) / float(num_words)  # float for python2 compatibility
    if DBG: print('average word length:', avg_word_length)  # debug statement
    return avg_word_length
    

def type_token_ratio(text):
    """ Return the type token ratio (TTR) for this text.
    TTR is the number of different words divided by the total number of words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word. """
    words = get_words(text)
    total_words = len(words)
    unique_words = 0
    used_words = []

    for each_word in words:
        if (each_word not in used_words):
            used_words.append(each_word)
            unique_words += 1

    ttr = float(unique_words) / float(total_words)  # float for python2 compatibility
    if DBG: print('type token ratio:', ttr)
    return ttr
    
                
def hapax_legomana_ratio(text):
    """ Return the hapax_legomana ratio for this text.
    This ratio is the number of words that occur exactly once divided
    by the total number of words.
    text is a list of strings each ending in \n.
    At least one line in text contains a word."""
    words = get_words(text)
    total_words = len(words)
    unique_words = []
    used_words = []

    for each_word in words:
        if (each_word not in used_words):
            used_words.append(each_word)
            unique_words.append(each_word)
        elif (each_word in unique_words):
            unique_words.remove(each_word)

    hapax_legomena = float(len(unique_words)) / float(total_words)  # float for python2 compatibility
    if DBG: print('hapax legomena ratio:', hapax_legomena)
    return hapax_legomena


def split_on_separators(original, separators):
    """Return a list of non-empty, non-blank strings from the original string
        determined by splitting the string on any of the separators.
        separators is a string of single-character separators."""
    pattern = "[" + separators + "]"
    return re.split(pattern, original)


def get_sentences(my_text):
    """Return a list of sentences from the original string or list
    by joining them, applying clean up function, and
     splitting on terminating characters."""

    my_text = ''.join(my_text)  # joins array into a string and does nothing if input is already a string

    new_text = clean_up(''.join(my_text))
    sentences = re.split("""[?!.]+""", new_text)
    return sentences


def get_words(sentence):
    """Return a list of words contained in the original string
    by splitting it on word characters using regex and list filtering
    to omit spaces."""

    sentence = ''.join(sentence)  # joins array into a string, does nothing if input is a string

    words = re.split("[^\w']+", sentence)  # split on anything that's not a word character or apostrophe
    word_list = list(filter(None, words))
    return word_list


def average_sentence_length(text):
    """ Return the average number of words per sentence in text.
    text is guaranteed to have at least one sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. """

    words = get_words(text)  # call get_words function to get list of words in the text
    sentences = get_sentences(text)  # call get_sentences function to get list of sentences in the text
    num_words = len(words)
    num_sentences = len(sentences)
    avg_length = float(num_words) / float(num_sentences)  # float for python2 compatibility
    if DBG: print('average sentence length:', avg_length)
    return avg_length
    

def avg_sentence_complexity(text):
    """Return the average number of phrases per sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file.
    Phrases are substrings of a sentences separated by
    one or more of the following delimiters ,;: """
    sentences = get_sentences(text)  # call get_sentences function to get list of sentences in the text
    num_sentences = len(sentences)
    total_phrases = 0

    for each_sentence in sentences:
        phrases = re.split("""[,;:]""", each_sentence)
        total_phrases += len(phrases)

    average_sentence_complexity = float(total_phrases) / float(num_sentences)  # float for python2 compatibility

    if DBG: print('average sentence complexity:', average_sentence_complexity)
    return average_sentence_complexity
    
    
def get_valid_filename(prompt):
    """Use prompt (a string) to ask the user to type the name of a file. If
    the file does not exist, keep asking until they give a valid filename.
    The filename must include the path to the file.
    Return the name of that file."""

    while True:
        filename = input(prompt)

        if (os.path.isfile(filename)):
            return filename

        print('That file does not exist: ' + filename)

    
def read_directory_name(prompt):
    """Use prompt (a string) to ask the user to type the name of a directory. If
    the directory does not exist, keep asking until they give a valid directory.
    """

    while True:
        directory_name = input(prompt)

        if os.path.isdir(directory_name):
            return directory_name

        print('That directory does not exist: ' + directory_name)

    
def compare_signatures(sig1, sig2, weight):
    """Return a non-negative real number indicating the similarity of two 
    linguistic signatures. The smaller the number the more similar the 
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0  : author name (a string)
    1  : average word length (float)
    2  : TTR (float)
    3  : Hapax Legomana Ratio (float)
    4  : average sentence length (float)
    5  : average sentence complexity (float)
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    """
    # if DBG: print(sig1)
    # if DBG: print(sig2)
    # if DBG: print(weight)

    comparison = [
        abs(sig1[1] - sig2[1]) * weight[1],
        abs(sig1[2] - sig2[2]) * weight[2],
        abs(sig1[3] - sig2[3]) * weight[3],
        abs(sig1[4] - sig2[4]) * weight[4],
        abs(sig1[5] - sig2[5]) * weight[5]
    ]

    comparison_total = sum(comparison)
    # if DBG: print('comparison:', comparison_total)
    return comparison_total
    

def read_signature(filename):
    """Read a linguistic signature from filename and return it as 
    list of features. """
    
    file = open(filename, 'r')
    # the first feature is a string so it doesn't need casting to float
    result = [file.readline()]
    # all remaining features are real numbers
    for line in file:
        result.append(float(line.strip()))
    if DBG: print(result)
    return result
        

if __name__ == '__main__':
    
    prompt = 'enter the name of the file with unknown author:'
    mystery_filename = get_valid_filename(prompt)

    # readlines gives us a list of strings one for each line of the file
    text = open(mystery_filename, 'r').readlines()
    
    # calculate the signature for the mystery file
    mystery_signature = [mystery_filename]
    mystery_signature.append(average_word_length(text))
    mystery_signature.append(type_token_ratio(text))
    mystery_signature.append(hapax_legomana_ratio(text))
    mystery_signature.append(average_sentence_length(text))
    mystery_signature.append(avg_sentence_complexity(text))

    if DBG: print(mystery_signature)

    weights = [0, 11, 33, 50, 0.4, 4]
    
    prompt = 'enter the path to the directory of signature files: '
    dir = read_directory_name(prompt)
    # every file in this directory must be a linguistic signature
    files = os.listdir(dir)

    # we will assume that there is at least one signature in that directory
    this_file = files[0]
    signature = read_signature('%s/%s'%(dir,this_file))
    best_score = compare_signatures(mystery_signature, signature, weights)
    best_author = signature[0]
    for this_file in files[1:]:
        signature = read_signature('%s/%s'%(dir, this_file))
        score = compare_signatures(mystery_signature, signature, weights)
        if score < best_score:
            best_score = score
            best_author = signature[0]
    print ("best author match: %s with score %s"%(best_author, best_score))
