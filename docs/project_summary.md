# EconoCausal – Project Summary

## Project Overview

EconoCausal is a dynamic pricing optimization system that uses causal machine
learning to estimate the effect of different discount levels on customer
purchases and identify personalized pricing strategies.

## Methodology

The project uses Double Machine Learning (DML) to estimate customer-level
treatment effects for discount values of ₹0, ₹10 and ₹20.

The workflow includes:

1. Synthetic customer dataset generation
2. Data preprocessing and validation
3. Exploratory data analysis
4. Causal effect estimation using EconML
5. Causal validation using DoWhy
6. Personalized pricing policy generation
7. Expected-profit optimization
8. Streamlit dashboard development

## Dataset

The synthetic dataset contains 100,000 customer records and 15 features,
including customer demographics, purchase history, engagement features,
discount information and purchase outcome.

## Results

The personalized pricing policy achieved 89.18% policy accuracy.

Estimated average profit improved from ₹181.46 per customer under the
baseline strategy to ₹237.43 per customer under the optimized policy,
representing an estimated improvement of 30.8%.

## Dashboard

The Streamlit dashboard presents:

- Pricing recommendations
- Customer-level insights
- Treatment effects
- Policy performance
- Business impact analysis

