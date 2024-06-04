import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# SAT scores and acceptance rates for each school
ivy_league_data = {
    'Yale': {'25th': 1470, '50th': 1540, '75th': 1560, 'acceptance_rate': 4.57},
    'Princeton': {'25th': 1510, '50th': 1540, '75th': 1570, 'acceptance_rate': 5.70},
    'UPenn': {'25th': 1500, '50th': 1540, '75th': 1570, 'acceptance_rate': 6.50},
    'Harvard': {'25th': 1490, '50th': 1550, '75th': 1580, 'acceptance_rate': 3.24},
    'Cornell': {'25th': 1470, '50th': 1520, '75th': 1550, 'acceptance_rate': 7.26},
    'Columbia': {'25th': 1500, '50th': 1540, '75th': 1560, 'acceptance_rate': 3.74},
    'Brown': {'25th': 1500, '50th': 1530, '75th': 1560, 'acceptance_rate': 5.06}
}

# Define the probability density function
def f(x, mean, std_dev=30):
    return norm.pdf(x, mean, std_dev)

# Function to find the percentile
def find_percentile(score, mean, std_dev=30):
    z = (score - mean) / std_dev
    percentile = norm.cdf(z)
    return percentile * 100

# Prompt the user to enter their SAT score
user_sat_score = float(input("Please enter your SAT score: "))

# Calculate and plot bell curves for each school
for school, data in ivy_league_data.items():
    mean = data['50th']
    std_dev = 30
    x = np.linspace(mean - 5 * std_dev, mean + 5 * std_dev, 1000)
    y = f(x, mean, std_dev)
    
    plt.plot(x, y, label=f'{school} SAT Score Distribution')
    
    # Fill the area under the curve to the left of the user's SAT score
    x_fill = np.linspace(mean - 5 * std_dev, user_sat_score, 1000)
    y_fill = f(x_fill, mean, std_dev)
    plt.fill_between(x_fill, y_fill, color='blue', alpha=0.3)
    
    # Calculate the percentile
    percentile = find_percentile(user_sat_score, mean, std_dev)
    
    # Add titles and labels
    plt.title(f'{school} SAT Score Distribution\nYour SAT Score Percentile: {percentile:.2f}%')
    plt.xlabel('SAT Score')
    plt.ylabel('Density')
    plt.legend()
    
    # Show the plot
    plt.show()

# Calculate the admission probabilities based on percentiles and acceptance rates
admission_probabilities = []
for school, data in ivy_league_data.items():
    mean = data['50th']
    acceptance_rate = data['acceptance_rate'] / 100
    percentile = find_percentile(user_sat_score, mean)
    admission_prob = (percentile / 100) * acceptance_rate  # Estimate probability
    admission_probabilities.append(admission_prob)

# Calculate the probability of getting into at least one school
def probability_at_least_one(num_schools, admission_probabilities):
    p_none = np.prod([1 - p for p in admission_probabilities[:num_schools]])
    return 1 - p_none

# Plot the graph
num_schools_range = range(1, len(ivy_league_data) + 1)
probabilities = [probability_at_least_one(n, admission_probabilities) for n in num_schools_range]

plt.figure(figsize=(10, 6))
plt.plot(num_schools_range, probabilities, marker='o')
plt.title('Probability of Getting into at Least One Ivy League School')
plt.xlabel('Number of Ivy League Schools Applied To')
plt.ylabel('Probability of Getting In')
plt.grid(True)
plt.show() 