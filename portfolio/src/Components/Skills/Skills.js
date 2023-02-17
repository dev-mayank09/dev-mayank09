import SkillCard from '../SkillCard/SkillCard';
import './Skills.css';

function Skills(props) {
    return <div className="Skills">
        <h1>SKILLS</h1>
        <div className="skillsContainer">
            <SkillCard image="https://cdn-icons-png.flaticon.com/128/174/174854.png" skill_name="HTML" />
            <SkillCard image="https://mohitkss.github.io/static/media/css3.845e8eb63836bef093cf.png" skill_name="CSS" />
            <SkillCard image="https://cdn-icons-png.flaticon.com/128/5968/5968292.png" skill_name="JavaScript" />
            <SkillCard image="https://img.icons8.com/color/48/000000/react-native.png" skill_name="ReactJS" />
            <SkillCard image="https://raw.githubusercontent.com/devicons/devicon/master/icons/redux/redux-original.svg" skill_name="Redux" />
            <SkillCard image="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original.svg" skill_name="NodeJS" />
            <SkillCard image="http://www.kaustubh.app/img/expressjs.8f887594.svg" skill_name="ExpressJS" />
            <SkillCard image="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg" skill_name="MongoDB" />
            <SkillCard image="https://cdn-icons-png.flaticon.com/128/733/733609.png" skill_name="Git/Github" />
            <SkillCard image="https://camo.githubusercontent.com/93b32389bf746009ca2370de7fe06c3b5146f4c99d99df65994f9ced0ba41685/68747470733a2f2f7777772e766563746f726c6f676f2e7a6f6e652f6c6f676f732f676574706f73746d616e2f676574706f73746d616e2d69636f6e2e737667" skill_name="Postman" />
        </div>
    </div>
}

export default Skills;