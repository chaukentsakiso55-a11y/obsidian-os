import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
test("scoring source exports expected functions", () => {
 const source = readFileSync(new URL("../src/scoring.ts", import.meta.url), "utf8");
 assert.match(source, /export function analyzeText/);
 assert.match(source, /export function analyzeUrl/);
 assert.match(source, /export function scoreSignals/);
});
