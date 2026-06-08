import { PricingTable } from '@clerk/nextjs';

export default function PricingPage() {
  return (
    <main className="min-h-screen flex flex-col items-center gap-8 p-8 sm:p-16 font-sans bg-linear-to-b from-slate-50 to-slate-100 dark:from-slate-950 dark:to-slate-900">
      <div className="text-center">
        <h1 className="text-4xl font-bold tracking-tight mb-2">Pricing</h1>
        <p className="text-slate-500 dark:text-slate-400">
          Upgrade to Pro for unlimited project ideas.
        </p>
      </div>
      <PricingTable />
    </main>
  );
}
