import React, { useState, useEffect } from 'react';
import './index.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [tickets, setTickets] = useState([]);
  const token = 'token123';
  const userId = 'user123';

  const askQuery = async () => {
    const res = await fetch('http://localhost:8000/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': token,
      },
      body: JSON.stringify({ query, user_id: userId }),
    });
    const data = await res.json();
    setResponse(data.answer);
    fetchTickets();
  };

  const fetchTickets = async () => {
    const res = await fetch(`http://localhost:8000/tickets?user_id=${userId}`, {
      headers: { 'Authorization': token },
    });
    const data = await res.json();
    setTickets(data);
  };

  useEffect(() => { fetchTickets(); }, []);

  return (
    <div className="min-h-screen p-6 bg-gray-100 text-gray-900">
      <div className="max-w-2xl mx-auto bg-white p-6 rounded-xl shadow">
        <h1 className="text-xl font-bold mb-4">HR Assistant</h1>
        <textarea
          className="w-full border rounded p-2 mb-4"
          rows={4}
          placeholder="Ask HR a question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          onClick={askQuery}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >Ask</button>
        <div className="mt-4">
          <strong>Response:</strong>
          <p className="mt-2 whitespace-pre-wrap">{response}</p>
        </div>
        <hr className="my-6" />
        <h2 className="text-lg font-semibold mb-2">Your IT Tickets</h2>
        <ul className="space-y-2">
          {tickets.map(t => (
            <li key={t.id} className="bg-gray-200 p-2 rounded">
              #{t.id}: {t.issue}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
