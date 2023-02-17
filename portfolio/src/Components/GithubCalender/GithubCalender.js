import React from "react";
import { GithubContributions } from "react-github-graph";
import './GithubCalender.css';

function GithubCalender() {
    return <div className="GithubCalender">
        <h1>DAYS I WORKED</h1>
        <GithubContributions username="Monks09"/>
    </div>
}

export default GithubCalender;