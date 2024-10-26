Visualizations:

    Use matplotlib to create daily weather summary graphs:

    python

import matplotlib.pyplot as plt

def plot_daily_summary(summary):
    plt.plot(summary['date'], summary['avg_temp'], label="Average Temperature")
    plt.plot(summary['date'], summary['max_temp'], label="Max Temperature")
    plt.plot(summary['date'], summary['min_temp'], label="Min Temperature")
    plt.legend()
    plt.show()
