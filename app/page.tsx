import TypewriterMarkdown from './TypewriterMarkdown';

export default async function Home() {
  const baseUrl = process.env.VERCEL_URL
    ? `https://${process.env.VERCEL_URL}`
    : 'http://localhost:8000';
  const res = await fetch(`${baseUrl}/api`, { cache: 'no-store' });
  const { idea } = await res.json();

  return (
    <main className="min-h-screen flex flex-col items-center gap-8 p-8 sm:p-16 font-sans bg-linear-to-b from-slate-50 to-slate-100 dark:from-slate-950 dark:to-slate-900">
      <div className="text-center">
        <h1 className="text-4xl font-bold tracking-tight mb-2">Project Idea</h1>
        <p className="text-slate-500 dark:text-slate-400">
          A fresh cloud + security + AI project idea, generated on every visit.
        </p>
      </div>
      <div className="w-full max-w-2xl p-6 sm:p-8 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-lg prose dark:prose-invert prose-headings:font-semibold">
        <TypewriterMarkdown text={idea} />
      </div>
    </main>
  );
}
