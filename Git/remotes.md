### Git remotes
- Checking remotes
```bash
git remote -v
```

- Adding a new remote 
```bash
git remote set-url add <reference> <remote_link>
git remote set-url add origin git@github.com:joaov777/study.git
git remote set-url add remote_gitlab git@gitlab.com:joaov777/myrepo.git
```
- Adding remote with automatic repo name
```bash
# gitlab
git remote add "$(basename -s .git $(git config --get remote.origin.url))_gitlab" git@gitlab.com:joaov777/"$(basename -s .git `git config --get remote.origin.url`)"

# github
git remote add "$(basename -s .git $(git config --get remote.origin.url))_github" git@github.com:joaov777/"$(basename -s .git `git config --get remote.origin.url`)"
```

- Pushing to multiple remotes 
```bash
git push study_github && git push study_gitlab 
```




