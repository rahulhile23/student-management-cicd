# Video Script (target: about 1 min 45 s)

Record in YOUR OWN voice (AI voice is not allowed). Both students should speak.
Screen-record while talking. Speak in your own words; this is a guide only.

**[0:00-0:15] Intro (Student 1, show GitHub repo)**
"Hello, we are <names> from B.Tech IT. For FA2 we built a CI/CD pipeline for an Agile project,
a Student Management System in Python, using GitHub Actions."

**[0:15-0:40] Agile plan (Student 1, show docs/AGILE_PLAN.md)**
"We wrote 5 user stories, for example adding students, searching, updating marks, deleting
records and viewing the topper. We planned two one-week sprints, defined our Definition of Done,
and wrote acceptance criteria for the update-marks story."

**[0:40-1:25] Pipeline (Student 2, show .github/workflows/ci-cd.yml, then Actions tab)**
"Our workflow runs on every push to GitHub. Stage one builds the app and installs dependencies.
Stage two runs automated tests with pytest and fails if coverage is below 80 percent.
Stage three is the code quality check using flake8. Stage four deploys: it packages the app
and uploads it as a release artifact. You can see all four jobs are green."

**[1:25-1:45] Wrap-up (Student 2)**
"This pipeline catches bugs before deployment. Thank you."
