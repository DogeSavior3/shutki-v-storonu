import glob
import tqdm
from scipy.sparse.linalg import svds
import numpy as np

def make_corpus(input_path, output_file_path):
    file_list = sorted(glob.glob(input_path + '/*'))
    with open(output_file_path, 'w') as output_file:
        for file in tqdm.tqdm(file_list):
            with open(file, 'r') as input_file:
                output_file.write(input_file.read().replace('\n', ' '))
                output_file.write('\n')

from sklearn.feature_extraction.text import TfidfVectorizer
def make_matrix_W_list_of_words(corpus_path, min_df, max_df=None, token_pattern = None, use_idf = True):
    with open(corpus_path, 'r') as corpus_file:
        if token_pattern:
            vectorizer = TfidfVectorizer(analyzer='word', min_df=min_df, token_pattern=token_pattern, use_idf=use_idf)
        else:
            vectorizer = TfidfVectorizer(analyzer='word', min_df=min_df, use_idf=use_idf)
        data_vectorized = vectorizer.fit_transform(corpus_file)
    return data_vectorized, vectorizer.get_feature_names_out()

def apply_svd(W, k, output_folder):
    '''
    W - matrix texts x words
    k - the rank of the SVD, must be less than any dimension of W
    '''
    #Apply the SVD function
    u, sigma, vt = svds(W, k)

    #The function does not garantee, that the order of the singular values is descending
    #So, we need to dreate it by hand
    descending_order_of_inds = np.flip(np.argsort(sigma))
    u = u[:,descending_order_of_inds]
    vt = vt[descending_order_of_inds]
    sigma = sigma[descending_order_of_inds]

    #Checking that sizes are ok
    assert sigma.shape == (k,)
    assert vt.shape == (k, W.shape[1])
    assert u.shape == (W.shape[0], k)

    # #Now, we'll save all the matrixes in folder (just in case)
    # with open(output_folder+'/' + str(k) + '_sigma_vt.npy', 'wb') as f:
    #     np.save(f, np.dot(np.diag(sigma), vt).T)
    # with open(output_folder+'/' +  str(k) + '_sigma.npy', 'wb') as f:
    #     np.save(f, sigma)
    # with open(output_folder+'/' +  str(k) + '_u.npy', 'wb') as f:
    #     np.save(f, u)
    # with open(output_folder+'/' +  str(k) + '_vt.npy', 'wb') as f:
    #     np.save(f, vt)
    return np.dot(np.diag(sigma), vt).T

token_pattern = r"(?u)\b[אבגדהוזחטיכלמנסעפצקרשתךםןףץ]{2,}\b"
make_corpus('lemma_stanza_anc', 'corpus_lemma_stanza_anc.txt')
W, words_list  = make_matrix_W_list_of_words('corpus_lemma_stanza_anc.txt', 1, token_pattern = token_pattern)
print(W.shape)

vv = apply_svd(W, 32, 'svd_files')

def create_dictionary(words_list, vv, output_file):
    dictionary = {}
    for word, vector in zip(words_list, vv):
        dictionary[word] = vector
    with open(output_file, 'wb') as f:
        np.save(f, dictionary)
    return dictionary

dictionary = create_dictionary(words_list, vv, 'hebrew_dictionary_svd_32.npy')
