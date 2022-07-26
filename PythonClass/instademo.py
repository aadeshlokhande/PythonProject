from instapy import InstaPy
from instapy import smart_run

id = "tech_in_seconds"
password = "ppopploo"

session =InstaPy(username = id,
                password = password,
                headless_browser = False)

with smart_run(session):
    session.set_relationship_bounds(
        enabled = True,
        delimit_by_numbers = True,
        max_followers = 500,
        min_followers = 30,
        min_following = 50
    )

    target_users = session.target_list("user.txt")
    session.follow_by_list(target_users,times = 1, sleep_delay = 600)