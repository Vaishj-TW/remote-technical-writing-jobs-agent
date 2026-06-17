import requests
def get_greenhouse_jobs(companies):

    jobs = []

    for company in companies:

        slug = company["slug"]

        url = (
            "https://boards-api.greenhouse.io/v1/boards/"
            f"{slug}/jobs"
        )

        try:

            data = requests.get(url).json()

            for job in data.get("jobs", []):

                jobs.append({
                    "title": job["title"],
                    "company": company["name"],
                    "location": job["location"]["name"],
                    "url": job["absolute_url"],
                    "description": ""
                })

        except Exception as e:

            print(e)

    return jobs

def get_lever_jobs(companies):

    jobs = []

    for company in companies:

        slug = company["slug"]

        url = (
            f"https://api.lever.co/v0/postings/"
            f"{slug}?mode=json"
        )

        try:

            data = requests.get(url).json()

            for job in data:

                jobs.append({
                    "title": job["text"],
                    "company": company["name"],
                    "location": job["categories"]["location"],
                    "url": job["hostedUrl"],
                    "description": ""
                })

        except Exception as e:

            print(e)

    return jobs

def get_ashby_jobs(companies):

    jobs = []

    for company in companies:

        slug = company["slug"]

        url = (
            "https://api.ashbyhq.com/"
            f"posting-api/job-board/{slug}"
        )

        try:

            response = requests.get(url)

            data = response.json()

            for job in data.get("jobs", []):

                jobs.append({
                    "title": job.get("title", ""),
                    "company": company["name"],
                    "location": (
                        job.get("location", {})
                        .get("name", "")
                    ),
                    "url": job.get("jobUrl", ""),
                    "description": ""
                })

        except Exception as e:

            print(e)

    return jobs
