# Student Management System: CI/CD with GitHub Actions

Pipeline: **GitHub -> Build -> Automated Testing -> Code Quality Check -> Deployment**

## Run locally
```
pip install -r requirements.txt
python main.py
pytest --cov=student_mgmt
flake8 .
```

See `docs/AGILE_PLAN.md` for user stories, sprint plan, DoD and acceptance criteria.
