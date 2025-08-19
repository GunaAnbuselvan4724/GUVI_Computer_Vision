// frontend/src/App.js
import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [mood, setMood] = useState(null);

  const analyzeMood = async () => {
    const response = await fetch('http://localhost:5000/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text }),
    });
    const data = await response.json();
    setMood(data.mood);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Social Media Mood Tracker</h1>
      <textarea
        rows={5}
        cols={40}
        placeholder="Enter your social media post or mood note"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br />
      <button onClick={analyzeMood}>Analyze Mood</button>
      {mood && <h2>Mood: {mood}</h2>}
    </div>
  );
}

export default App;
