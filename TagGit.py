import os
import git

def generate_release_notes(repo_path, start_tag, end_tag):
    repo = git.Repo(repo_path)
    commits = list(repo.iter_commits(f"{start_tag}..{end_tag}"))

    release_notes = {
        'features': [],
        'bug_fixes': [],
        'enhancements': [],
        'documentation': []
    }

    for commit in commits:
        message = commit.message.lower()
        if 'feat:' in message:
            release_notes['features'].append(commit.message[5:])
        elif 'fix:' in message:
            release_notes['bug_fixes'].append(commit.message[4:])
        elif 'enhancement:' in message:
            release_notes['enhancements'].append(commit.message[12:])
        elif 'docs:' in message:
            release_notes['documentation'].append(commit.message[5:])

    return release_notes

def format_release_notes(release_notes):
    formatted_notes = "# Release Notes\n\n"
    
    for category, notes in release_notes.items():
        if notes:
            formatted_notes += f"## {category.capitalize()}\n\n"
            for note in notes:
                formatted_notes += f"- {note}\n"
            formatted_notes += "\n"
    
    return formatted_notes

def main():
    print("Git Release Notes Generator")
    print("----------------------------")
    
    repo_path = input("Enter the path to the Git repository: ")
    start_tag = input("Enter the start tag: ")
    end_tag = input("Enter the end tag: ")
    
    if not os.path.exists(repo_path):
        print("Repository path does not exist.")
        return

    release_notes = generate_release_notes(repo_path, start_tag, end_tag)
    formatted_notes = format_release_notes(release_notes)

    print("\nGenerated Release Notes:")
    print(formatted_notes)

if __name__ == "__main__":
    main()
