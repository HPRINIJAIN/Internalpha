import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = "C:/Users/Rini jain hp/OneDrive/Desktop/salesdataset.csv"  # Update this if needed
df = pd.read_csv(file_path)

# Convert 'Order Date' to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract year and month
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# Aggregate monthly sales
monthly_sales = df.groupby(["Year", "Month"])['Amount'].sum().reset_index()

# Define a color palette
def generate_colors(n):
    return plt.cm.get_cmap("tab10", n).colors

# Plot sales trends using Matplotlib
def plot_sales_trends():
    plt.figure(figsize=(12, 6))
    colors = generate_colors(len(monthly_sales["Year"].unique()))
    for idx, year in enumerate(monthly_sales["Year"].unique()):
        yearly_data = monthly_sales[monthly_sales["Year"] == year]
        plt.plot(yearly_data["Month"], yearly_data["Amount"], marker="o", label=str(year), color=colors[idx])
    plt.title("Monthly Sales Trend Over Years", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Total Sales Amount", fontsize=12)
    plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.legend(title="Year")
    plt.grid(True)
    plt.show()

# Seasonal effects
seasonal_sales = df.groupby("Month")["Amount"].mean().reset_index()

def plot_seasonal_effects():
    plt.figure(figsize=(12, 6))
    colors = generate_colors(len(seasonal_sales))
    plt.bar(seasonal_sales["Month"], seasonal_sales["Amount"], color=colors)
    plt.title("Average Monthly Sales (Seasonal Effect)", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Average Sales Amount", fontsize=12)
    plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.grid(axis="y")
    plt.show()

# Category-wise sales and profit
category_performance = df.groupby("Category")[['Amount', 'Profit']].sum().reset_index()

def plot_category_performance():
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    colors = generate_colors(len(category_performance))
    ax[0].bar(category_performance["Category"], category_performance["Amount"], color=colors)
    ax[0].set_title("Total Sales by Category", fontsize=14)
    ax[0].set_xlabel("Category", fontsize=12)
    ax[0].set_ylabel("Total Sales Amount", fontsize=12)
    ax[0].grid(axis="y")
    ax[1].bar(category_performance["Category"], category_performance["Profit"], color=colors[::-1])
    ax[1].set_title("Total Profit by Category", fontsize=14)
    ax[1].set_xlabel("Category", fontsize=12)
    ax[1].set_ylabel("Total Profit", fontsize=12)
    ax[1].grid(axis="y")
    plt.tight_layout()
    plt.show()

# Sub-category performance
subcategory_performance = df.groupby("Sub-Category")[['Amount', 'Profit']].sum().reset_index()
subcategory_performance = subcategory_performance.sort_values(by="Profit", ascending=False)

def plot_subcategory_performance():
    plt.figure(figsize=(14, 6))
    colors = generate_colors(len(subcategory_performance))
    plt.barh(subcategory_performance["Sub-Category"], subcategory_performance["Profit"], color=colors)
    plt.title("Profit by Sub-Category", fontsize=14)
    plt.xlabel("Total Profit", fontsize=12)
    plt.ylabel("Sub-Category", fontsize=12)
    plt.grid(axis="x")
    plt.show()

# Run all plots
plot_sales_trends()
plot_seasonal_effects()
plot_category_performance()
plot_subcategory_performance()
