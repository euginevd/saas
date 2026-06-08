'use client';

import { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';
const CHARS_PER_TICK = 3;
const TICK_MS = 20;

export default function Home() {
  const [idea, setIdea] = useState('');
  const [loading, setLoading] = useState(false);
  const [visibleChars, setVisibleChars] = useState(0);

  // calls the FastAPI backend to get a new idea
  const fetchIdea = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_URL}/api`, { cache: 'no-store' });
      const data = await res.json();
      setIdea(data.idea);
    } finally {
      setLoading(false);
    }
  };

  // load an idea on first render
  useEffect(() => {
    fetchIdea();
  }, []);

  // typewriter effect: reveal the idea text a few characters at a time
  useEffect(() => {
    setVisibleChars(0);
    const interval = setInterval(() => {
      setVisibleChars((current) => {
        const next = current + CHARS_PER_TICK;
        if (next >= idea.length) clearInterval(interval);
        return next;
      });
    }, TICK_MS);

    return () => clearInterval(interval);
  }, [idea]);

  return (
    <main className="min-h-screen flex flex-col items-center gap-8 p-8 sm:p-16 font-sans bg-linear-to-b from-slate-50 to-slate-100 dark:from-slate-950 dark:to-slate-900">
      <div className="text-center">
        <h1 className="text-4xl font-bold tracking-tight mb-2">Project Idea</h1>
        <p className="text-slate-500 dark:text-slate-400">
          A fresh cloud + security + AI project idea, generated on every visit.
        </p>
      </div>
      {/* idea card: renders only the characters revealed so far */}
      <div className="w-full max-w-2xl p-6 sm:p-8 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-lg prose dark:prose-invert prose-headings:font-semibold">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {idea.slice(0, visibleChars)}
        </ReactMarkdown>
      </div>
      {/* triggers a fresh fetch from the backend */}
      <button
        onClick={fetchIdea}
        disabled={loading}
        className="px-6 py-3 rounded-full bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-medium shadow-md hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed transition"
      >
        {loading ? 'Generating…' : 'Generate new idea'}
      </button>
    </main>
  );
}
