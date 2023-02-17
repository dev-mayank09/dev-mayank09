import './SkillCard.css';

function SkillCard({image, skill_name}) {
    return <div className="SkillCard">
        <img src={image} alt="card" width="70px" height="70px"/>
        <p>{skill_name}</p>
    </div>
}

export default SkillCard;