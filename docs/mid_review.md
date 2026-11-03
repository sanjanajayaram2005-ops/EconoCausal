# EconoCausal Mid-Review

## Project Objective

EconoCausal aims to estimate the causal effect of different discount levels on customer purchases and use these treatment effects to recommend a personalized discount that maximizes expected profit.

## Dataset

The project uses a synthetic retail dataset containing 100,000 customer records and 15 features.

The treatment variable is discount, with three levels:

- ?0
- ?10
- ?20

The outcome variable is purchase.

## Methodology

The project workflow consists of:

1. Data Generation
2. Data Validation
3. Exploratory Data Analysis
4. Causal Modeling
5. Treatment Effect Estimation
6. Personalized Pricing Policy
7. Policy Evaluation
8. Visualization

Double Machine Learning is used for causal effect estimation with EconML and DoWhy.

## Personalized Pricing

For each customer, the model estimates purchase probabilities under the three discount scenarios and calculates the corresponding expected profit.

The discount with the highest expected profit is selected as the customer's recommended discount.

## Current Results

- Policy accuracy: 89.18%
- Average profit before policy: ?181.46
- Average profit after policy: ?237.43
- Estimated improvement: 30.8%

## Validation

Automated validation tests have been implemented for both the dataset and causal policy results.

Current test suite:

- 14 tests
- 14 passed

## Dashboard

A Streamlit and Plotly dashboard is used to visualize customer-level recommendations, treatment effects, pricing policy results, and business impact.

## Current Status

The core causal pricing workflow has been implemented and validated. The current focus is on project refinement, documentation, testing, and final presentation.

## Limitation

The dataset is synthetic, so the current results demonstrate the methodology and simulated business impact. Real-world deployment would require validation using real customer data and controlled experiments.
