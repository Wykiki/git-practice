# Git practice

## Description

This project is intended to show how users interacts on a Git project, and what
is the purpose of using an efficient Git branching workflow (Gitflow).

This project is supposed to be built with 2 peoples, or at list from 2 different
Git repositories. See [Build the project](#build-the-project) for more details.

## Run the project

### Docker

TODO

### Bare python / pip

Create your virtualenv (command depends on what you have installed, but with `virtualenvwrapper`) :

```
mkvirtualenv git-practice
workon git-practice
```

Install requirements :

```
pip install -r requirements.txt
```

And run the main :

```
python3 main.py
```

## Build the project

It is advised that you have a GitHub account.

For each Gitflow, you have to clone this project and push it up to a shared
remote, or fork it on GitHub.

### No Gitflow

We'll begin using no Gitflow, so you'll always stay on `master` branch.

There is 3 steps per user.  
At each step, you copy files from the step directory to the project directory.  
Then you push to master.

Some things should happen at some steps and you have to figure out why.

Example :

```
cp -rf steps/user1/step1/* ./
git add .
git commit -m 'Some commit message'
git push [-u origin master]
```

Let people working with you doing the same with its corresponding step, and work
with him to solve problems if any.

### GitHub Gitflow

We'll now use the [GitHub Gitflow](https://guides.github.com/introduction/flow/).

Same as above, there is 3 steps, but before you copy anything, you create a
`branch`.  
After you make your copy, you fetch latest informations about master, and rebase your
branch on master.
Then, once you pushed your branch, you go on GitHub to open a Pull request.

Example :

```
# To ensure we branch from master
git checkout master
git pull [origin master]
# Create and go on your new branch
git checkout -b user1-step1
cp -rf steps/user1/step1/* ./
git add .
git commit -m 'Some commit message'
git checkout master
git pull [-u origin master]
git checkout user1-step1
git rebase master
git push [-u origin user1-step1]
```

You need a bit more Git commands than above, but you will probably see some
advantage doing this Gitflow.

