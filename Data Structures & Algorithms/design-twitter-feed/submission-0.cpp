class Twitter {
    int time;
    unordered_map<int, unordered_set<int>> followMap;
    unordered_map<int, vector<pair<int, int>>> tweetMap;
public:
    Twitter() : time(0) {
        
    }
    
    void postTweet(int userId, int tweetId) {
        tweetMap[userId].push_back({time++, tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<pair<int, int>> feed = tweetMap[userId];
        for (int followeeId : followMap[userId]) {
            feed.insert(feed.end(), tweetMap[followeeId].begin(), tweetMap[followeeId].end());
        }
        sort(feed.begin(), feed.end(), [](auto& a, auto& b) {
            return a.first > b.first;
        });
        vector<int> res;
        for (int i = 0; i < min((int)feed.size(), 10); i++) {
            res.push_back(feed[i].second);
        }
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        if (followeeId != followerId) {
            followMap[followerId].insert(followeeId);
        }
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followeeId != followerId) {
            followMap[followerId].erase(followeeId);
        }
        
    }
};
