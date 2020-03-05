import back_NLP as bk

stopwords_a_retener = ['are','is','do','did','has','have','should','was','were']

NLP_kaggle = bk.data_maniputation()
NLP_kaggle.load_data()
NLP_kaggle.prepro_tweets()
NLP_kaggle.tokenizer()
NLP_kaggle.filtro_stopwords(lista_a_retener = stopwords_a_retener)