import './ContactCard.css';

function ContactCard({icon, heading, text, link, link_text}) {
    return <div className="ContactCard">
        <i class={icon}></i>
        <h2>{heading}</h2>
        <p>{text}</p>
        <a href={link}>{link_text}</a>
    </div>
}

export default ContactCard;