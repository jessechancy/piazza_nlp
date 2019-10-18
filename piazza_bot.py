from scraper import gather_posts

class PiazzaBot():
    """Constructs message of unanswered piazza posts"""
    
    INTRO_BLOCK = {
        "type" : "section",
        "text" : {
            "type" : "mrkdwn",
            "text" : ("There are some unanswered piazza questions!")
        },
    }
    
    def __init__(self, channel):
        self.channel = channel
        self.username = "piazza_bot"
        self.unanswered = []
        
    def find_unanswered(self, length):
        posts = gather_posts(length)
        for id_key in posts.keys():
            if posts[id_key]["answered"] == False:
                unanswered_post = dict()
                unanswered_post["url"] = f"https://piazza.com/class/jz16gkwriwo4vr?cid={id_key}"
                unanswered_post["header"] = posts[id_key]["heading"]
                self.unanswered.append(unanswered_post)

    def get_json_payload(self):
        blocks = []
        blocks.append(self.INTRO_BLOCK)
        for post in self.unanswered:
            post_block = {
                "type" : "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"Question:{post['header']}\n"
                        f"URL: {post['url']}"
                    ),
                },
            }
            blocks.append(post_block)
        return ({"channel": self.channel,
                "username": "piazza_bot",
                "blocks": blocks})
                