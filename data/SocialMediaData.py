class SocialMediaData:
    def __init__(self, tiktok_paths, instagram_paths, X_paths):
        pass

        self.tiktok_paths = tiktok_paths
        self.instagram_paths = instagram_paths
        self.X_paths = X_paths

        self.tiktokAcc = {}
        self.instagramAcc = {}
        self.xAcc = {}

    def fetch_acc_info(self, source):
        return source.get("info", [])
    def fetch_posts(self, source):
        return source.get("posts", [])
    def fetch_shares(self, source):
        return source.get("shares", [])
    def fetch_likes(self, source):
        return source.get("likes", [])
    def fetch_comments(self, source):
        return source.get("comments", [])

    def fetch_X_data(self):
        source = self.X_paths
        self.xAcc = {
            "info": self.fetch_acc_info(source),
            "posts": self.fetch_posts(source),
            "shares": self.fetch_shares(source),
            "likes": self.fetch_likes(source),
            "comments": self.fetch_comments(source),
        }
        return self.xAcc
        
    def fetch_Instagram_data(self):
        source = self.instagram_paths
        self.instagramAcc = {
            "info": self.fetch_acc_info(source),
            "posts": self.fetch_posts(source),
            "shares": self.fetch_shares(source),
            "likes": self.fetch_likes(source),
            "comments": self.fetch_comments(source),
        }
        return self.instagramAcc

    def fetch_Tiktok_data(self):
        source = self.tiktok_paths
        self.tiktokAcc = {
            "info": self.fetch_acc_info(source),
            "posts": self.fetch_posts(source),
            "shares": self.fetch_shares(source),
            "likes": self.fetch_likes(source),
            "comments": self.fetch_comments(source),
        }
        return self.tiktokAcc
