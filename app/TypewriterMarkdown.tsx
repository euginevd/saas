'use client';

import { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

const CHARS_PER_TICK = 3;
const TICK_MS = 20;

export default function TypewriterMarkdown({ text }: { text: string }) {
  const [visibleChars, setVisibleChars] = useState(0);

  useEffect(() => {
    setVisibleChars(0);
    const interval = setInterval(() => {
      setVisibleChars((current) => {
        const next = current + CHARS_PER_TICK;
        if (next >= text.length) clearInterval(interval);
        return next;
      });
    }, TICK_MS);

    return () => clearInterval(interval);
  }, [text]);

  return (
    <ReactMarkdown remarkPlugins={[remarkGfm]}>
      {text.slice(0, visibleChars)}
    </ReactMarkdown>
  );
}
