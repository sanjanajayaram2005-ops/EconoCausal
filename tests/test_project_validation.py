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