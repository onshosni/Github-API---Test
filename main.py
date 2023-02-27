import requests
import datetime
import json
import os
import matplotlib.pyplot as plt
import numpy as np


# Définition des constantes
API_BASE_URL = "https://api.github.com"
REPO_OWNER = "pandas-dev"
REPO_NAME = "pandas"
AUTH_HEADER = {"Authorization": "token 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"}


# Fonction pour envoyer des requêtes à l'API GitHub
def send_request(url):
    response = requests.get(url, headers=AUTH_HEADER)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("La requête a échoué avec le code d'erreur %s" % response.status_code)


# Fonction pour récupérer la liste des contributeurs au repository pandas
def get_contributors():
    contributors_url = API_BASE_URL + "/repos/%s/%s/contributors" % (REPO_OWNER, REPO_NAME)
    contributors = send_request(contributors_url)
    return contributors


# Fonction pour formater les données des contributeurs
def format_contributors_data(contributors):
    formatted_data = {}
    for contributor in contributors:
        login = contributor['login']
        formatted_data[login] = {
            "id": contributor['id'],
            "contributions": contributor['contributions']
        }
    return formatted_data


# Fonction pour monitorer le nombre de commits journaliers
def monitor_commits():
    commits_url = API_BASE_URL + "/repos/%s/%s/stats/participation" % (REPO_OWNER, REPO_NAME)
    stats = send_request(commits_url)
    commit_counts = stats['all']
    last_week_commit_counts = commit_counts[-7:]
    for commit_count in last_week_commit_counts:
        if commit_count < 2:
            today = datetime.date.today()
            with open("commits_monitor.txt", "a") as f:
                f.write("%s: Nombre de commits : %s\n" % (today, commit_count))

def plot_contributors_data(contributors_data):
    contributor_count = len(contributors_data)
    contributions = [data["contributions"] for data in contributors_data.values()]
    plt.scatter(range(contributor_count), contributions)
    plt.xlabel('Contributeur')
    plt.ylabel('Nombre de contributions')
    plt.title('Corrélation entre le nombre de contributions de chaque contributeur et le nombre total de contributeurs')
    plt.show()


def plot_contributions_histogram(contributors_data):
    contributions = [data['contributions'] for data in contributors_data.values()]
    plt.hist(contributions, bins=np.arange(0, max(contributions), 10))
    plt.xlabel('Contributions')
    plt.ylabel('Nombre de contributeurs')
    plt.title('Histogramme des contributions')
    plt.show()

def plot_contributions_over_time(contributors_data):
    weekly_contributions_url = API_BASE_URL + "/repos/%s/%s/stats/commit_activity" % (REPO_OWNER, REPO_NAME)
    weekly_contributions = send_request(weekly_contributions_url)
    weeks = [datetime.datetime.fromtimestamp(w['week']) for w in weekly_contributions]
    contributions = [w['total'] for w in weekly_contributions]
    plt.bar(weeks, contributions)
    plt.xlabel('Semaine')
    plt.ylabel('Nombre de contributions')
    plt.title('Activité des contributeurs au fil du temps')
    plt.show()

def plot_contributions_by_contributor(contributors_data):
    contributor_names = [name for name in contributors_data.keys()]
    contributions = [data['contributions'] for data in contributors_data.values()]
    plt.pie(contributions, labels=contributor_names)
    plt.title('Répartition des contributions par contributeur')
    plt.show()

# Main program
if __name__ == '__main__':
    contributors = get_contributors()
    contributors_data=format_contributors_data(contributors)
    monitor_commits()
    plot_contributors_data(contributors_data)
    plot_contributions_histogram(contributors_data)
    plot_contributions_over_time(contributors_data)
    plot_contributions_by_contributor(contributors_data)
