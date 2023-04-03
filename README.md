# Market-Basket-Data-Analytics

## INTRODUCTION:
Market Basket Analysis is a data mining technique used quite frequently by the shop-owners and retailers to understand the shopping behaviour and the purchasing pattern of their customers. This project contains data analysis and data visualization which is helpful in understanding the customers' purchase behavior and also analyzes the number of accidents in different city corresponding to the sales of liquor in that state.

In simpler terms, it helps entrepreneurs get the insights of the most frequently bought products and combination of these products.

### NOTE:
Market Basket Analysis does not rely on any assumption like linearity, or normality which are often violated during linear-based techniques.

## LOGIC BEHIND MAREKT BASKET ANALYSIS:
Primary aim of this analysis is to find the relation between the items being purchased by the customer. This technique primarily computes **If-Then** clause i.e,

> ***If[A] then[B] = 'the item on the left(A) is likely to be ordered more often with the item on the right(B)'***

***Example 1:***

If[Bread] then[Butter] => Customer's are more frequent in buying *Butter* when they buy *Bread*.

## MATHEMATICS & FORMULAE's USED:
1. **Antecedent:** Item on the *LEFT*; primary item being bought. *(Example 1. - Bread)*
2. **Consequent:** Item on the *RIGHT*; secondary item being bought following item on the left. *(Example 2. - Butter)*
<p align = 'center'>
  <img src = "./Formula's/Antecedant & Consequent.png" alt = 'Apoorv Pathak' width = '200' height = '200'>
</p>
3. **Support:** Probability of the occurrence of the antecedent. *(Example 1. -  Probability that the customer will buy the 'Bread')*
<p align = 'center'>
  <img src = "./Formula's/Support.png" alt = 'Apoorv Pathak' width = '200' height = '200'>
</p>
4. **Confidence:** Probability of the occurrence of the consequent given tht antecedent has occured. *(Example 1. -  Probability that the customer will buy the 'Butter' when 'Bread' was bought)*
<p align = 'center'>
  <img src = "./Formula's/Confidence.png" alt = 'Apoorv Pathak' width = '200' height = '200'>
</p>
5. **Lift:** Ratio of the support of the left-hand side(antecedent, *Bread*) and it's co-occurrence with the right-hand side(consequent, *Butter*), divided by the probability that the left-hand side(antecedent, *Bread*) and right-hand side(consequent, *Butter*) co-occur together when they are independent.
<p align = 'center'>
  <img src = "./Formula's/Lift.png" alt = 'Apoorv Pathak' width = '400' height = '200'>
</p>
6. **Zhang's Metric:** Zhang metric or F-measure can be used to evaluate the performance of association rule mining algorithms. This metric's value ranges from -1 to 1 to represent both positive and perfect associations. This metric helps in determining the specific items which must not be put together.
<p align = 'center'>
  <img src = "./Formula's/Zhang Metric.png" alt = 'Apoorv Pathak' width = '800' height = '200'>
</p>
7. **Centrality:** This is a crucial concept as it help in determining the most important node in the graph. Importance of any node depends on the defination of the *importance*.
<p align = 'center'>
  <img src = "./Formula's/Centrality.png" alt = 'Apoorv Pathak' width = '800' height = '200'>
</p>
8. **Silhouette Coefficient:** Silhouette Score is pretty helpful in calculating the goodness of the clustering techniques. Its value ranges from -1 to 1.
- 1 means clusters are well apart from each other and clearly distinguished.
- 0 means clusters are indifferent from each other and distance between them is not significant.
- -1 means clusters are assigned incorrectly.
<p align = 'center'>
  <img src = "./Formula's/Silhouette Score.png" alt = 'Apoorv Pathak' width = '800' height = '200'>
</p>

## REFERENCES:
[1] [Research Paper: How to Increase Sales in Retail with Market Basket Analysis](https://www.academia.edu/download/56086206/Article_1.pdf)

[2] [Market Basket Analysis in Management Research](https://journals.sagepub.com/doi/abs/10.1177/0149206312466147)

[3] [Centrality](https://towardsdatascience.com/graph-analytics-introduction-and-concepts-of-centrality-8f5543b55de3)

[4] [Silhouette Coefficient](https://towardsdatascience.com/silhouette-coefficient-validating-clustering-techniques-e976bb81d10c)
