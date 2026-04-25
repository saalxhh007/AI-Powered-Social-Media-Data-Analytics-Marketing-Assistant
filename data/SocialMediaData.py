import os
import json
import pandas as pd

class SocialMediaData:
    def __init__(self, tiktok_paths, instagram_paths, X_paths):
        pass

        self.tiktok_paths = tiktok_paths
        self.instagram_paths = instagram_paths
        self.X_paths = X_paths

        self.tiktokAcc = {}
        self.instagramAcc = {}
        self.xAcc = {}

    def load_data(self, path):
        # print(path)
        if not path or not os.path.exists(path):
            return "Specify a file path"
        
        # CSV
        if path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
            
        elif path.endswith(".csv"):
            return pd.read_csv(path)
        
        return r'Not a Valid csv/json {path}'
            
    def fetch_acc_info(self, source):
        return self.load_data(source.get("info"))
    def fetch_posts(self, source):
        return self.load_data(source.get("posts"))
    def fetch_comments(self, source):
        path = source.get("comments")
        comments = []
        for f in os.listdir(path):
            file_path = os.path.join(path, f)
            data = self.load_data(file_path)
            if data:
                comments.append(data)
        return comments

    def fetch_X_data(self):
        source = self.X_paths
        self.xAcc = {
            "info": self.fetch_acc_info(source),
            "posts": self.fetch_posts(source),
            "comments": self.fetch_comments(source),
        }
        return self.xAcc
        
    def fetch_Instagram_data(self):
        source = self.instagram_paths
        self.instagramAcc = {
            "info": self.fetch_acc_info(source),
            "posts": self.fetch_posts(source),
            "comments": self.fetch_comments(source),
        }
        return self.instagramAcc

    def fetch_Tiktok_data(self):
        source = self.tiktok_paths
        self.tiktokAcc = {
            "info": self.fetch_acc_info(source),
            "posts": self.fetch_posts(source),
            "comments": self.fetch_comments(source),
        }
        return self.tiktokAcc

    def preprocess(self, preprocess):
        return preprocess
    
tiktok_paths = {
    "info": "./tiktok/info.json",
    "posts": "./tiktok/posts.json",
    "comments": "./tiktok/comments",
}
x_paths = {
    "info": "./x/info.json",
    "posts": "./x/posts.json",
    "comments": "./x/comments",
}
instagram_paths = {
    "info": "./instagram/info.json",
    "posts": "./instagram/posts.json",
    "comments": "./instagram/comments",
}

# accounts = SocialMediaData(tiktok_paths, x_paths, instagram_paths)

# insta_data = accounts.fetch_Instagram_data()
# tiktok_data = accounts.fetch_Tiktok_data()
# x_data = accounts.fetch_X_data()

# print("\n===== ACCOUNTS INFO =====")
# print(json.dumps(insta_data.get("info", {}), indent=4, default=str))
# print(json.dumps(tiktok_data.get("info", {}), indent=4, default=str))
# print(json.dumps(x_data.get("info", {}), indent=4, default=str))

# print("\n===== POSTS =====")
# insta_posts = insta_data.get("posts", [])
# tiktok_posts = tiktok_data.get("posts", [])
# x_posts = x_data.get("posts", [])

# print(f"Total Instagram posts: {len(insta_posts)}")
# for i, post in enumerate(insta_posts[:2]):
#     print(f"\nInstagram Post {i+1}:")
#     print(json.dumps(post, indent=4, default=str))

# print(f"Total TikTok posts: {len(tiktok_posts)}")
# for i, post in enumerate(tiktok_posts[:2]):
#     print(f"\nTikTok Post {i+1}:")
#     print(json.dumps(post, indent=4, default=str))
# print(f"Total X posts: {len(x_posts)}")
# for i, post in enumerate(x_posts[:2]):
#     print(f"\nX Post {i+1}:")
#     print(json.dumps(post, indent=4, default=str))

# print("\n===== COMMENTS =====")
# insta_comments = insta_data.get("comments", [])
# tiktok_comments = tiktok_data.get("comments", [])
# x_comments = x_data.get("comments", [])

# print(f"Total Instagram comment files: {len(insta_comments)}")
# print(f"Total TikTok comment files: {len(tiktok_comments)}")
# print(f"Total X comment files: {len(x_comments)}")

# if insta_comments:
#     print("\nSample Instagram comments:")
#     print(json.dumps(insta_comments[0], indent=4, default=str))
# if tiktok_comments:
#     print("\nSample TikTok comments:")
#     print(json.dumps(tiktok_comments[0], indent=4, default=str))
# if x_comments:
#     print("\nSample X comments:")
#     print(json.dumps(x_comments[0], indent=4, default=str))