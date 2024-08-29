import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-8">
        Flux style LoRA caption comparison
      </h1>
      <div className="flex flex-col space-y-4">
        <Link
          href="/schnell-4"
          className="text-blue-500 hover:underline text-xl"
        >
          Schnell 4
        </Link>
        <Link
          href="/schnell-8"
          className="text-blue-500 hover:underline text-xl"
        >
          Schnell 8
        </Link>
        <Link href="/dev-30" className="text-blue-500 hover:underline text-xl">
          Dev 30
        </Link>
      </div>
    </main>
  );
}
