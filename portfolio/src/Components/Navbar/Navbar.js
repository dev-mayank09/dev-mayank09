import "./Navbar.css";
import Button from "../Button/Button";

function Navbar() {
    return (
        <div className="Navbar">
            <div><h1>Mayank</h1></div>
            <div>
                <a href="#">HOME</a>
                <a href="#">ABOUT</a>
                <a href="#">SKILLS</a>
                <a href="#">PROJECTS</a>
                <a href="#">CONTACT</a>
                <Button text="RESUME"/>
            </div>

        </div>
    );
}

export default Navbar;