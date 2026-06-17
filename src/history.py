import json

HISTORY_FILE = "data/history.json"

def load_history():

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(history):

    with open(HISTORY_FILE, "w") as f:
        json.dump(
            history,
            f,
            indent=2
        )

def make_job_id(job):

    return (
        job["company"]
        + "-"
        + job["title"]
        + "-"
        + job["url"]
    )

def get_seen_ids(history):

    return {
        item["id"]
        for item in history
    }

def get_new_jobs(jobs, history):

    seen_ids = get_seen_ids(history)

    new_jobs = []

    for job in jobs:

        job_id = make_job_id(job)

        if job_id not in seen_ids:
            new_jobs.append(job)

    return new_jobs

from datetime import date

def add_jobs_to_history(
    history,
    jobs
):

    today = str(date.today())

    for job in jobs:

        history.append({
            "id": make_job_id(job),
            "date_seen": today
        })

    return history
