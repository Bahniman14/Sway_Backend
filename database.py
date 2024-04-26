import sqlite3
import datetime
import psycopg2
# 0.
# def create_connection(db_file):
#     """Create a connection to the SQLite database."""
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(f"Connected to SQLite database: {db_file}")
#         return conn
#     except sqlite3.Error as e:
#         print(f"Error connecting to SQLite database: {e}")
#         return None
# 1.

def create_poll(conn, create_poll_input):
    # Extract data from the poll_data object
    user_id = create_poll_input.user_id
    poll_id = create_poll_input.poll_id
    question = create_poll_input.question
    option_id1 = create_poll_input.option_id1
    option_id2 = create_poll_input.option_id2
    option_id3 = create_poll_input.option_id3
    option_id4 = create_poll_input.option_id4
    option1 = create_poll_input.option1
    option2 = create_poll_input.option2
    option3 = create_poll_input.option3
    option4 = create_poll_input.option4
    tags = create_poll_input.tag
    created_date = create_poll_input.created_date
    created_time = create_poll_input.created_time

    # Convert created_time to a string representation
    created_time_str = created_time.strftime('%H:%M:%S')

    # Calculate days_ago
    days_ago = (datetime.date.today() - created_date).days

    try:
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Insert poll_id into poll_table
        cursor.execute(
            """
            INSERT INTO poll_table (poll_id, question, options, tags, user_created, created_date, created_time, days_ago)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (poll_id, question, f"{option_id1},{option_id2},{option_id3},{option_id4}", tags, user_id, created_date, created_time_str, days_ago)
        )

        # Add poll_id to user's list of polls in user_table
        cursor.execute(
            """
            UPDATE user_table
            SET polls = COALESCE(polls || ',', '') || %s
            WHERE user_id = %s
            """,
            (poll_id, user_id)
        )

        # Insert options into option_table
        cursor.execute(
            """
            INSERT INTO option_table (option_id, options)
            VALUES (%s, %s), (%s, %s), (%s, %s), (%s, %s)
            """,
            (option_id1, option1, option_id2, option2, option_id3, option3, option_id4, option4)
        )

        # Commit the transaction
        conn.commit()
        return {"message": "Poll created successfully"}

    except psycopg2.Error as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print(f"Error creating poll: {e}")
        return {"error": "Poll creation failed"}

    finally:
        # Close the cursor
        if cursor:
            cursor.close()

# 2.
def create_channel(conn, create_channel_input):
    # Extract data from the create_channel_input object
    user_id = create_channel_input.user_id
    channel_name = create_channel_input.channel_name
    channel_id = create_channel_input.channel_id

    try:
        # Insert channel_id and channel_name into channel_table
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO channel_table (channel_id, channel_name, subscriber_count, polls_in_it)
            VALUES (?, ?, 0, '')
            """,
            (channel_id, channel_name)
        )
        conn.commit()
        cursor.close()

        # Add channel_id to user's list of channels_created in user_table
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE user_table
            SET channels_created = IFNULL(channels_created || ',', '') || ?
            WHERE user_id = ?
            """,
            (channel_id, user_id)
        )
        conn.commit()
        cursor.close()

        return {"message": "Channel created successfully"}

    except sqlite3.Error as e:
        print(f"Error creating channel: {e}")
        return {"error": "Failed to create channel"}

# 3.
def create_profile(conn, create_profile_input):
    # Extract data from the create_profile_input object
    user_id = create_profile_input.user_id
    username = create_profile_input.username
    photoURL = create_profile_input.photoURL
    about_me = create_profile_input.about_me

    # Set default values for other attributes
    channels_created = ""
    channel_subscribed = ""
    polls = ""
    followers = ""
    followings = ""
    subscription_data = ""
    isSubscribed = 0  # False
    visibility = 1  # True
    score = 0

    try:
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Insert data into user_table
        cursor.execute(
            """
            INSERT INTO user_table (user_id, username, photoURL, about_me, channels_created, channel_subscribed,
                                    polls, followers, followings, subscription_data, isSubscribed, visibility, score)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (user_id, username, photoURL, about_me, channels_created, channel_subscribed,
             polls, followers, followings, subscription_data, isSubscribed, visibility, score)
        )

        # Commit the transaction
        conn.commit()

        return {"message": "Profile created successfully"}

    except psycopg2.Error as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print(f"Error creating profile: {e}")
        return {"error": "Profile creation failed"}

    finally:
        # Close the cursor
        if cursor:
            cursor.close()

