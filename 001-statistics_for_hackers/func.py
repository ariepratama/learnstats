import matplotlib.pyplot as plt

def draw_bar_plot_heads_counts(unique, counts):
    f,ax = plt.subplots(figsize=(12, 7))
    plt.bar(unique, counts)
    plt.xlabel('x')
    plt.ylabel('Frequency of heads')
    plt.title('Frequencies of Heads')
    plt.show()
    
def draw_step_plot_head_probabilities(unique, probabilities, what_we_get=None, probability_of_what_we_get=None):
    f,ax = plt.subplots(figsize=(12, 7))
    plt.step(unique, probabilities)
    if what_we_get is not None and probability_of_what_we_get is not None:
        plt.axvline(what_we_get, c='red')
        plt.text(
            what_we_get + 0.3, 0.12, 
            s='this is {}, with prob: {}%'.format(what_we_get, probability_of_what_we_get * 100), 
            color='red'
        )

    plt.ylabel('Probability')
    plt.title('Probabilities of Number of Heads Happening')
    plt.show()