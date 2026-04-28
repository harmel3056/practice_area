from datetime import datetime, date


def stale_flag_detector(flags) -> list:
    stale_flags = []
    current_date = datetime.now().date()

    for flag in flags:
        if flag["permanent"] == True:
            continue
        
        created_date = datetime.strptime(flag["created_at"], "%Y-%m-%d")
        days_old = (current_date - created_date.date()).days

        if days_old > 90 and flag["updated_at"] == flag["created_at"]:
            stale_flags.append(flag["name"])
            continue
        
        if flag["enabled_for_all"] == True and flag["enabled_at"] is not None:
            enabled_date = datetime.strptime(flag["enabled_at"], "%Y-%m-%d").date()
            if (current_date - enabled_date).days > 30:
                stale_flags.append(flag["name"])

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

    print(stale_flag_detector(flags))


"""
How would I modify the function if stale flags needed to auto-generate
a GitHub issue?
I don't presently know anything about GitHub issue generation, however
if the flags are needed for its purpose then I would most likely implement
this as a helper function, rather than try to create a hybrid purpose function.

What data structure would I use to process 100,000 flags efficiently?
I THINK this function is O(n) as it isn't running any loops or anything like
that. If a list of names is needed then I think this data structure is
sufficient.

How would I write a unit test for this function?
I would likely build a pytest that can be automated with GH Actions. Some edge
cases I would start with are:
- what happens when flag has been enabled for 30 days exactly (Expected: not added to list)
- what happens when flag was created 90 days ago, has not been modified (Expected: not added to list)
- what happens when a flag was created 91 days ago but has been modified (Expected: not added to list)
- what happens when a flag was created 91 days ago and has not been modified (Expected: added to list)
- what happens when a flag is marked as permanent (Expected: not added to list)
- what happens when enabled_for_all is False and enabled_at is None (Expected: not added to list)
- and then a few happy path additions


flags = [
{ 
"name": "new_graph_question",
"created_at": "2024-10-01", 
"updated_at": "2024-10-01",
"enabled_for_all": True, 
"enabled_at": "2024-10-05", 
"permanent": False },

{ "name": "legacy_video_embed",
"created_at": "2023-06-01", 
"updated_at": "2023-06-01",
"enabled_for_all": False, 
"enabled_at": None, 
"permanent": False },

{ "name": "accessibility_mode",
"created_at": "2022-01-01", 
"updated_at": "2024-12-01",
"enabled_for_all": True, 
"enabled_at": "2022-01-15", 
"permanent": True }
]
"""
