import fs from "node:fs";
import path from "node:path";

interface Prompt {
  caption_source: string;
  prompt_sha: string;
  seed: number;
}

export function parsePrompts(): Prompt[] {
  const filePath = path.join(
    process.cwd(),
    "src",
    "app",
    "lib",
    "manifest.jsonl"
  );
  const fileContent = fs.readFileSync(filePath, "utf-8");
  return fileContent
    .trim()
    .split("\n")
    .map((line) => JSON.parse(line));
}
