-- Create option_table
CREATE TABLE option_table (
    option_id TEXT PRIMARY KEY,
    options TEXT,
    counts INTEGER DEFAULT 0 -- Default value set to 0
);
-- Create comment_table
CREATE TABLE comment_table (
    comment_id TEXT PRIMARY KEY, -- Primary key constraint added
    user_created TEXT,
    comment TEXT,
    like_count INTEGER DEFAULT 0,
    dislike_count INTEGER DEFAULT 0,
    user_liked TEXT,
    user_disliked TEXT
);
-- Create poll_table
CREATE TABLE poll_table (
    poll_id TEXT PRIMARY KEY,
    question TEXT,
    options TEXT, -- Comma-separated text containing option_ids
    tags TEXT,
    user_created TEXT,
    created_time TIME,
    created_date DATE,
    ends_at DATE,
    days_ago INTEGER DEFAULT 0,
    days_left INTEGER DEFAULT 999999,
    user_interacted INTEGER DEFAULT 0,
    up_vote_count INTEGER DEFAULT 0,
    down_vote_count INTEGER DEFAULT 0,
    comment_list TEXT  -- Comma-separated text containing comment_ids
);
-- Create channel_table
CREATE TABLE channel_table (
    channel_id TEXT PRIMARY KEY,
    channel_name TEXT,
    subscriber_count INTEGER DEFAULT 0,
    polls_in_it TEXT  -- Comma-separated text containing poll_ids
);

-- Create user_table
CREATE TABLE user_table (
    user_id TEXT PRIMARY KEY,
    username TEXT,
    isSubscribed INTEGER, -- 0 or 1 for boolean value
    channels_created TEXT, -- Comma-separated text containing channel_ids
    channel_subscribed TEXT, -- Comma-separated text containing subscribed channel_ids
    polls TEXT , -- Comma-separated text containing created poll_ids
    followers TEXT, -- Comma-separated text containing user_ids of followers
    followings TEXT, -- Comma-separated text containing user_ids of users being followed
    photoURL TEXT,
    subscription_data TEXT,
    about_me TEXT,
    visibility INTEGER, -- 0 or 1 for boolean value
    score INTEGER Default 0
);

CREATE TABLE organization_table(
    organization_id TEXT PRIMARY KEY,
    organization_name TEXT,
    organization_size INTEGER,
    organization_type TEXT DEFAULT 'Startup',
    organization_email TEXT,
    org_location TEXT,
    channels_created TEXT, -- Comma-separated text containing channel_ids
    channel_subscribed TEXT, -- Comma-separated text containing subscribed channel_ids
    polls TEXT, -- Comma-separated text containing created poll_ids
    followers TEXT, -- Comma-separated text containing user_ids of followers
    followings TEXT, -- Comma-separated text containing user_ids of users being followed
    photoURL TEXT,
    subscription_data TEXT,
    about_me TEXT
);