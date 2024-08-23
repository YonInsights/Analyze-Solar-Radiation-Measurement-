import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

def load_data(file_path):
    data = pd.read_csv(file_path)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data.set_index('Timestamp', inplace=True)
    return data

def plot_time_series(data, title):
    plt.figure(figsize=(14, 7))
    plt.plot(data['GHI'], label='GHI')
    plt.plot(data['DNI'], label='DNI')
    plt.plot(data['DHI'], label='DHI')
    plt.plot(data['Tamb'], label='Tamb')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.show()

def plot_heatmap(data, title):
    plt.figure(figsize=(12, 8))
    sns.heatmap(data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr(), annot=True, cmap='coolwarm')
    plt.title(title)
    plt.show()

def plot_wind_polar(data, title):
    wd_rad = np.deg2rad(data['WD'])
    plt.figure(figsize=(10, 8))
    ax = plt.subplot(111, polar=True)
    ax.scatter(wd_rad, data['WS'], alpha=0.75, c=data['WS'], cmap='viridis', edgecolors='w', linewidth=0.5)
    ax.set_title(title, va='bottom')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    plt.show()

def plot_temp_humidity_scatter(data, title):
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='RH', y='Tamb', data=data)
    plt.title(f'Relative Humidity vs Temperature in {title}')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature (°C)')
    plt.show()

def plot_histogram(data, variable, title):
    plt.figure(figsize=(10, 6))
    plt.hist(data[variable].dropna(), bins=30, edgecolor='k', alpha=0.7)
    plt.title(f'{variable} Distribution in {title}')
    plt.xlabel(variable)
    plt.ylabel('Frequency')
    plt.show()

def calculate_z_scores(data, variables):
    z_scores = pd.DataFrame()
    for var in variables:
        z_scores[var] = (data[var] - data[var].mean()) / data[var].std()
    return z_scores

def flag_significant_points(z_scores):
    significant_points = (z_scores.abs() > 3).any(axis=1)
    return significant_points

def plot_significant_points(data, significant_points, variable, title):
    plt.figure(figsize=(12, 8))
    plt.scatter(data.index, data[variable], c=significant_points, cmap='coolwarm', alpha=0.6)
    plt.title(f'Significant Data Points in {title} for {variable}')
    plt.xlabel('Time')
    plt.ylabel(variable)
    plt.show()

def plot_bubble_chart(data, x_var, y_var, size_var, color_var, title):
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(data[x_var], data[y_var], s=data[size_var] * 10, c=data[color_var], cmap='viridis', alpha=0.6, edgecolors='w', linewidth=0.5)
    plt.title(title)
    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.colorbar(scatter, label=color_var)
    plt.show()