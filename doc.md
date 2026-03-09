**Version Control and Change Management – Git Workflow Documentation**

**Repository Link:**
https://github.com/nandan645/soft-ass-5

---

# 1. Introduction

This document describes the configuration management workflow implemented using Git and GitHub CLI for a Python To-Do List application. The workflow demonstrates repository initialization, branch management, feature development, bug fixing, and merging changes into the main branch.

---

# 2. Repository Initialization

A new Git repository was initialized for the project directory.

Commands used:

```
git init
ni todo.py
```

Explanation:

* `git init` created an empty Git repository.
* `todo.py` was created to store the Python To-Do application.

---

# 3. Creating the Remote Repository

GitHub CLI was used to create and connect a remote repository.

Command used:

```
gh repo create soft-ass-5 --public --source=. --remote=origin --push
```

This command performed the following actions:

* Created a public GitHub repository named **soft-ass-5**
* Linked the local repository to GitHub using the **origin** remote
* Pushed the **main branch** to GitHub

---

# 4. Branching Strategy

Separate branches were used for development and bug fixing.

Branches created:

| Branch    | Purpose                          |
| --------- | -------------------------------- |
| main      | Stable production-ready code     |
| feature-1 | Development of a new feature     |
| bug-fix   | Fixing issues in the application |

Commands used:

```
git checkout -b feature-1
git checkout -b bug-fix
```

---

# 5. Feature Development

A new feature was implemented on the **feature-1** branch.

Commands used:

```
git add todo.py
git commit -m "added a feature"
git push origin feature-1
```

Commit Message:

```
added a feature
```

Description:

* Code was modified to add additional functionality to the To-Do list application.
* The changes were committed and pushed to the remote repository.

---

# 6. Bug Fix Implementation

A bug fix was implemented on the **bug-fix** branch.

Commands used:

```
git add .
git commit -m "simple bug fix"
git push origin bug-fix
```

Commit Message:

```
simple bug fix
```

Description:

* Minor issues in the code were corrected.
* Improvements were made to the program logic.

---

# 7. Merging Branches into Main

After development and testing, both branches were merged into the **main** branch.

Commands used:

```
git checkout main
git merge feature-1
git merge bug-fix
git push origin main
```

Explanation:

* The feature branch was merged into the main branch.
* The bug-fix branch was also merged into the main branch.
* The updated main branch was pushed to the remote repository.

Git performed **fast-forward merges**, meaning there were no conflicting changes between the branches.

---

# 8. Commit History

The commit history was checked using:

```
git log --oneline --graph --all
```

Output:

```
* 185780e simple bug fix
* e4662db added a feature
* 3a0bb7a initial code
```

Explanation:

| Commit ID | Message         | Description                           |
| --------- | --------------- | ------------------------------------- |
| 3a0bb7a   | initial code    | Added the initial To-Do application   |
| e4662db   | added a feature | Implemented new feature functionality |
| 185780e   | simple bug fix  | Fixed issues in the code              |

---
