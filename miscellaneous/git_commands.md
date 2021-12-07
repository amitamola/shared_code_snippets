### Some useful git commands

**to initialize git-**  
```git init```

**tells the current directory-**  
```git status```

**adds a file to the Git staging area-**  
``git add .``

**captures a snapshot of the project's currently staged changes-**  
```git commit -m "MESSAGE"```

**a utility tool to review and read a history of everything that happens to a repository**  
```git log```

**Create new branch and checkout-**  
```git checkout -b <branch_name>```

**Push changes to master for creating pull request-**  
```git push -u origin <branch>```

*******************************************
#### If you made some changes but someone else in the team made them too including new change and then if you try to pull, it won't happen until you commit. So you can just reset and now you can do pull. There is another option of performing stash, but that is a long case.
```git reset --hard```

**Reset the HEAD to this old commit-**  
```git reset --hard <old commit number>```

**additionally, you need to use git push -f origin to alter the remote repo too-**  
```git push -f origin```
*******************************************
