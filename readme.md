**Requirements**
- Python 3.x
- requests library 
- matplotlib library 
- A GitHub Personal Access Token with read access to the repository (more information on how to create a token (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))

**Usage**

To use this program, follow these steps:
- Clone or download the repository to your local machine.
- Install the required libraries by running pip install -r requirements.txt.
- Replace the REPO_OWNER, REPO_NAME and AUTH_HEADER variables in the script with the appropriate values for the repository you want to monitor and your GitHub Personal Access Token.
- Run the script using the command python main.py.
- The program will retrieve data from the GitHub API, monitor the number of commits made in the past week, and generate different visualizations

**Visualizations** 

The program generates 4 visualizations to provide insights into the activity of the community of contributors:
- This functions **plot_contributors_data** will display a scatter plot that shows the correlation between the total number of contributors and the number of contributions from each contributor. If the points on the graph are clustered along a diagonal line, it suggests a positive correlation between the two variables, indicating that the number of contributions is indeed correlated with the total number of contributors.
- This function **plot_contributions_histogram(contributors_data)** is used to plot a histogram of the contributions to the repository by each contributor. The x-axis represents the number of contributions, while the y-axis represents the number of contributors who have made that number of contributions.
The histogram allows visualizing the distribution of contributions by contributors. By observing the shape of the histogram, it is possible to determine whether the majority of contributions come from a small group of very active contributors or if the contributions are more evenly distributed among different contributors. This information can help better understand the dynamics of the contributor community and identify the most active contributors.
- This function **plot_contributions_by_contributor(contributors_data)** will display a pie chart that shows the distribution of contributions among the different contributors. If the chart shows that a small number of contributors make the majority of contributions, it could indicate that the project is dominated by a small group of individuals, which could have implications for the long-term sustainability of the project.
- This function **plot_contributions_over_time** will display a bar chart showing the total number of contributions per week over time. If the chart shows spikes in activity, it could indicate periods of particular interest for the project or periods of intensive work.

