import pandas as pd

def process_data():
    # Load the biopics data
    biopics = pd.read_csv("biopics.csv")

    # Filter out duplicated rows
    biopics = biopics.drop_duplicates()

    # Rename the variable box_office to earnings
    biopics.rename(columns={"box_office": "earnings"}, inplace=True)

    # Filter out rows with missing earnings
    biopics = biopics.dropna(subset=["earnings"])

    # Keep only movies released in the year 1990 or later
    biopics = biopics[biopics["year_release"] >= 1990]

    # Convert the type of type_of_subject and country to Categorical
    biopics["type_of_subject"] = biopics["type_of_subject"].astype("category")
    biopics["country"] = biopics["country"].astype("category")

    # Create a new variable called lead_actor_actress_known
    biopics["lead_actor_actress_known"] = ~biopics["lead_actor_actress"].isna()

    # Update earnings to be in million dollars
    biopics["earnings"] /= 10**6  # Convert earnings to million dollars

    # Reorder the columns
    biopics = biopics[["title", "year_release", "earnings", "country", "type_of_subject", "lead_actor_actress", "lead_actor_actress_known"]]

    # Sort the rows in descending order by earnings
    biopics = biopics.sort_values(by="earnings", ascending=False)

    return biopics

# Example usage:
processed_data = process_data()
print(processed_data.head())