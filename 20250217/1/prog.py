from git import Repo
import sys

# Функция для вывода всех веток в репозитории
def list_branches(repo):
    branches = repo.branches
    for branch in branches:
        print(branch.name)

# Функция для вывода информации о последнем коммите указанной ветки
def get_last_commit(repo, branch_name):
    branch = repo.heads[branch_name]
    commit = branch.commit
    print(f"tree {commit.tree.hexsha}")  # Вывод хеша дерева коммита
    print(f"parent {commit.parents[0].hexsha if commit.parents else ''}")  # Вывод хеша родительского коммита
    print(f"author {commit.author.name} <{commit.author.email}>")  # Вывод информации об авторе
    print(f"committer {commit.committer.name} <{commit.committer.email}>")  # Вывод информации о коммитере
    print(commit.message)  # Вывод сообщения коммита

# Функция для вывода дерева последнего коммита
def print_tree(tree):
    for item in tree:
        print(f"{item.type} {item.hexsha}    {item.name}")  # Вывод типа, хеша и имени элемента дерева

# Функция для вывода дерева последнего коммита указанной ветки
def get_tree_of_last_commit(repo, branch_name):
    branch = repo.heads[branch_name]
    commit = branch.commit
    tree = commit.tree
    print_tree(tree)

# Функция для прохода по истории коммитов и вывода дерева для каждого коммита
def walk_history(repo, branch_name):
    branch = repo.heads[branch_name]
    commit = branch.commit
    while commit:
        print(f"TREE for commit {commit.hexsha}")  # Вывод информации о дереве для каждого коммита
        print_tree(commit.tree)
        commit = commit.parents[0] if commit.parents else None  # Переход к родительскому коммиту

# Основная функция для выполнения программы
def main():
    if len(sys.argv) < 2:
        print("Usage: python git_viewer.py <path_to_repo> [branch_name]")
        return

    repo_path = sys.argv[1]
    repo = Repo(repo_path)  # Инициализация репозитория

    if len(sys.argv) == 2:
        list_branches(repo)  # Вывод всех веток, если не указана ветка
    elif len(sys.argv) == 3:
        branch_name = sys.argv[2]
        get_last_commit(repo, branch_name)  # Вывод последнего коммита указанной ветки
        get_tree_of_last_commit(repo, branch_name)  # Вывод дерева последнего коммита
        walk_history(repo, branch_name)  # Проход по истории коммитов

if __name__ == "__main__":
    main()
