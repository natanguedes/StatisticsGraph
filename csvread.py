

import pandas as pd

# making data frame from csv file
data = pd.read_csv("ANO-2012.csv")

# making new data frame with dropped NA values

print(data.head())









    df <- data.frame(col1 = c(NA, 2, 3, 4),
             col2 = c(1, NA, 3, 4),
             col3 = c(1, 2, NA, 4),
             col4 = c(1, 2, 3, NA),
             col5 = c(1, 2, 3, 4))

# test whether an NA is present in each row

apply(df, 1, function(x) {sum(is.na(x)) > 0})
[1] TRUE TRUE TRUE TRUE