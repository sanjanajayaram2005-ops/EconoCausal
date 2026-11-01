import pandas as pd


DATA_PATH = "data/causal_retail_data.csv"


def load_data():
    return pd.read_csv(DATA_PATH)


def test_dataset_shape():
    df = load_data()
    assert df.shape == (100000, 15)


def test_required_columns():
    df = load_data()

    required_columns = [
        "customer_id",
        "age",
        "past_purchases",
        "product_views",
        "website_visits",
        "avg_order_value",
        "days_since_last_purchase",
        "loyalty_score",
        "cart_additions",
        "email_engagement",
        "customer_tenure",
        "product_interest_score",
        "previous_discount_usage",
        "discount",
        "purchase",
    ]

    assert all(column in df.columns for column in required_columns)


def test_no_missing_values():
    df = load_data()
    assert df.isnull().sum().sum() == 0


def test_age_range():
    df = load_data()
    assert df["age"].between(18, 70).all()


def test_loyalty_score_range():
    df = load_data()
    assert df["loyalty_score"].between(1, 100).all()


def test_product_interest_score_range():
    df = load_data()
    assert df["product_interest_score"].between(1, 100).all()


def test_discount_values():
    df = load_data()
    assert set(df["discount"].unique()).issubset({0, 10, 20})


def test_purchase_values():
    df = load_data()
    assert set(df["purchase"].unique()).issubset({0, 1})

def test_policy_results_shape():
    df = pd.read_csv("data/causal_policy_results.csv")
    assert df.shape == (100000, 16)


def test_policy_required_columns():
    df = pd.read_csv("data/causal_policy_results.csv")

    required_columns = [
        "customer_id",
        "p0_hat",
        "p10_hat",
        "p20_hat",
        "profit_0_hat",
        "profit_10_hat",
        "profit_20_hat",
        "recommended_discount",
        "recommended_profit_hat",
        "profit_gain_vs_no_discount",
        "persuadable"
    ]

    for column in required_columns:
        assert column in df.columns


def test_predicted_purchase_probabilities():
    df = pd.read_csv("data/causal_policy_results.csv")

    for column in ["p0_hat", "p10_hat", "p20_hat"]:
        assert df[column].between(0, 1).all()


def test_recommended_discount_values():
    df = pd.read_csv("data/causal_policy_results.csv")

    assert df["recommended_discount"].isin([0, 10, 20]).all()


def test_policy_results_no_missing_values():
    df = pd.read_csv("data/causal_policy_results.csv")

    columns_to_check = [
        "customer_id",
        "p0_hat",
        "p10_hat",
        "p20_hat",
        "profit_0_hat",
        "profit_10_hat",
        "profit_20_hat",
        "recommended_discount",
        "recommended_profit_hat",
        "profit_gain_vs_no_discount",
        "persuadable"
    ]

    assert df[columns_to_check].notna().all().all()


def test_profit_gain_is_non_negative():
    df = pd.read_csv("data/causal_policy_results.csv")

    assert (df["profit_gain_vs_no_discount"] >= 0).all()