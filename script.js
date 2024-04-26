const baseApiUrl = 'http://127.0.0.1:8000'; //URL where backend is running
// Update:
// 1
async function Create_Poll(){
    const create_poll_input_user_id = document.getElementById('create_poll_input_user_id').value;
    const create_poll_input_poll_id = document.getElementById('create_poll_input_poll_id').value;
    const create_poll_input_question = document.getElementById('create_poll_input_question').value;
    const create_poll_input_option1 = document.getElementById('create_poll_input_option1').value;
    const create_poll_input_option2 = document.getElementById('create_poll_input_option2').value;
    const create_poll_input_option3 = document.getElementById('create_poll_input_option3').value;
    const create_poll_input_option4 = document.getElementById('create_poll_input_option4').value;
    const create_poll_input_option_id1 = document.getElementById('create_poll_input_option_id1').value;
    const create_poll_input_option_id2 = document.getElementById('create_poll_input_option_id2').value;
    const create_poll_input_option_id3 = document.getElementById('create_poll_input_option_id3').value;
    const create_poll_input_option_id4 = document.getElementById('create_poll_input_option_id4').value;
    const create_poll_input_tag = document.getElementById('create_poll_input_tag').value;
    const create_poll_input_created_date = document.getElementById('create_poll_input_created_date').value;
    const create_poll_input_created_time = document.getElementById('create_poll_input_created_time').value;
    console.log(create_poll_input_question);
    // console.log(typeof(channel_id_input));
    try {
        const response = await fetch(`${baseApiUrl}/Create_Poll`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                user_id: create_poll_input_user_id,  
                poll_id: create_poll_input_poll_id,
                question: create_poll_input_question,
                option_id1:  create_poll_input_option_id1,
                option_id2: create_poll_input_option_id2,
                option_id3: create_poll_input_option_id3,
                option_id4: create_poll_input_option_id4,
                option1: create_poll_input_option1,
                option2: create_poll_input_option2,
                option3: create_poll_input_option3,
                option4: create_poll_input_option4,
                tag: create_poll_input_tag,
                created_date: create_poll_input_created_date,
                created_time:create_poll_input_created_time,
            }),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 2 
async function Create_Channel(){
    const create_channel_input_user_id = document.getElementById('create_channel_input_user_id').value;
    const create_channel_input_channel_name = document.getElementById('create_channel_input_channel_name').value;
    const create_channel_input_channel_id = document.getElementById('create_channel_input_channel_id').value;
    try {
        const response = await fetch(`${baseApiUrl}/Create_Channel`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id:create_channel_input_user_id,
                channel_name:create_channel_input_channel_name,
                channel_id: create_channel_input_channel_id,  // Use the correct field name
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 3
async function Create_Profile(){
    const create_profile_input_user_id = document.getElementById('create_profile_input_user_id').value;
    const create_profile_input_username = document.getElementById('create_profile_input_username').value;
    const create_profile_input_photoURL = document.getElementById('create_profile_input_photoURL').value;
    const create_profile_input_aboutMe = document.getElementById('create_profile_input_aboutMe').value;
    console.log(create_profile_input_aboutMe)
    try {
        const response = await fetch(`${baseApiUrl}/Create_Profile`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id: create_profile_input_user_id,
                username: create_profile_input_username,
                photoURL: create_profile_input_photoURL,
                about_me: create_profile_input_aboutMe,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 4
async function UpVote(){
    const upvote_input_poll_id = document.getElementById('upvote_input_poll_id').value;
    try {
        const response = await fetch(`${baseApiUrl}/UpVote`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                poll_id: upvote_input_poll_id,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 5
async function DownVote(){
    const downvote_input_poll_id = document.getElementById('downvote_input_poll_id').value;
    try {
        const response = await fetch(`${baseApiUrl}/DownVote`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                poll_id: downvote_input_poll_id,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 6
async function Comment(){
    const Comment_input_user_id = document.getElementById('Comment_input_user_id').value;
    const Comment_input_poll_id = document.getElementById('Comment_input_poll_id').value;
    const Comment_input_comment_id = document.getElementById('Comment_input_comment_id').value;
    const Comment_input_comment = document.getElementById('Comment_input_comment').value;
    console.log(Comment_input_comment)
    try {
        const response = await fetch(`${baseApiUrl}/Comment`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id:Comment_input_user_id, 
                poll_id: Comment_input_poll_id, 
                comment_id:Comment_input_comment_id, 
                comment:Comment_input_comment,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 7
async function Edit_Profile(){
    const Edit_Profile_input_user_id = document.getElementById('Edit_Profile_input_user_id').value;
    const Edit_Profile_input_username = document.getElementById('Edit_Profile_input_username').value;
    const Edit_Profile_input_visibility = document.querySelector('input[name="visibility"]:checked').value;  
    const Edit_Profile_input_photoURL = document.getElementById('Edit_Profile_input_photoURL').value;
    const Edit_Profile_input_aboutMe = document.getElementById('Edit_Profile_input_aboutMe').value;
    console.log(Edit_Profile_input_visibility)
    try {
        const response = await fetch(`${baseApiUrl}/Edit_Profile`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id: Edit_Profile_input_user_id,
                username: Edit_Profile_input_username,
                visibility: Edit_Profile_input_visibility,
                photoURL: Edit_Profile_input_photoURL,
                about_me: Edit_Profile_input_aboutMe,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 8
async function Follow(){
    const Follow_input_user_id1 = document.getElementById('Follow_input_user_id1').value;
    const Follow_input_user_id2 = document.getElementById('Follow_input_user_id2').value;

    // console.log(Edit_Profile_input_visibility)
    try {
        const response = await fetch(`${baseApiUrl}/Follow`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id1: Follow_input_user_id1,
                user_id2: Follow_input_user_id2,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 9
async function Sway(){
    const sway_input_poll_id = document.getElementById('sway_input_poll_id').value;
    const sway_input_option_id = document.getElementById('sway_input_option_id').value;
    // console.log(Edit_Profile_input_visibility)
    try {
        const response = await fetch(`${baseApiUrl}/Sway`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                poll_id: sway_input_poll_id,
                option_id: sway_input_option_id,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 10
async function Subsribe_Channel(){
    const subscribe_channel_input_user_id = document.getElementById('subscribe_channel_input_user_id').value;
    const subscribe_channel_input_channel_id = document.getElementById('subscribe_channel_input_channel_id').value;
    // console.log(typeof(channel_id_input));
    try {
        const response = await fetch(`${baseApiUrl}/Subsribe_Channel`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                user_id: subscribe_channel_input_user_id,
                channel_id: subscribe_channel_input_channel_id,  // Use the correct field name
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 11

async function Comment_Like(){
    const Comment_Like_input_channel_id = document.getElementById('Comment_Like_input_channel_id').value; //change area
    const Comment_Like_input_user_id = document.getElementById('Comment_Like_input_user_id').value; 
    console.log(Comment_Like_input_channel_id);
    console.log(Comment_Like_input_user_id);
    try {
        const response = await fetch(`${baseApiUrl}/Comment_Like`, { //change area
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                comment_id: Comment_Like_input_channel_id,  //change area
                user_id: Comment_Like_input_user_id , 
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}
// 12
async function Comment_Dislike(){
    const Comment_Dislike_input_channel_id = document.getElementById('Comment_Dislike_input_channel_id').value; //change area
    const Comment_Dislike_input_user_id = document.getElementById('Comment_Dislike_input_user_id').value; 
    console.log(Comment_Dislike_input_channel_id);
    console.log(Comment_Dislike_input_user_id);
    try {
        const response = await fetch(`${baseApiUrl}/Comment_Dislike`, { //change area
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                comment_id: Comment_Dislike_input_channel_id,  //change area
                user_id: Comment_Dislike_input_user_id , 
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    } catch (error) {
        console.error('Error subscribing to channel:', error);
    }
}


// Response:
// 1
// 2
// 3
async function Profile() {
    const profile_input = document.getElementById('profile_input').value;
    console.log(profile_input);
    console.log(typeof(profile_input));
    try {
        const response = await fetch(`${baseApiUrl}/Profile?user_id=${profile_input}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const responseData = await response.json();
        console.log(responseData)
        const profile_response_username = document.getElementById('profile_response_username');
        const profile_response_photoURL = document.getElementById('profile_response_photoURL');
        const profile_response_about = document.getElementById('profile_response_about');

        profile_response_username.innerText = responseData.username;
        profile_response_photoURL.innerText = responseData.photoURL;
        profile_response_about.innerText = responseData.about_me;

    } catch (error) {
        console.error('Error fetching profile data:', error);
    }
}