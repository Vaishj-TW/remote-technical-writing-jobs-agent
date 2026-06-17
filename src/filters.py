KEYWORDS = [
    "content designer",
    "ux writer",
    "technical writer",
    "senior technical writer",
    "documentation engineer",
    "staff technical writer",
    "principal technical writer"
]

def is_relevant(job):

    title = job["title"].lower()

    return any(
        keyword in title
        for keyword in KEYWORDS
    )

def is_remote(job):

    location = job["location"].lower()

    remote_terms = [
        "remote",
        "worldwide",
        "distributed",
        "anywhere"
    ]

    return any(
        term in location
        for term in remote_terms
    )

def allows_india(job):

    text = (
        job["title"]
        + " "
        + job["location"]
    ).lower()

    blocked = [
        "us only",
        "canada only",
        "europe only",
        "uk only"
    ]

    return not any(
        item in text
        for item in blocked
    )
