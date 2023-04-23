# Question 2
### Problem statement 
Implementation of the login and logout (Django)
### Description 
The implementation of this login is a bit more complicated than the typical login process. It allows users to log in to their account for their own workspace or switch to the workspace they belong to. Once logged in, the user receives a session ID, which is used to handle various tasks such as making API calls and performing redirects. After the login process is complete, the user can log out.
### Requirements 
- Understand the login process by reading the API documentation carefully and familiarizing yourself with the inputs required for login, the expected response, and any error messages that might occur.

- Display all the information you receive back from the API after a successful login. You can use JavaScript or any other front-end framework to fetch the data from the API and display it on the user interface.

- Write code using any front-end framework / html&css based on your understanding of the API to interact with it. You can make use of the API's endpoints to make API calls and fetch data.

- Develop a user-friendly interface that follows design principles like simplicity, consistency, and readability for a better user experience. You should use a color scheme that is easy on the eyes, legible text, clear and concise labels and instructions, and display feedback to the user by showing success or error messages. Note that you do not need to design the login and logout pages
- Marks will be based on the structure of the codebase
### Notice
You are required to deploy the project on GitHub and complete it within 7 days from the date of question selection. You must share both the codebase link and the deployed link on GitHub. Based on your performance, you will be considered for the next step in the interview process.

### Documentation
1. I want you to focus on the documentation .
2. Few things you have to understand
    - Home_URL : `http://127.0.0.1:8000/` (if it is your home URL else consider your home URL)
    - login_URL : `https://100014.pythonanywhere.com/?redirect_URL=http://127.0.0.1:8000/`
    - after_logged_in_URL : `http://127.0.0.1:8000/?session_id={}` or `http://127.0.0.1:8000/?session_id={}/id={}`
    - Login_api : `https://100014.pythonanywhere.com/api/userinfo/`
    - client_admin_api : `https://100014.pythonanywhere.com/api/userinfo/`
    - logout_URL : `https://100014.pythonanywhere.com/sign-out` 
3. Create 2 functions 
    - home
    - logout
4. Logic (follow step2 to understand this statement) :
    - The home function will be your base URL . 
    - if the URL doesnot has a session_id then redirect to {login_URL}
    - After an user sucessful logged in ,Now we have two methods :
        - if the URL looks like `http://127.0.0.1:8000/?session_id={}` , post the session_id to {login_api}
            ```json
            {
                "session_id":""
            }
            ```
        - Once you get a response from the server , check if it has portfolio object , if it has then display all data and home page , else ask user to create a new portfolio and the link to be given is `http://100093.pythonanywhere.com/?session_id={}`

        - if the URL looks like `http://127.0.0.1:8000/?session_id={}/id={}` , post the session_id to {client_admin_api}
            ```json
            {
                "session_id":""
            }
            ```
        - Once you get a response from the server display the data in a proper way and the home page.
    - To logout , redirect to {logout_URL}
5. Build a beautiful home page as your wish .
### Conclusion :
Deploy your project onto any deployment service provider . 