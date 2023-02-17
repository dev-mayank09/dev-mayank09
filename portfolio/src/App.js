import './App.css';
import Navbar from './Components/Navbar/Navbar';
import UserProfile from './Components/UserProfile/UserProfile';
import PersonalDetails from './Components/PersonalDetails/PersonalDetails';
import Skills from './Components/Skills/Skills';
import Projects from './Components/Projects/Projects';
import Statistics from './Components/Statistics/Statistics';
import Footer from './Components/Footer/Footer';
import GithubCalender from './Components/GithubCalender/GithubCalender';
import Contact from './Components/Contact/Contact';

function App() {
  return (
    <div className="App">
      <Navbar />
      <UserProfile />
      <PersonalDetails />
      <Skills />
      <Projects />
      <GithubCalender />
      <Statistics />
      <Contact />
      <Footer />
    </div>
  );
}

export default App;
