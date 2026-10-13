import { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

const example = {
  schema_version: '1.0', scenario_id: 'example-only', basis: 'scenario',
  source_ids: ['SYNTHETIC-EXAMPLE'],
  intervals: [{ mean_it_power_kw: 10, duration_hours: 8 }, { mean_it_power_kw: 4, duration_hours: 16 }],
  repeat_days: 1,
};

function App() {
  const [input, setInput] = useState(JSON.stringify(example, null, 2));
  const [output, setOutput] = useState('');
  const [busy, setBusy] = useState(false);
  async function evaluate() {
    setBusy(true);
    try {
      const payload: unknown = JSON.parse(input);
      const response = await fetch('/api/v1/power/evaluate', {
        method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload),
      });
      const data: unknown = await response.json();
      setOutput(`${response.ok ? 'Result' : 'Validation error'}\n${JSON.stringify(data, null, 2)}`);
    } catch (error) { setOutput(error instanceof Error ? error.message : 'Request failed'); }
    finally { setBusy(false); }
  }
  return <main>
    <h1>WISP Team C workbench</h1>
    <p>Enter a power profile to calculate energy. The example uses synthetic values. PUE, tariff and carbon factor are optional evidence inputs.</p>
    <label htmlFor="request">Scenario request (JSON)</label>
    <textarea id="request" value={input} onChange={e => setInput(e.target.value)} spellCheck={false} />
    <button onClick={evaluate} disabled={busy}>{busy ? 'Calculating…' : 'Evaluate profile'}</button>
    <h2>Result</h2><pre aria-live="polite">{output || 'Results will appear here.'}</pre>
  </main>;
}

createRoot(document.getElementById('root')!).render(<App />);
