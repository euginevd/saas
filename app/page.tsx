import ReactMarkdown from 'react-markdown';

export default async function Home() {
  const baseUrl = process.env.VERCEL_URL
    ? `https://${process.env.VERCEL_URL}`
    : 'http://localhost:8000';
  const res = await fetch(`${baseUrl}/api`, { cache: 'no-store' });
  const { idea } = await res.json();

  return (
    <main className="p-8 font-sans">
      <h1 className="text-3xl font-bold mb-4">Project Idea</h1>
      <div className="w-full max-w-2xl p-6 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-lg shadow-sm prose dark:prose-invert">
        <ReactMarkdown>{idea}</ReactMarkdown>
      </div>
    </main>
  );
}