# 4.
def upvote(conn, upvote_input):
    # Extract data from the input object
    poll_id = upvote_input.poll_id
    
    try:
        # Increase the up_vote_count by 1 for the received poll_id in poll_table
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE poll_table
            SET up_vote_count = up_vote_count + 1
            WHERE poll_id = ?
            """,
            (poll_id,)
        )
        conn.commit()
        cursor.close()
        
        return {"message": f"Upvoted poll with ID: {poll_id}"}
    
    except sqlite3.Error as e:
        print(f"Error upvoting poll: {e}")
        return {"error": "Unable to upvote the poll"}

# 5.
def downvote(conn, downvote_input):
    # Extract data from the input object
    poll_id = downvote_input.poll_id
    
    try:
        # Increase the up_vote_count by 1 for the received poll_id in poll_table
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE poll_table
            SET down_vote_count = down_vote_count + 1
            WHERE poll_id = ?
            """,
            (poll_id,)
        )
        conn.commit()
        cursor.close()
        
        return {"message": f"Upvoted poll with ID: {poll_id}"}
    
    except sqlite3.Error as e:
        print(f"Error upvoting poll: {e}")
        return {"error": "Unable to upvote the poll"}

# 6.
def comment(conn, comment_input):
    # Extract data from the comment_input object
    user_id = comment_input.user_id
    poll_id = comment_input.poll_id
    comment_id = comment_input.comment_id
    comment_text = comment_input.comment
    
    # Add comment_id to the list of comments in poll_table for the specific poll_id
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE poll_table
        SET comments = IFNULL(comments || ',', '') || ?
        WHERE poll_id = ?
        """,
        (comment_id, poll_id)
    )
    conn.commit()
    cursor.close()

    # Insert comment data into comment_table
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO comment_table (comment_id, user_created, comment, like_count, dislike_count, user_liked, user_disliked)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (comment_id, user_id, comment_text, 0, 0, "", "")
    )
    conn.commit()
    cursor.close()

    return {"message": "Comment added successfully"}
# 7.

def edit_profile(conn, edit_profile_input):
    # Extract data from the edit_profile_input object
    user_id = edit_profile_input.user_id
    username = edit_profile_input.username
    visibility = edit_profile_input.visibility
    photoURL = edit_profile_input.photoURL
    about_me = edit_profile_input.about_me
    
    try:
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Update user details in user_table
        cursor.execute(
            """
            UPDATE user_table
            SET username = %s,
                visibility = %s,
                photoURL = %s,
                about_me = %s
            WHERE user_id = %s
            """,
            (username, visibility, photoURL, about_me, user_id)
        )

        # Commit the transaction
        conn.commit()
        
        return {"message": "Profile updated successfully"}

    except psycopg2.Error as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print(f"Error updating profile: {e}")
        return {"error": "Profile update failed"}

    finally:
        # Close the cursor
        if cursor:
            cursor.close()

# 8.
def follow(conn, follow_input):
    user_id1 = follow_input.user_id1
    user_id2 = follow_input.user_id2

    # Add user_id1 to the list of followers for user_id2
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE user_table
        SET followers = IFNULL(followers || ',', '') || ?
        WHERE user_id = ?
        """,
        (user_id1, user_id2)
    )
    conn.commit()
    cursor.close()

    # Add user_id2 to the list of followings for user_id1
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE user_table
        SET followings = IFNULL(followings || ',', '') || ?
        WHERE user_id = ?
        """,
        (user_id2, user_id1)
    )
    conn.commit()
    cursor.close()

    return {"message": f"User {user_id1} is now following User {user_id2}"}

# 9.
def sway(conn, sway_input):
    poll_id = sway_input.poll_id
    option_id = sway_input.option_id

    try:
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Increase user_interacted by 1 for the specified poll_id in poll_table
        cursor.execute(
            """
            UPDATE poll_table
            SET user_interacted = user_interacted + 1
            WHERE poll_id = %s
            """,
            (poll_id,)
        )

        # Increase count by 1 for the specified option_id in option_table
        cursor.execute(
            """
            UPDATE option_table
            SET counts = counts + 1
            WHERE option_id = %s
            """,
            (option_id,)
        )

        # Commit the transaction
        conn.commit()

        return {"message": "Sway operation performed successfully"}

    except psycopg2.Error as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print(f"Error performing sway operation: {e}")
        return {"error": "Sway operation failed"}

    finally:
        # Close the cursor
        if cursor:
            cursor.close()

# 10.
def subscribe_channel(conn, subscribe_channel_input):
    # Extract data from the subscribe_channel_input object
    user_id = subscribe_channel_input.user_id
    channel_id = subscribe_channel_input.channel_id
    
    try:
        # Increase subscriber_count by 1 for the received channel_id in channel_table
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE channel_table
            SET subscriber_count = subscriber_count + 1
            WHERE channel_id = ?
            """,
            (channel_id,)
        )
        conn.commit()
        cursor.close()
        
        # Add the received channel_id in the channel_subscribed list for the received user_id in user_table
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE user_table
            SET channel_subscribed = IFNULL(channel_subscribed || ',', '') || ?
            WHERE user_id = ?
            """,
            (channel_id, user_id)
        )
        conn.commit()
        cursor.close()

        return {"message": "Channel subscribed successfully"}
    
    except sqlite3.Error as e:
        print(f"Error subscribing to channel: {e}")
        return {"message": f"Error subscribing to channel: {e}"}

# 11.
def comment_like(conn, comment_like_input):
    # Extract data from the comment_like_input object
    comment_id = comment_like_input.comment_id
    user_id = comment_like_input.user_id

    # Increase the like_count by 1 for the particular comment_id in comment_table
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE comment_table
        SET like_count = like_count + 1,
            user_liked = IFNULL(user_liked || ',', '') || ?
        WHERE comment_id = ?
        """,
        (user_id, comment_id)
    )
    conn.commit()
    cursor.close()

    return {"message": "Comment liked successfully"}

