import git
from git import Repo

def read_repo():
    myRepo = Repo('.')
    head = myRepo.heads

    for r in head:
        get_commits(myRepo, r)


def get_commits(repo, branch):
    print(branch.log())
    print(branch.name)
    commits = list(repo.iter_commits(branch.name,max_count=1))
    print(commits)
    for line in commits:
        print(line.committed_datetime)


if __name__ == "__main__":
    read_repo()


