import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import { analyzeText, analyzeUrl, type Assessment } from "./scoring";
import "./style.css";

function App() {
  const [mode, setMode] = useState<"text" | "url">("url");
  const [value, setValue] = useState("");
  const [result, setResult] = useState<Assessment | null>(null);
  const [error, setError] = useState("");
  function check(event: React.FormEvent) {
    event.preventDefault();
    try { setResult(mode === "url" ? analyzeUrl(value) : analyzeText(value)); setError(""); }
    catch (e) { setResult(null); setError(e instanceof Error ? e.message : "Analysis failed"); }
  }
  return <main><header><span className="brand">◈ OBSIDIAN</span><span className="tag">LOCAL SECURITY PROTOTYPE</span></header>
    <section className="hero"><p className="eyebrow">CYBER PULSE · 2027</p><h1>Your privacy.<br/><em>Your control.</em></h1><p>Explore suspicious links and messages with transparent, offline heuristic analysis. Nothing is uploaded.</p></section>
    <section className="panel"><h2>Threat assessment</h2><div className="tabs"><button aria-pressed={mode === "url"} onClick={() => {setMode("url");setResult(null);}}>URL analysis</button><button aria-pressed={mode === "text"} onClick={() => {setMode("text");setResult(null);}}>Message analysis</button></div>
    <form onSubmit={check}><label htmlFor="input">{mode === "url" ? "URL to assess" : "Message to assess"}</label><textarea id="input" maxLength={10000} required value={value} onChange={e => setValue(e.target.value)} placeholder={mode === "url" ? "https://example.org" : "Paste a suspicious message"}/><button className="submit">Analyze locally →</button></form>
    {error && <p role="alert">{error}</p>}{result && <div className="result" role="status"><strong>{result.risk.toUpperCase()}</strong><span>{result.score === null ? "Invalid URL" : "Heuristic score: " + result.score + "/100"}</span><p>{result.signals.length ? result.signals.join(" · ") : "No known indicators matched."}</p><small>A low score does not prove safety. No external reputation checks are performed.</small></div>}</section>
    <footer>OBSIDIAN v0.1 · Offline by default · No account required</footer></main>;
}
createRoot(document.getElementById("root")!).render(<React.StrictMode><App/></React.StrictMode>);
