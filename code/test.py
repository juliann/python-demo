import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Test:
    # listings_df = "daza"
    listings_df = pd.read_csv("AB_NYC_2019.csv")
    # print(listings_df)

    columns_to_drop = ['id', 'host_name', 'last_review']
    listings_df.drop(columns_to_drop, axis="columns", inplace=True)
    listings_df.fillna({'reviews_per_month': 0}, inplace=True)
    print(listings_df.nlargest(10, 'number_of_reviews'))
    print(listings_df['neighbourhood_group'].unique())

    countplot = sns.countplot(data=listings_df, x='neighbourhood_group')
    plt.show()
