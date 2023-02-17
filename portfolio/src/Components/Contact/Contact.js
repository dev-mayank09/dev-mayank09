import './Contact.css';
import ContactCard from './ContactCard';

function Contact(props) {
    return <div className="Contact">
        <h1>Contact Me</h1>
        <div className="ContactCardsDiv">
            <ContactCard icon="fa-brands fa-linkedin" heading="LinkedIn" text="You can contact me on LinkedIn" link="https://www.linkedin.com/in/mayank-sharma-2a25ab251/" link_text="mayank-sharma" />
            <ContactCard icon="fa-solid fa-phone" heading="Phone" text="Here is My Phone Number" link="#" link_text="+919875335104" />
            <ContactCard icon="fa-solid fa-envelope" heading="Email" text="You can Simply mail me just by clicking on my email" link="#" link_text="mayanksharma5104@gmail.com" />
            <ContactCard icon="fa-solid fa-location-dot" heading="Location" text="Kolkata, West Bengal" link="https://www.google.com/maps/place/Kolkata,+West+Bengal/@22.5354273,88.3473527,12z/data=!3m1!4b1!4m5!3m4!1s0x39f882db4908f667:0x43e330e68f6c2cbc!8m2!3d22.572646!4d88.363895" link_text="View on Google map" />
        </div>

    </div>
}

export default Contact;