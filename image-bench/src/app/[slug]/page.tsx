import { parsePrompts } from "@/app/lib/parse-prompts";
export default function Home({ params }: { params: { slug: string } }) {
  const { slug } = params;
  const prompts = parsePrompts();
  const captionSources = Array.from(
    new Set(prompts.map((p) => p.caption_source))
  );

  return (
    <main className="p-4">
      <div className="grid grid-cols-4 gap-4">
        {captionSources.map((source) => (
          <div key={source} className="space-y-2">
            <h2 className="text-xl font-bold sticky top-0 bg-white z-10 py-2 text-center">
              {source}
            </h2>
            <div className="space-y-2">
              {prompts
                .filter((p) => p.caption_source === source)
                .map((prompt) => (
                  <div key={prompt.prompt_sha}>
                    <img
                      alt={`${source} - ${prompt.prompt_sha}`}
                      title={prompt.prompt}
                      src={`/${slug}/${source}/${prompt.prompt_sha}-${prompt.seed}.webp`}
                      className="w-full h-auto"
                    />
                  </div>
                ))}
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