# 12.
def comment_dislike(conn, comment_dislike_input):
    # Extract data from the comment_dislike_input object
    comment_id = comment_dislike_input.comment_id
    user_id = comment_dislike_input.user_id

    try:
        # Increase the dislike_count by 1 for the particular comment_id in comment_table
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE comment_table
            SET dislike_count = dislike_count + 1,
                user_disliked = IFNULL(user_disliked || ',', '') || ?
            WHERE comment_id = ?
            """,
            (user_id, comment_id)
        )
        conn.commit()
        cursor.close()

        return {"message": "Comment disliked successfully"}
    except Exception as e:
        return {"error": str(e)}

# responce:
# 3.

def return_profile(conn, user_id):
    profile_data = {}

    try:
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute SQL query to fetch profile data based on user_id
        cursor.execute("SELECT username, photoURL, about_me FROM user_table WHERE user_id=%s", (user_id,))

        # Fetch the profile data
        profile_row = cursor.fetchone()

        if profile_row:
            # Extract profile information
            username, photoURL, about_me = profile_row

            # Assign profile data to the dictionary
            profile_data["username"] = username
            profile_data["photoURL"] = photoURL
            profile_data["about_me"] = about_me
        else:
            # If no profile data found, return None
            return None

    except psycopg2.Error as e:
        # Print any errors that occur during database query
        print(f"Error fetching profile data: {e}")
        return None

    finally:
        # Close the cursor
        if cursor:
            cursor.close()

    return profile_data

