from datetime import datetime, timedelta


def find_the_oldies(flags) -> list:
    stale_flags = []
    now = datetime.now()
    cutoff_date = now - timedelta(days=30)
    created_cutoff = now - timedelta(days=90)

    for flag in flags:
        created_date = datetime.strptime(flag["created_at"], "%Y-%m-%d")
        updated_at = datetime.strptime(flag["updated_at"], "%Y-%m-%d")
        enabled_date = None

        if flag["enabled_at"] is not None:
            enabled_date = datetime.strptime(flag["enabled_at"], "%Y-%m-%d")

        if flag["permanent"] == True:
            continue

        if created_date < created_cutoff and created_date == updated_at:
            stale_flags.append(flag["name"])
            continue
        
        if flag["enabled_for_all"] == True and enabled_date != None and enabled_date < cutoff_date:
            stale_flags.append(flag["name"])
            continue

    return stale_flags

if __name__ == "__main__":
    flags = [
    { "name": "new_graph_question",
    "created_at": "2024-10-01", "updated_at": "2024-10-01",
    "enabled_for_all": True, "enabled_at": "2024-10-05", "permanent": False },
    { "name": "legacy_video_embed",
    "created_at": "2023-06-01", "updated_at": "2023-06-01",
    "enabled_for_all": False, "enabled_at": None, "permanent": False },
    { "name": "accessibility_mode",
    "created_at": "2022-01-01", "updated_at": "2024-12-01",
    "enabled_for_all": True, "enabled_at": "2022-01-15", "permanent": True }
]

    expected = ["new_graph_question", "legacy_video_embed"]
    stale_flags = find_the_oldies(flags)
    print("Stale flags:", stale_flags)
    assert stale_flags == expected



"""
My notes

  Clarifying for self:
- Check if flag is explicitly marked as permanent; if yes 'continue' 
- Check if created_at is more than 90 days prior AND updated_at is the same date
- Check if enabled_for_all == True AND enabled_at no more than 30 days old

  Edge cases for unit tests:
- enabled_at is exactly 30 days SHOULD REMAIN VALID
- enabled_at is exactly 31 days SHOULD BE INVALID
- enabled_for_all True but enabled_at None; if there is a case for that
- created_at greater than 90 days and hasn't been modified (happy path) STALE
- created_at greater than 90 days but has been modified (unhappy path) FRESH

  If stale flags are needed to auto-generate a GitHub issue:
We would write a new function to cater for that concern - we don't want any one
function to be trying to do too much

def stale_flags_github_issue():
  stale_flags = find_the_oldies(flags)
  ...
  return 

  Data structure to use to process 100,000 flags efficiently:
- This is already efficient for single-pass events, list is great here if we're
talking in-memory
- If the data is coming from a database, you'd push the filtering into SQL rather
than Python
- I'd also just revise the thing for any redundancy, I've tried to avoid repeated
calls but there might be more elegant/clever solutions. Actually I can see the
.strptime() is iterating every loop so I may take that out.




Task: Practical Technical Task

  The scenario
You're a junior engineer on Stile's platform team. Feature flags — used to roll out new question types — are
being left active long after features ship, cluttering the codebase. Your tech lead asks you to write a script
that audits feature flags and identifies any that look stale.

  What you need to build
Write a Python function that takes a list of feature flags and returns the stale ones:
• A flag is stale if it has been enabled for all users for more than 30 days
• A flag is stale if it was created more than 90 days ago and has never been modified
• A flag is NOT stale if it is explicitly marked as permanent
Each flag is a dict with: name, created_at, updated_at, enabled_for_all, enabled_at, permanent

  Example input
flags = [
{ "name": "new_graph_question",
"created_at": "2024-10-01", "updated_at": "2024-10-01",
"enabled_for_all": True, "enabled_at": "2024-10-05", "permanent": False },
{ "name": "legacy_video_embed",
"created_at": "2023-06-01", "updated_at": "2023-06-01",
"enabled_for_all": False, "enabled_at": None, "permanent": False },
{ "name": "accessibility_mode",
"created_at": "2022-01-01", "updated_at": "2024-12-01",
"enabled_for_all": True, "enabled_at": "2022-01-15", "permanent": True }
]

  Expected output
["new_graph_question", "legacy_video_embed"]
accessibility_mode is excluded — it is marked permanent.

  Stretch questions
• How would you modify the function if stale flags needed to auto-generate a GitHub issue?
• What data structure would you use to process 100,000 flags efficiently?
• How would you write a unit test for this function?
"""