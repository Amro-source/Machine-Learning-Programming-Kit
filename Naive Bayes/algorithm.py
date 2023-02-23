#Introduction to Naive Bayes Naive Bayes is among one of the very simple and powerful
#algorithms for classification based on Bayes Theorem with an assumption of independence among
#the predictors.The Naive Bayes classifier assumes that the presence of a feature in a class is
#not related to any other feature.Naive Bayes is a classification algorithm for binary and
#multi- class classification problems.

#Bayes Theorem

#Based on prior knowledge of conditions that may be related to an event, Bayes theorem
#describes the probability of the event conditional probability can be found this way
#Assume we  have a Hypothesis(H) and evidence(E),According to Bayes theorem, the relationship
#between the probability of Hypothesis before getting the evidence represented as P(H) and the
#probability of the hypothesis after getting the evidence represented as P(H | E) is:

#P(H | E) = P(E | H) * P(H) / P(E)
#Prior probability = P(H) is the probability before getting the evidence Posterior
#probability = P(H | E) is the probability after getting evidence In general,

#P(class |data) = (P(data |class ) * P( class )) / P(data)

#Bayes Theorem Example
#Assume we have to find the probability of the randomly picked card to be king given that it is a face card.
#There are 4 Kings in a Deck of Cards which implies that P(King) = 4/52
#as all the Kings are face Cards so P(Face|King) = 1
#there are 3 Face Cards in a Suit of 13 cards and there are 4 Suits in total so P(Face) = 12/52
#Therefore,

