import './PersonalDetails.css';

function PersonalDetails(props) {
    return <div className="PersonalDetails">
        <div>
            <h3>Personal Details</h3>
            <p>------------------------------------</p>
            <p>Email:
                <span>mayanksharma5104@gmail.com</span>
            </p>
            <p>Language:
                <span>English</span>
            </p>
            <p>Nationality:
                <span>Indian</span>
            </p>
        </div>
        <div>
            <h2>I am Full Stack Web Developer</h2>
            <p>My name is Mayank Sharma, I am from Kolkata, India. Passionate Full Stack Web Developer with skills in the MERN stack, I have learned Full Stack Web Development in Masai school. Skilled in problem-solving and execution of software tasks from start to finish. I look forward to joining a company where I can contribute to individual and company growth.</p>
            <div>
                <img src="./my_signature.jpg" width="200px" alt="sign"/>
            </div>

        </div>

    </div>
}

export default PersonalDetails;